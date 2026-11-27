"""Gera os números, quadros e figuras do relatório de resultados (PDF, ABNT).

Tudo sai da exportação bruta, pelo mesmo pipeline do dashboard. Depois de rodar,
compile `resultados/relatorio/relatorio.tex` com `tectonic`.

    .venv/bin/python analise/relatorio.py && (cd resultados/relatorio && tectonic relatorio.tex)
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
import survey as sv  # noqa: E402

SAIDA = sv.RAIZ / "resultados" / "relatorio"
GER = SAIDA / "gerado"


def br(x, nd=2):
    if x is None or (isinstance(x, float) and not np.isfinite(x)):
        return "---"
    s = f"{x:.{nd}f}".replace(".", ",")
    if s.startswith("-") and s.strip("-0,") == "":
        s = s[1:]  # evita "-0,00"
    return s.replace("-", "$-$") if s.startswith("-") else s


def p_tex(p):
    return "---" if p is None else ("$<$\\,0,001" if p < 0.001 else br(p, 3))


def esc(s: str) -> str:
    return (s.replace("&", "\\&").replace("%", "\\%").replace("_", "\\_").replace("ᴿ", "\\textsuperscript{R}")
            .replace("ρ", "$\\rho$").replace("δ", "$\\delta$").replace("ε²", "$\\varepsilon^2$").replace("χ²", "$\\chi^2$")
            .replace("×", "$\\times$").replace("≥", "$\\geq$").replace("<", "$<$"))


def main():
    GER.mkdir(parents=True, exist_ok=True)
    t = sv.carregar_tudo()
    d, v, u = t["d"], t["validas"], t["usuarios"]
    hs = sv.testar(v)
    conf = sv.confiabilidade(u)
    desc = sv.descritivas(v)
    oficiais = d[d["motivo"] != "E0"]
    H = {h.id: h for h in hs}

    # ------------------------------------------------------------ macros com os números
    m = {
        "nRecebidas": len(d), "nPreteste": int((d["motivo"] == "E0").sum()), "nOficial": len(oficiais),
        "nDescartes": int(((d["motivo"] != "") & (d["motivo"] != "E0")).sum()), "nValidas": len(v), "nUsuarios": len(u),
        "margem": br(100 * sv.margem_erro(len(v)), 1), "margemU": br(100 * sv.margem_erro(len(u)), 1),
        "medianaDur": f"{d.attrs['mediana_duracao_s']:.0f}", "limiteDur": f"{d.attrs['mediana_duracao_s'] / 3:.0f}",
        "minDur": f"{oficiais['duracao_s'].min():.0f}",
        "primeira": oficiais["envio"].min().strftime("%d/%m/%Y"), "ultima": oficiais["envio"].max().strftime("%d/%m/%Y"),
        "alfaCON": br(conf["CON"]["alfa"]), "alfaCONlo": br(conf["CON"]["ic95"][0]), "alfaCONhi": br(conf["CON"]["ic95"][1]),
        "alfaPRA": br(conf["PRA"]["alfa"]), "alfaPRAlo": br(conf["PRA"]["ic95"][0]), "alfaPRAhi": br(conf["PRA"]["ic95"][1]),
        "nTestes": sum(1 for h in hs if h.familia == "confirmatória" and h.status == "testada"),
        "pctMelhorou": br(desc["pct_melhorou"]["pct"], 1), "melhorouLo": br(desc["pct_melhorou"]["ic95"][0], 1),
        "melhorouHi": br(desc["pct_melhorou"]["ic95"][1], 1), "melhorouMargem": br(desc["pct_melhorou"]["margem_pp"], 1),
        "pctPiorou": br(100 * v["AVG_n"].le(2).mean(), 1),
        "pctUsoAlto": br(sum(x["pct"] for x in desc["IAF"] if x["categoria"] in ("Sempre", "Frequentemente")), 1),
        "medianaMtres": br(u["M3_CON"].median()),
        "pctPRAquatro": f"{100 * u['PRA4_n'].ge(4).mean():.0f}", "pctPRAquatroTot": f"{100 * u['PRA4_n'].eq(5).mean():.0f}",
        "pctCONum": f"{100 * u['CON1_n'].ge(4).mean():.0f}",
        "nABR": int((v["ABR"].str.strip() != "").sum()),
        "rhoHdoisB": br(H["H2b"].efeito), "pHdoisB": p_tex(H["H2b"].p), "pHolmHdoisB": p_tex(H["H2b"].p_holm),
        "pOrigHdoisB": p_tex(H["H2b"].p_holm_plano_original),
        "rhoPRAdoisCONF": br(H["H3b·PRA2"].efeito), "rhoPRAdoisCONFlo": br(H["H3b·PRA2"].efeito_ic[0]),
        "rhoPRAdoisCONFhi": br(H["H3b·PRA2"].efeito_ic[1]), "pHolmPRAdoisCONF": p_tex(H["H3b·PRA2"].p_holm),
        "deltaHquatroA": br(H["H4a·PRA2"].efeito), "deltaHquatroAlo": br(H["H4a·PRA2"].efeito_ic[0]),
        "deltaHquatroAhi": br(H["H4a·PRA2"].efeito_ic[1]), "pHquatroA": p_tex(H["H4a·PRA2"].p),
        "pHolmHquatroA": p_tex(H["H4a·PRA2"].p_holm),
        "dataExport": __import__("datetime").datetime.fromtimestamp(sv.arquivo_bruto_mais_recente().stat().st_mtime).strftime("%d/%m/%Y")
        if sv.arquivo_bruto_mais_recente() else oficiais["envio"].max().strftime("%d/%m/%Y"),
        "nDepois": int((u["MOM_c"] == "DEPOIS").sum()), "nNaoAtua": int((u["ATU_c"] == "NAO").sum()),
        "nGerar": int((u["IAU_c"] == "PRATICAR").sum()), "nCodigo": int((u["IAU_c"] == "CODIGO").sum()),
    }
    rmin = min(H[f"H2a·{k}"].efeito for k in sv.PRA_ITENS); rmax = max(H[f"H2a·{k}"].efeito for k in sv.PRA_ITENS)
    m["rMinHdoisA"], m["rMaxHdoisA"] = br(rmin), br(rmax)
    c = u[["PRA1_n", "PRA2_n", "PRA3_n", "PRA4_inv"]].corr(method="spearman")
    outros = [c.loc["PRA2_n", k] for k in ("PRA1_n", "PRA3_n", "PRA4_inv")]
    m["rhoPRAdoisMin"], m["rhoPRAdoisMax"] = br(min(outros)), br(max(outros))
    tab4c = H["H4c"].grupos["tabela"]
    est = tab4c["Código pronto"]["Estudante"] / (tab4c["Código pronto"]["Estudante"] + tab4c["Demais finalidades"]["Estudante"])
    form = tab4c["Código pronto"]["Formado"] / (tab4c["Código pronto"]["Formado"] + tab4c["Demais finalidades"]["Formado"])
    m["pctCodEst"], m["pctCodForm"] = f"{100 * est:.0f}", f"{100 * form:.0f}"
    (GER / "numeros.tex").write_text("\n".join(f"\\newcommand{{\\{k}}}{{{val}}}" for k, val in m.items()) + "\n", encoding="utf-8")

    # ------------------------------------------------------------ Quadro: limpeza
    linhas = [f"E0 & {esc(sv.MOTIVOS['E0'])} & {m['nPreteste']} & {', '.join(map(str, d.loc[d['motivo'] == 'E0', 'id']))} \\\\"]
    for k in ["E1", "E2", "E3", "E4", "E5"]:
        ids = ", ".join(map(str, d.loc[d["motivo"] == k, "id"])) or "---"
        linhas.append(f"{k} & {esc(sv.MOTIVOS[k])} & {int((d['motivo'] == k).sum())} & {ids} \\\\")
    (GER / "tab_limpeza.tex").write_text("\n".join(linhas) + "\n", encoding="utf-8")

    # ------------------------------------------------------------ Quadro: perfil
    rows = []
    for col, nome in [("CUR_c", "Curso"), ("SIT_c", "Situação"), ("ATU_c", "Atuação"), ("MOM_c", "Começou a aprender")]:
        rot = sv.ROTULOS[col[:3]]
        cnt = v[col].value_counts()
        cats = [k for k in rot if k != "NENHUM"]
        partes = [f"{esc(rot[k])}: {int(cnt.get(k, 0))} ({br(100 * cnt.get(k, 0) / len(v), 0)}\\%)" for k in cats]
        rows.append(f"{nome} & {'; '.join(partes)} \\\\")
    (GER / "tab_perfil.tex").write_text("\n".join(rows) + "\n", encoding="utf-8")

    # ------------------------------------------------------------ Quadro: confiabilidade
    rows = []
    for k, nome in [("CON", "CON (CON1--CON3)"), ("PRA", "PRA (PRA1--PRA3, PRA4\\textsuperscript{R})")]:
        r = conf[k]
        sem = "; ".join(f"{esc(i)}: {br(a)}" for i, a in r["alfa_sem_item"].items())
        aval = "Questionável" if r["alfa"] >= 0.6 and r["alfa"] < 0.7 else ("Aceitável" if r["alfa"] >= 0.7 else "Insuficiente")
        rows.append(f"{nome} & {r['k']} & {br(r['alfa'])} & [{br(r['ic95'][0])}; {br(r['ic95'][1])}] & {sem} & {aval} \\\\")
    (GER / "tab_alfa.tex").write_text("\n".join(rows) + "\n", encoding="utf-8")

    # ------------------------------------------------------------ Quadro: QP1
    rows = []
    for chave, nome, rot in [("IAF", "Frequência de uso (IAF)", None), ("IAU", "Principal finalidade (IAU)", sv.ROTULOS["IAU"]),
                             ("AVG", "Efeito geral (AVG)", None)]:
        for i, x in enumerate(desc[chave]):
            if x["n"] == 0 and x["categoria"] in ("Não uso IA", "Raramente"):
                continue
            cat = rot[x["categoria"]] if rot else x["categoria"]
            rows.append(f"{nome if i == 0 else ''} & {esc(cat)} & {x['n']} & {br(x['pct'], 1)} & [{br(x['ic95'][0], 1)}; {br(x['ic95'][1], 1)}] & $\\pm${br(x['margem_pp'], 1)} \\\\")
        rows.append("\\midrule")
    (GER / "tab_qp1.tex").write_text("\n".join(rows[:-1]) + "\n", encoding="utf-8")

    # ------------------------------------------------------------ Quadro: hipóteses
    def linha(h):
        ic = h.efeito_ic
        ef = f"{esc(h.efeito_nome.replace('δ de Cliff', 'δ'))} = {br(h.efeito)}" if h.efeito is not None else "---"
        if ic and np.isfinite(ic[0]):
            ef += f" [{br(ic[0])}; {br(ic[1])}]"
        dec = {"Rejeita H0": "\\textbf{Rejeita}", "Não rejeita H0": "Não rejeita"}.get(h.decisao, "Descritiva")
        teste = esc(h.teste.replace("Mann-Whitney (código pronto × demais)", "Mann-Whitney\\textsuperscript{(i)}")
                    .replace("Descritiva (regra iii)", "Descritiva\\textsuperscript{(iii)}")
                    .replace("Exato de Fisher (2 × 2)", "Fisher\\textsuperscript{(ii)}").replace("Correlação de Spearman", "Spearman")
                    .replace("Wilcoxon pareado", "Wilcoxon"))
        teste = teste.replace("\\textsuperscript", "\\textsuperscript")
        return f"{esc(h.id).replace('·', '$\\cdot$')} & {teste} & {h.n} & {p_tex(h.p)} & {p_tex(h.p_holm)} & {ef} & {esc(h.magnitude)} & {dec} \\\\"

    rows = []
    qp_atual = None
    for h in [h for h in hs if h.familia == "confirmatória"]:
        if h.qp != qp_atual:
            if qp_atual is not None:
                rows.append("\\midrule")
            rows.append(f"\\multicolumn{{8}}{{@{{}}l}}{{\\textit{{{h.qp}}}}} \\\\")
            qp_atual = h.qp
        rows.append(linha(h))
    (GER / "tab_hipoteses.tex").write_text("\n".join(rows) + "\n", encoding="utf-8")

    # ------------------------------------------------------------ Quadro: sensibilidade
    rows = []
    for h in [h for h in hs if h.p_holm_plano_original is not None]:
        dec = "\\textbf{Rejeita}" if h.p_holm_plano_original < sv.ALFA else "Não rejeita"
        rows.append(f"{esc(h.id)} & {esc(h.efeito_nome)} = {br(h.efeito)} & {p_tex(h.p)} & {p_tex(h.p_holm_plano_original)} & {dec} \\\\")
    (GER / "tab_sensibilidade.tex").write_text("\n".join(rows) + "\n", encoding="utf-8")

    # ------------------------------------------------------------ figuras (preto e branco)
    plt.rcParams.update({"font.family": "serif", "font.serif": ["Times New Roman", "TeX Gyre Termes", "Times", "DejaVu Serif"],
                         "font.size": 9, "axes.edgecolor": "#444444", "axes.linewidth": 0.6, "hatch.linewidth": 0.5})
    estilos = {1: ("#4d4d4d", "////"), 2: ("#bdbdbd", "////"), 3: ("#ffffff", ""), 4: ("#bdbdbd", ""), 5: ("#4d4d4d", "")}
    itens = [("CON1", "CON1_n"), ("CON2", "CON2_n"), ("CON3", "CON3_n"), ("PRA1", "PRA1_n"), ("PRA2", "PRA2_n"),
             ("PRA3", "PRA3_n"), ("PRA4", "PRA4_n")]
    fig, ax = plt.subplots(figsize=(6.3, 2.9))
    for j, (nome, col) in enumerate(itens):
        s = u[col].dropna()
        pct = {k: 100 * (s == k).mean() for k in range(1, 6)}
        esq = -(pct[1] + pct[2] + pct[3] / 2)
        x0 = esq
        for k in range(1, 6):
            cor, hatch = estilos[k]
            ax.barh(j, pct[k], left=x0, color=cor, hatch=hatch, edgecolor="#222222", linewidth=0.5, height=0.62,
                    label=sv.LIKERT_ROT[k] if j == 0 else None)
            if pct[k] >= 9:
                ax.text(x0 + pct[k] / 2, j, f"{pct[k]:.0f}%", ha="center", va="center", fontsize=7.5,
                        color="white" if k in (1, 5) else "black",
                        bbox=dict(boxstyle="square,pad=0.1", fc="white", ec="none", alpha=0.85) if k in (2, 4) else None)
            x0 += pct[k]
    ax.axvline(0, color="#222222", linewidth=0.8)
    ax.set_yticks(range(len(itens)), [f"{n}" + ("*" if n == "PRA4" else "") for n, _ in itens])
    ax.invert_yaxis()
    ax.set_xlim(-100, 100)
    ax.set_xticks([-100, -50, 0, 50, 100], ["100%", "50%", "0", "50%", "100%"])
    ax.axhline(2.5, color="#888888", linewidth=0.5, linestyle="--")
    ax.legend(ncol=5, loc="upper center", bbox_to_anchor=(0.5, -0.12), frameon=False, fontsize=7.5, handlelength=1.6)
    for s_ in ("top", "right"):
        ax.spines[s_].set_visible(False)
    fig.tight_layout()
    fig.savefig(GER / "fig_likert.pdf")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(6.3, 2.6))
    series = [("Conceitos\n(M3)", u["M3_CON"])] + [(k, u[c]) for k, c in sv.PRA_ITENS.items()]
    rng = np.random.default_rng(sv.SEED)
    bp = ax.boxplot([s.dropna() for _, s in series], widths=0.45, patch_artist=True, showfliers=False,
                    medianprops=dict(color="black", linewidth=1.4))
    for i, patch in enumerate(bp["boxes"]):
        patch.set(facecolor="#d9d9d9" if i == 0 else "white", edgecolor="#222222", linewidth=0.7)
    for i, (_, s) in enumerate(series, start=1):
        y = s.dropna().values
        ax.scatter(i + rng.uniform(-0.16, 0.16, len(y)), y + rng.uniform(-0.08, 0.08, len(y)), s=6, color="#555555", alpha=0.6, linewidths=0)
    ax.set_xticks(range(1, len(series) + 1), [n.replace("ᴿ", "ᴿ") for n, _ in series])
    ax.set_ylim(0.6, 5.4); ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_ylabel("Escala Likert (1 a 5)")
    for s_ in ("top", "right"):
        ax.spines[s_].set_visible(False)
    fig.tight_layout()
    fig.savefig(GER / "fig_h2a.pdf")
    plt.close(fig)
    print("Gerado em", GER.relative_to(sv.RAIZ), "| hipóteses:", len(hs), "| válidas:", len(v))


if __name__ == "__main__":
    main()
