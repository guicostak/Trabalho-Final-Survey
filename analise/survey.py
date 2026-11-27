"""Análise do survey pré-registrado (Parte 2).

Lê a exportação BRUTA do Microsoft Forms (CSV da coleta ou .xlsx do botão
"Abrir no Excel"), aplica a codificação do `instrumento/codebook.csv`, as
regras de descarte E0–E5 do protocolo (§5) e calcula os testes pré-registrados
(Quadro 4), com tamanho de efeito, IC por bootstrap, correção de Holm e
margem de erro.

Uso em linha de comando (gera resultados/resultados.json e imprime o resumo):
    .venv/bin/python analise/survey.py

Para gerar o dashboard da entrega com os dados brutos mais recentes embutidos:
    .venv/bin/python analise/survey.py --dashboard ~/Downloads/Dashboard-Survey.html
"""
from __future__ import annotations

import json
import math
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

RAIZ = Path(__file__).resolve().parents[1]
DIR_BRUTOS = RAIZ / "dados" / "brutos"
ARQ_ANONIMIZADO = RAIZ / "dados" / "respostas_anonimizadas.csv"
ARQ_ABR_COD = RAIZ / "analise" / "abr_codificacao.csv"

FUSO = "America/Sao_Paulo"
# Pré-teste = respostas enviadas até o fim do prazo da Parte 1 (13/11/2026 23:59, horário de Brasília).
CORTE_PRETESTE = pd.Timestamp("2026-11-13 23:59:59", tz=FUSO)
ALFA = 0.05
N_BOOT = 5000
SEED = 2026
META_VALIDAS = 50

CODIGOS = ["ACE", "CUR", "SIT", "ATU", "MOM", "IAF", "IAU", "CON1", "CON2", "CON3",
           "PRA1", "PRA2", "PRA3", "PRA4", "ATN1", "CONF", "AVG", "ABR"]
CON = ["CON1", "CON2", "CON3"]
PRA = ["PRA1", "PRA2", "PRA3", "PRA4"]

LIKERT = {"Discordo totalmente": 1, "Discordo": 2, "Nem concordo nem discordo": 3,
          "Concordo": 4, "Concordo totalmente": 5}
LIKERT_ROT = {v: k for k, v in LIKERT.items()}
IAF_MAP = {"Nunca": 1, "Raramente": 2, "Às vezes": 3, "Frequentemente": 4, "Sempre": 5}
CONF_MAP = {"Nada confiante": 1, "Pouco confiante": 2, "Razoavelmente confiante": 3,
            "Confiante": 4, "Muito confiante": 5}
AVG_MAP = {"Piorou muito": 1, "Piorou um pouco": 2, "Não mudou": 3,
           "Melhorou um pouco": 4, "Melhorou muito": 5}
CUR_MAP = {"Ciência da Computação": "CC", "Engenharia de Software": "ES",
           "Análise e Desenvolvimento de Sistemas (ADS)": "ADS", "Sistemas de Informação": "SI",
           "Outro curso de tecnologia": "OUTRO", "Não cursei curso de tecnologia": "NENHUM"}
SIT_MAP = {"Estudante, do 1º ao 4º período": "EST14", "Estudante, do 5º período em diante": "EST5",
           "Formado(a) há até 3 anos": "FORM3", "Formado(a) há mais de 3 anos": "FORM3MAIS"}
IAU_MAP = {"Obter código pronto para a tarefa": "CODIGO",
           "Entender conceitos ou mensagens de erro": "ENTENDER",
           "Revisar ou melhorar o meu próprio código": "REVISAR",
           "Gerar exemplos ou exercícios para praticar": "PRATICAR",
           "Não uso IA para estudar programação": "NAOUSO"}

ROTULOS = {
    "CUR": {"CC": "Ciência da Computação", "ES": "Engenharia de Software", "ADS": "ADS",
            "SI": "Sistemas de Informação", "OUTRO": "Outro curso", "NENHUM": "Nenhum"},
    "SIT": {"EST14": "Estudante 1º–4º", "EST5": "Estudante 5º+", "FORM3": "Formado até 3 anos",
            "FORM3MAIS": "Formado há mais de 3 anos"},
    "ATU": {"SIM": "Atua na área", "NAO": "Não atua"},
    "MOM": {"ANTES": "Antes da IA (até 2022)", "DEPOIS": "Depois da IA (2023+)"},
    "IAU": {"CODIGO": "Código pronto", "ENTENDER": "Entender conceitos/erros",
            "REVISAR": "Revisar o próprio código", "PRATICAR": "Gerar exemplos/exercícios",
            "NAOUSO": "Não uso IA"},
}

ITENS_TEXTO = {
    "CON1": "A IA me ajuda a entender conceitos de programação.",
    "CON2": "Com a IA, entendo mais rápido por que um código funciona ou falha.",
    "CON3": "A IA me ajuda a compreender mensagens de erro e documentação.",
    "PRA1": "Escrevo eu mesmo(a) a maior parte do código das minhas atividades.",
    "PRA2": "Consigo escrever do zero, sem IA, um código parecido com o que ela me ajudou a fazer.",
    "PRA3": "Com frequência, pratico escrevendo código sem nenhuma ajuda de IA.",
    "PRA4": "Desde que passei a usar IA, escrevo menos código por conta própria. (invertido)",
}

MOTIVOS = {
    "E0": "Pré-teste (enviada até 13/11/2026 23:59)",
    "E1": "Não cursou curso de tecnologia",
    "E2": "Falhou na pergunta de atenção (ATN1)",
    "E3": "PRA1–PRA4 todos em 1 ou todos em 5 (contradiz o item invertido)",
    "E4": "Duração menor que 1/3 da mediana",
    "E5": "Duplicata técnica (idêntica, < 5 min de diferença)",
}


# --------------------------------------------------------------------------- leitura
# Palavras-chave para reconhecer as colunas da exportação .xlsx do Forms (títulos das perguntas).
CHAVES_XLSX = {
    "ACE": "li o termo", "CUR": "qual curso", "SIT": "situação atual", "ATU": "atua profissionalmente",
    "MOM": "começou a aprender", "IAF": "com que frequência", "IAU": "principal finalidade",
    "CON1": "entender conceitos de programação", "CON2": "entendo mais rápido",
    "CON3": "mensagens de erro e documentação", "PRA1": "maior parte do código",
    "PRA2": "consigo escrever do zero", "PRA3": "pratico escrevendo", "PRA4": "escrevo menos código",
    "ATN1": "lendo com atenção", "CONF": "quão confiante", "AVG": "no geral", "ABR": "equilíbrio",
}


def arquivo_bruto_mais_recente() -> Path | None:
    if not DIR_BRUTOS.exists():
        return None
    arqs = sorted([*DIR_BRUTOS.glob("*.csv"), *DIR_BRUTOS.glob("*.xlsx")], key=lambda p: p.stat().st_mtime)
    return arqs[-1] if arqs else None


def ler_bruto(caminho: Path | None = None) -> tuple[pd.DataFrame, str]:
    """Devolve (dataframe com colunas id, inicio, envio e CODIGOS em texto original, origem)."""
    caminho = caminho or arquivo_bruto_mais_recente()
    if caminho is None:
        df = pd.read_csv(ARQ_ANONIMIZADO, dtype=str, keep_default_na=False)
        df["inicio"] = pd.to_datetime(df["envio_local"]).dt.tz_localize(FUSO) - pd.to_timedelta(df["duracao_s"].astype(float), unit="s")
        df["envio"] = pd.to_datetime(df["envio_local"]).dt.tz_localize(FUSO)
        return df, f"{ARQ_ANONIMIZADO.relative_to(RAIZ)} (conjunto anonimizado)"
    if caminho.suffix == ".xlsx":
        raw = pd.read_excel(caminho, dtype=str).fillna("")
        cols = {}
        for c in raw.columns:
            lc = str(c).lower()
            if lc in ("id",):
                cols[c] = "id"
            elif lc.startswith("start time") or lc.startswith("hora de início"):
                cols[c] = "inicio_utc"
            elif lc.startswith("completion time") or lc.startswith("hora de conclusão"):
                cols[c] = "envio_utc"
            else:
                for cod, chave in CHAVES_XLSX.items():
                    if chave in lc and cod not in cols.values():
                        cols[c] = cod
                        break
        df = raw.rename(columns=cols)
        # O Excel do Forms traz horário local sem fuso.
        df["inicio"] = pd.to_datetime(df["inicio_utc"]).dt.tz_localize(FUSO)
        df["envio"] = pd.to_datetime(df["envio_utc"]).dt.tz_localize(FUSO)
    else:
        df = pd.read_csv(caminho, dtype=str, keep_default_na=False)
        df["inicio"] = pd.to_datetime(df["inicio_utc"], utc=True, format="ISO8601").dt.tz_convert(FUSO)
        df["envio"] = pd.to_datetime(df["envio_utc"], utc=True, format="ISO8601").dt.tz_convert(FUSO)
    faltando = [c for c in CODIGOS if c not in df.columns]
    if faltando:
        raise ValueError(f"Colunas não reconhecidas na exportação: {faltando}")
    df["id"] = df["id"].astype(int)
    return df[["id", "inicio", "envio", *CODIGOS]].sort_values("id").reset_index(drop=True), str(caminho.relative_to(RAIZ))


# --------------------------------------------------------------------------- codificação
def codificar(df: pd.DataFrame) -> pd.DataFrame:
    d = df.copy()
    d["duracao_s"] = (d["envio"] - d["inicio"]).dt.total_seconds()
    d["CUR_c"] = d["CUR"].map(CUR_MAP)
    d["SIT_c"] = d["SIT"].map(SIT_MAP)
    d["ATU_c"] = d["ATU"].map(lambda s: "SIM" if s.startswith("Sim") else "NAO")
    d["MOM_c"] = d["MOM"].map(lambda s: "ANTES" if s.startswith("Antes") else "DEPOIS")
    d["IAU_c"] = d["IAU"].map(IAU_MAP)
    d["IAF_n"] = d["IAF"].map(IAF_MAP)
    d["CONF_n"] = d["CONF"].map(CONF_MAP)
    d["AVG_n"] = d["AVG"].map(AVG_MAP)  # "Não uso IA" -> NaN
    for c in CON + PRA + ["ATN1"]:
        d[c + "_n"] = d[c].map(LIKERT)  # "Não uso IA" -> NaN
    d["PRA4_inv"] = 6 - d["PRA4_n"]
    d["M3_CON"] = d[[c + "_n" for c in CON]].mean(axis=1, skipna=False)
    d["M4_PRA"] = d[["PRA1_n", "PRA2_n", "PRA3_n", "PRA4_inv"]].mean(axis=1, skipna=False)
    d["USA_IA"] = (d["IAF_n"] != 1) & (d["IAU_c"] != "NAOUSO")
    d["SIT_2"] = d["SIT_c"].map(lambda s: "Estudante" if str(s).startswith("EST") else "Formado")
    d["IAU_2"] = d["IAU_c"].map(lambda s: "Código pronto" if s == "CODIGO" else "Demais finalidades")
    return d


def limpar(d: pd.DataFrame) -> pd.DataFrame:
    """Aplica E0–E5 na ordem do protocolo; cada registro recebe o primeiro motivo que se aplica."""
    d = d.copy()
    d["motivo"] = ""
    vazio = lambda: d["motivo"] == ""
    d.loc[vazio() & (d["envio"] <= CORTE_PRETESTE), "motivo"] = "E0"
    d.loc[vazio() & (d["CUR_c"] == "NENHUM"), "motivo"] = "E1"
    d.loc[vazio() & (d["ATN1_n"] != 1), "motivo"] = "E2"
    pra_brutos = d[[c + "_n" for c in PRA]]
    linha_reta = pra_brutos.eq(1).all(axis=1) | pra_brutos.eq(5).all(axis=1)
    d.loc[vazio() & linha_reta, "motivo"] = "E3"
    mediana = d.loc[d["motivo"] != "E0", "duracao_s"].median()
    d.attrs["mediana_duracao_s"] = float(mediana)
    d.loc[vazio() & (d["duracao_s"] < mediana / 3), "motivo"] = "E4"
    fechadas = [c for c in CODIGOS]
    d = d.sort_values("envio")
    for i, r in d[vazio()].iterrows():
        anteriores = d[(d["envio"] < r["envio"]) & (d["envio"] >= r["envio"] - pd.Timedelta(minutes=5)) & (d.index != i)]
        if any((a[fechadas] == r[fechadas]).all() for _, a in anteriores.iterrows()):
            d.loc[i, "motivo"] = "E5"
    d = d.sort_values("id")
    d["valida"] = d["motivo"] == ""
    return d


# --------------------------------------------------------------------------- estatística
def margem_erro(n: int, p: float = 0.5) -> float:
    return 1.96 * math.sqrt(p * (1 - p) / n) if n else float("nan")


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    den = 1 + z ** 2 / n
    c = (p + z ** 2 / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z ** 2 / (4 * n ** 2)) / den
    return (c - h, c + h)


def cronbach(itens: pd.DataFrame) -> float:
    x = itens.dropna()
    k = x.shape[1]
    var_tot = x.sum(axis=1).var(ddof=1)
    if k < 2 or var_tot == 0:
        return float("nan")
    return k / (k - 1) * (1 - x.var(ddof=1).sum() / var_tot)


def cliff_delta(a, b) -> float:
    a, b = np.asarray(a, float), np.asarray(b, float)
    if len(a) == 0 or len(b) == 0:
        return float("nan")
    gt = (a[:, None] > b[None, :]).sum()
    lt = (a[:, None] < b[None, :]).sum()
    return (gt - lt) / (len(a) * len(b))


def cramer_v(tab: np.ndarray) -> float:
    chi2 = stats.chi2_contingency(tab, correction=False)[0]
    n = tab.sum()
    r, k = tab.shape
    return math.sqrt(chi2 / (n * (min(r, k) - 1)))


def wilcoxon_r(x, y) -> tuple[float, float, float]:
    """Wilcoxon pareado; devolve (W, p, r = Z/√n), com n = pares não empatados."""
    x, y = np.asarray(x, float), np.asarray(y, float)
    dif = x - y
    nz = dif[dif != 0]
    res = stats.wilcoxon(x, y, zero_method="wilcox", method="approx", correction=False)
    z = abs(stats.norm.ppf(res.pvalue / 2))
    r = math.copysign(z / math.sqrt(len(nz)), np.median(dif)) if len(nz) else float("nan")
    return float(res.statistic), float(res.pvalue), r


def bootstrap_ic(df: pd.DataFrame, fn, n_boot: int = N_BOOT, seed: int = SEED) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    n = len(df)
    vals = []
    arr = df.reset_index(drop=True)
    for _ in range(n_boot):
        idx = rng.integers(0, n, n)
        try:
            v = fn(arr.iloc[idx])
        except Exception:
            continue
        if v is not None and np.isfinite(v):
            vals.append(v)
    if len(vals) < n_boot * 0.5:
        return (float("nan"), float("nan"))
    return (float(np.percentile(vals, 2.5)), float(np.percentile(vals, 97.5)))


def holm(pvals: dict[str, float]) -> dict[str, float]:
    itens = sorted(pvals.items(), key=lambda kv: kv[1])
    m = len(itens)
    ajust, maxacum = {}, 0.0
    for i, (k, p) in enumerate(itens):
        maxacum = max(maxacum, min(1.0, (m - i) * p))
        ajust[k] = maxacum
    return ajust


def magnitude(valor: float, limites: tuple[float, float, float]) -> str:
    if valor is None or not np.isfinite(valor):
        return "—"
    a = abs(valor)
    p, m, g = limites
    return "desprezível" if a < p else "pequeno" if a < m else "médio" if a < g else "grande"


LIM = {"r": (0.1, 0.3, 0.5), "rho": (0.1, 0.3, 0.5), "eps2": (0.01, 0.08, 0.26),
       "delta": (0.147, 0.33, 0.474), "V": (0.1, 0.3, 0.5)}


@dataclass
class Hipotese:
    id: str
    base: str
    qp: str
    descricao: str
    direcao_esperada: str
    teste: str
    n: int
    variavel: str = ""
    familia: str = "confirmatória"  # confirmatória | referência
    estatistica: str = ""
    p: float | None = None
    p_holm: float | None = None
    p_holm_plano_original: float | None = None  # Holm na família de 7 testes com M4 como escore (sensibilidade)
    efeito_nome: str = ""
    efeito: float | None = None
    efeito_ic: tuple[float, float] | None = None
    magnitude: str = ""
    margem_erro_pp: float | None = None
    status: str = "testada"  # testada | descritiva
    regra_condicional: str = ""
    decisao: str = ""
    direcao_observada: str = ""
    leitura: str = ""
    grupos: dict = field(default_factory=dict)


def resumo_grupo(s: pd.Series) -> dict:
    s = s.dropna()
    return {"n": int(len(s)), "mediana": float(s.median()) if len(s) else None,
            "q1": float(s.quantile(.25)) if len(s) else None, "q3": float(s.quantile(.75)) if len(s) else None}


def _me(n: int) -> float:
    return round(100 * margem_erro(n), 1)


# Variáveis de prática de escrita: rótulo -> coluna (PRA4 já invertido: maior = mais prática)
PRA_ITENS = {"PRA1": "PRA1_n", "PRA2": "PRA2_n", "PRA3": "PRA3_n", "PRA4ᴿ": "PRA4_inv"}
M4 = {"M4": "M4_PRA"}


def _h2a(u, rot, col, fam, n_boot):
    x = u[["M3_CON", col]].dropna()
    W, p, r = wilcoxon_r(x["M3_CON"], x[col])
    ic = bootstrap_ic(x, lambda b: wilcoxon_r(b["M3_CON"], b[col])[2], n_boot)
    return Hipotese(f"H2a·{rot}" if rot != "M4" else "H2a", "H2a", "QP2",
                    f"Conceitos (M3) difere da prática de escrita ({rot})", "conceitos maior",
                    "Wilcoxon pareado", len(x), rot, fam, f"W = {W:.1f}", p, efeito_nome="r", efeito=r, efeito_ic=ic,
                    magnitude=magnitude(r, LIM["r"]), margem_erro_pp=_me(len(x)),
                    direcao_observada="conceitos maior" if r > 0 else "prática maior",
                    grupos={"Conceitos (M3)": resumo_grupo(x["M3_CON"]), rot: resumo_grupo(x[col])})


def _spearman(u, hid, base, qp, a, b, rot, desc, dire, fam, n_boot):
    x = u[[a, b]].dropna()
    rho, p = stats.spearmanr(x[a], x[b])
    ic = bootstrap_ic(x, lambda bb: stats.spearmanr(bb[a], bb[b])[0], n_boot)
    return Hipotese(hid, base, qp, desc, dire, "Correlação de Spearman", len(x), rot, fam, f"ρ = {rho:.3f}", float(p),
                    efeito_nome="ρ", efeito=float(rho), efeito_ic=ic, magnitude=magnitude(rho, LIM["rho"]),
                    margem_erro_pp=_me(len(x)), direcao_observada="positiva" if rho > 0 else "negativa")


def _h3a(u, rot, col, fam, n_boot):
    x = u[[col, "IAU_c"]].dropna()
    cont = x["IAU_c"].value_counts()
    detalhe = {"(detalhe) " + ROTULOS["IAU"][g]: resumo_grupo(x.loc[x["IAU_c"] == g, col]) for g in cont.index}
    hid = f"H3a·{rot}" if rot != "M4" else "H3a"
    desc = f"Prática de escrita ({rot}) difere entre finalidades de uso (M2)"
    if (cont < 5).any():
        a = x.loc[x["IAU_c"] == "CODIGO", col]; b = x.loc[x["IAU_c"] != "CODIGO", col]
        U, p = stats.mannwhitneyu(a, b, alternative="two-sided")
        dlt = cliff_delta(a, b)
        ic = bootstrap_ic(x, lambda bb: cliff_delta(bb.loc[bb["IAU_c"] == "CODIGO", col], bb.loc[bb["IAU_c"] != "CODIGO", col]), n_boot)
        pequenos = ", ".join(f"{ROTULOS['IAU'][k]} = {v}" for k, v in cont.items() if v < 5)
        return Hipotese(hid, "H3a", "QP3", desc, "menor em quem busca código pronto",
                        "Mann-Whitney (código pronto × demais)", len(x), rot, fam, f"U = {U:.1f}", float(p),
                        efeito_nome="δ de Cliff", efeito=dlt, efeito_ic=ic, magnitude=magnitude(dlt, LIM["delta"]),
                        margem_erro_pp=_me(len(x)), direcao_observada="menor em código pronto" if dlt < 0 else "maior em código pronto",
                        regra_condicional=f"Regra (i): finalidade com n < 5 ({pequenos}); IAU agrupada em código pronto × demais.",
                        grupos={"Código pronto": resumo_grupo(a), "Demais finalidades": resumo_grupo(b), **detalhe})
    H, p = stats.kruskal(*[x.loc[x["IAU_c"] == g, col] for g in cont.index])
    eps = H / (len(x) - 1)
    return Hipotese(hid, "H3a", "QP3", desc, "menor em quem busca código pronto", "Kruskal-Wallis", len(x), rot, fam,
                    f"H = {H:.2f}", float(p), efeito_nome="ε²", efeito=eps, magnitude=magnitude(eps, LIM["eps2"]),
                    margem_erro_pp=_me(len(x)), grupos=detalhe)


def _grupo2(u, base, rot, col, var, g1, g2, desc, dire, fam, n_boot):
    x = u[[col, var]].dropna()
    a = x.loc[x[var] == g1, col]; b = x.loc[x[var] == g2, col]
    r = ROTULOS[var[:3]]
    dlt = cliff_delta(a, b)
    h = Hipotese(f"{base}·{rot}" if rot != "M4" else base, base, "QP4", desc.format(rot=rot), dire, "Mann-Whitney",
                 len(x), rot, fam, efeito_nome="δ de Cliff", efeito=dlt, magnitude=magnitude(dlt, LIM["delta"]),
                 margem_erro_pp=_me(len(x)), direcao_observada=("menor" if dlt < 0 else "maior") + f" em «{r[g1]}»",
                 grupos={r[g1]: resumo_grupo(a), r[g2]: resumo_grupo(b)})
    if min(len(a), len(b)) < 10:
        h.status, h.teste = "descritiva", "Descritiva (regra iii)"
        h.regra_condicional = f"Regra (iii): grupo com n < 10 ({r[g1]} = {len(a)}, {r[g2]} = {len(b)}); só descritiva, fora da correção de Holm."
    else:
        U, p = stats.mannwhitneyu(a, b, alternative="two-sided")
        h.estatistica, h.p = f"U = {U:.1f}", float(p)
        h.efeito_ic = bootstrap_ic(x, lambda bb: cliff_delta(bb.loc[bb[var] == g1, col], bb.loc[bb[var] == g2, col]), n_boot)
    return h


def _h4c(u, n_boot):
    x = u[["IAU_2", "SIT_2"]].dropna()
    tab = pd.crosstab(x["IAU_2"], x["SIT_2"])
    if tab.shape != (2, 2):
        return Hipotese("H4c", "H4c", "QP4", "Finalidade de uso (M2) × situação (M7)", "bilateral", "Descritiva", len(x),
                        status="descritiva", regra_condicional="Tabela sem as duas categorias em ambas as variáveis.")
    esperado = stats.contingency.expected_freq(tab.values)
    V = cramer_v(tab.values)
    if (esperado < 5).any():
        _, p = stats.fisher_exact(tab.values)
        teste, est = "Exato de Fisher (2 × 2)", f"esperado mínimo = {esperado.min():.1f}"
    else:
        chi2, p, _, _ = stats.chi2_contingency(tab.values, correction=False)
        teste, est = "χ² (2 × 2)", f"χ² = {chi2:.2f}"
    ic = bootstrap_ic(x, lambda bb: cramer_v(pd.crosstab(bb["IAU_2"], bb["SIT_2"]).reindex(index=tab.index, columns=tab.columns, fill_value=0).values), n_boot)
    prop_est = tab.loc["Código pronto", "Estudante"] / tab["Estudante"].sum()
    prop_form = tab.loc["Código pronto", "Formado"] / tab["Formado"].sum()
    return Hipotese("H4c", "H4c", "QP4", "Finalidade de uso (M2) × situação (M7)", "bilateral", teste, len(x), "", "confirmatória",
                    est, float(p), direcao_observada=f"código pronto: {100*prop_est:.0f}% dos estudantes × {100*prop_form:.0f}% dos formados", efeito_nome="V de Cramér", efeito=V, efeito_ic=ic, magnitude=magnitude(V, LIM["V"]),
                    margem_erro_pp=_me(len(x)),
                    regra_condicional="Regra (ii): SIT agrupada em estudante × formado e IAU em código pronto × demais.",
                    grupos={"tabela": {str(i): {str(c): int(tab.loc[i, c]) for c in tab.columns} for i in tab.index}})


def testar(v: pd.DataFrame, n_boot: int = N_BOOT) -> list[Hipotese]:
    """Hipóteses confirmatórias sobre os usuários de IA válidos.

    Se o α de Cronbach de PRA for < 0,60, a regra do protocolo (§5) manda analisar
    os itens de PRA separadamente: cada hipótese que usa M4 vira uma hipótese por
    item, todas na mesma família de Holm. O escore M4 é relatado como referência,
    fora da família.
    """
    u = v[v["USA_IA"]].copy()
    alfa_pra = cronbach(u[["PRA1_n", "PRA2_n", "PRA3_n", "PRA4_inv"]])
    separar = bool(np.isfinite(alfa_pra) and alfa_pra < 0.60)
    conjuntos = [(PRA_ITENS, "confirmatória"), (M4, "referência")] if separar else [(M4, "confirmatória")]
    hs: list[Hipotese] = []
    for itens, fam in conjuntos:
        for rot, col in itens.items():
            hs.append(_h2a(u, rot, col, fam, n_boot))
    hs.append(_spearman(u, "H2b", "H2b", "QP2", "IAF_n", "M3_CON", "", "Frequência de uso (M1) × conceitos (M3)", "positiva", "confirmatória", n_boot))
    for itens, fam in conjuntos:
        for rot, col in itens.items():
            hs.append(_spearman(u, f"H2c·{rot}" if rot != "M4" else "H2c", "H2c", "QP2", "IAF_n", col, rot,
                                f"Frequência de uso (M1) × prática de escrita ({rot})", "negativa", fam, n_boot))
    for itens, fam in conjuntos:
        for rot, col in itens.items():
            hs.append(_h3a(u, rot, col, fam, n_boot))
    for itens, fam in conjuntos:
        for rot, col in itens.items():
            hs.append(_spearman(u, f"H3b·{rot}" if rot != "M4" else "H3b", "H3b", "QP3", col, "CONF_n", rot,
                                f"Prática de escrita ({rot}) × confiança sem IA (M5)", "positiva", fam, n_boot))
    for itens, fam in conjuntos:
        for rot, col in itens.items():
            hs.append(_grupo2(u, "H4a", rot, col, "MOM_c", "DEPOIS", "ANTES",
                              "Prática de escrita ({rot}): começou depois × antes da IA", "menor depois", fam, n_boot))
    for itens, fam in conjuntos:
        for rot, col in itens.items():
            hs.append(_grupo2(u, "H4b", rot, col, "ATU_c", "SIM", "NAO",
                              "Prática de escrita ({rot}): atua × não atua na área", "bilateral", fam, n_boot))
    hs.append(_h4c(u, n_boot))

    pv = {h.id: h.p for h in hs if h.familia == "confirmatória" and h.status == "testada" and h.p is not None}
    aj = holm(pv)
    # Sensibilidade: família original do protocolo (M4 como escore + H2b + H4c), só para leitura
    original = [h for h in hs if h.status == "testada" and h.p is not None and
                (h.variavel in ("M4", "") if separar else h.familia == "confirmatória")]
    aj_orig = holm({h.id: h.p for h in original})
    for h in hs:
        h.p_holm = aj.get(h.id, aj_orig.get(h.id) if h.familia == "referência" else None)
        h.p_holm_plano_original = aj_orig.get(h.id)
        if h.status == "descritiva":
            h.decisao = "Sem teste (descritiva)"
        elif h.familia == "referência":
            h.decisao = "Referência (α de PRA insuficiente)"
        else:
            h.decisao = "Rejeita H0" if h.p_holm < ALFA else "Não rejeita H0"
        h.leitura = leitura(h)
    return hs


def leitura(h: Hipotese) -> str:
    if h.status == "descritiva":
        return "Grupo pequeno demais para teste confirmatório; ver medianas por grupo."
    conf = "" if not h.direcao_esperada or h.direcao_esperada == "bilateral" else (
        " Direção igual à esperada." if h.direcao_observada == h.direcao_esperada or
        (h.direcao_esperada.startswith("menor") and h.direcao_observada.startswith("menor")) or
        (h.direcao_esperada == "menor em quem busca código pronto" and h.direcao_observada == "menor em código pronto") else " Direção oposta à esperada.")
    if h.p_holm is not None and h.p_holm < ALFA:
        return f"Diferença/associação significativa após Holm, efeito {h.magnitude} ({h.direcao_observada}).{conf}"
    return f"Sem evidência após Holm (efeito {h.magnitude}, {h.direcao_observada}).{conf} Com n = {h.n}, só efeitos grandes eram detectáveis."


def descritivas(v: pd.DataFrame) -> dict:
    n = len(v)
    out = {"n": n, "margem_erro_pp": round(100 * margem_erro(n), 1)}
    def freq(col, ordem=None):
        c = v[col].value_counts()
        ordem = ordem or list(c.index)
        res = []
        for k in ordem:
            kk = int(c.get(k, 0))
            lo, hi = wilson(kk, n)
            res.append({"categoria": k, "n": kk, "pct": round(100 * kk / n, 1) if n else 0,
                        "ic95": [round(100 * lo, 1), round(100 * hi, 1)], "margem_pp": round(100 * margem_erro(n, kk / n), 1) if n else None})
        return res
    out["IAF"] = freq("IAF", list(IAF_MAP))
    out["IAU"] = freq("IAU_c", list(IAU_MAP.values()))
    out["AVG"] = freq("AVG", list(AVG_MAP) + ["Não uso IA"])
    out["CONF"] = freq("CONF", list(CONF_MAP))
    melhorou = int(v["AVG_n"].ge(4).sum())
    lo, hi = wilson(melhorou, n)
    out["pct_melhorou"] = {"n": melhorou, "pct": round(100 * melhorou / n, 1), "ic95": [round(100 * lo, 1), round(100 * hi, 1)],
                           "margem_pp": round(100 * margem_erro(n, melhorou / n), 1)}
    return out


def confiabilidade(u: pd.DataFrame) -> dict:
    res = {}
    for nome, cols in [("CON", [c + "_n" for c in CON]), ("PRA", ["PRA1_n", "PRA2_n", "PRA3_n", "PRA4_inv"])]:
        a = cronbach(u[cols])
        sem = {c.replace("_n", "").replace("_inv", "ᴿ"): cronbach(u[[k for k in cols if k != c]]) for c in cols}
        ic = bootstrap_ic(u[cols].dropna(), lambda b: cronbach(b))
        res[nome] = {"alfa": a, "ic95": ic, "n": int(u[cols].dropna().shape[0]), "k": len(cols), "alfa_sem_item": sem,
                     "avaliacao": "aceitável (≥ 0,70)" if a >= 0.70 else "questionável (0,60–0,70)" if a >= 0.60 else "insuficiente (< 0,60): itens analisados separadamente"}
    return res


def carregar_tudo(caminho: Path | None = None) -> dict:
    bruto, origem = ler_bruto(caminho)
    d = limpar(codificar(bruto))
    v = d[d["valida"]]
    u = v[v["USA_IA"]]
    return {"bruto": bruto, "d": d, "validas": v, "usuarios": u, "origem": origem}


def gerar_json(caminho_saida: Path = RAIZ / "resultados" / "resultados.json") -> dict:
    t = carregar_tudo()
    d, v, u = t["d"], t["validas"], t["usuarios"]
    hs = testar(v)
    oficiais = d[d["motivo"] != "E0"]
    out = {
        "origem": t["origem"],
        "gerado_em": pd.Timestamp.now(tz=FUSO).isoformat(timespec="seconds"),
        "recebidas": int(len(d)),
        "preteste": int((d["motivo"] == "E0").sum()),
        "coleta_oficial": int(len(oficiais)),
        "descartes": {k: int((d["motivo"] == k).sum()) for k in MOTIVOS},
        "ids_descartados": {k: d.loc[d["motivo"] == k, "id"].tolist() for k in MOTIVOS},
        "validas": int(len(v)),
        "usuarios_ia": int(len(u)),
        "meta": META_VALIDAS,
        "mediana_duracao_s": d.attrs.get("mediana_duracao_s"),
        "primeira_oficial": oficiais["envio"].min().isoformat() if len(oficiais) else None,
        "ultima_oficial": oficiais["envio"].max().isoformat() if len(oficiais) else None,
        "descritivas": descritivas(v),
        "confiabilidade": confiabilidade(u),
        "hipoteses": [asdict(h) for h in hs],
    }
    caminho_saida.parent.mkdir(exist_ok=True)
    caminho_saida.write_text(json.dumps(out, ensure_ascii=False, indent=2, default=float), encoding="utf-8")
    return out


def exportar_anonimizado() -> None:
    """Conjunto público: sem horário de início exato (só envio arredondado ao minuto e duração)."""
    bruto, _ = ler_bruto()
    d = limpar(codificar(bruto))
    pub = bruto.copy()
    pub["envio_local"] = d["envio"].dt.tz_localize(None).dt.floor("min").astype(str)
    pub["duracao_s"] = d["duracao_s"].round(0).astype(int)
    pub = pub[["id", "envio_local", "duracao_s", *CODIGOS]]
    pub.to_csv(ARQ_ANONIMIZADO, index=False, encoding="utf-8")


def embutir_no_dashboard(saida: Path) -> None:
    """Grava uma cópia de dashboard/dashboard.html com a exportação bruta mais recente embutida."""
    import csv
    import io
    import re
    bruto, origem = ler_bruto()
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["id", "inicio_utc", "envio_utc", *CODIGOS])
    for _, r in bruto.iterrows():
        utc = lambda t: t.tz_convert("UTC").strftime("%Y-%m-%dT%H:%M:%S.%f") + "Z"
        w.writerow([r["id"], utc(r["inicio"]), utc(r["envio"]), *[r[c] for c in CODIGOS]])
    txt = buf.getvalue().strip()
    html = (RAIZ / "dashboard" / "dashboard.html").read_text(encoding="utf-8")
    fonte = f"exportação bruta do Microsoft Forms ({Path(origem).name})"
    html, n = re.subn(r'(<script id="dados" type="text/plain" data-fonte=")[^"]*(">\n).*?(</script>)',
                      lambda m: m.group(1) + fonte + m.group(2) + txt + m.group(3), html, count=1, flags=re.S)
    if n != 1:
        raise SystemExit("Bloco de dados não encontrado em dashboard/dashboard.html")
    Path(saida).write_text(html, encoding="utf-8")


if __name__ == "__main__":
    if "--anonimizar" in sys.argv:
        exportar_anonimizado()
        print("Conjunto anonimizado gravado em", ARQ_ANONIMIZADO.relative_to(RAIZ))
    if "--dashboard" in sys.argv:
        destino = Path(sys.argv[sys.argv.index("--dashboard") + 1]).expanduser()
        embutir_no_dashboard(destino)
        print("Dashboard com os dados brutos gravado em", destino)
        sys.exit(0)
    r = gerar_json()
    print(f"Origem: {r['origem']}")
    print(f"Recebidas: {r['recebidas']} | pré-teste: {r['preteste']} | coleta oficial: {r['coleta_oficial']}")
    print("Descartes:", {k: v for k, v in r["descartes"].items() if v}, r["ids_descartados"])
    print(f"Válidas: {r['validas']} (meta {r['meta']}) | usuários de IA: {r['usuarios_ia']} | mediana duração: {r['mediana_duracao_s']:.0f} s")
    for k, c in r["confiabilidade"].items():
        print(f"α {k} = {c['alfa']:.3f} IC95 {c['ic95'][0]:.2f}–{c['ic95'][1]:.2f} ({c['avaliacao']}); sem item: { {i: round(a, 3) for i, a in c['alfa_sem_item'].items()} }")
    for h in r["hipoteses"]:
        ic = h["efeito_ic"]
        ics = f" IC95 [{ic[0]:.2f}; {ic[1]:.2f}]" if ic and ic[0] == ic[0] else ""
        p = f"p = {h['p']:.4f}" if h["p"] is not None else "p = —"
        ph = f"p Holm = {h['p_holm']:.4f}" if h["p_holm"] is not None else ""
        ef = f"{h['efeito']:.3f}" if h['efeito'] is not None else "—"
        print(f"{h['id']:<11} [{h['familia'][:4]}] {h['teste']} n={h['n']} {h['estatistica']} {p} {ph} {h['efeito_nome']}={ef}{ics} ({h['magnitude']}) -> {h['decisao']}")
        if h["regra_condicional"]:
            print("   ", h["regra_condicional"])
        print("   ", h["leitura"])
