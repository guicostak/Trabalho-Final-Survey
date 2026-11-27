"""Dashboard do survey (Parte 2) — lê a exportação BRUTA do Microsoft Forms.

Rodar:
    .venv/bin/streamlit run dashboard/app.py
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "analise"))
import survey as sv  # noqa: E402

st.set_page_config(page_title="Survey · IA e aprendizado de programação", page_icon="📊", layout="wide")

# ----------------------------------------------------------------- paleta (skill dataviz, validada)
DIV = {1: "#b3302f", 2: "#e8807f", 3: "#d6d5cf", 4: "#6da7ec", 5: "#1c5cab"}  # azul ↔ vermelho, cinza no meio
CAT = ["#2a78d6", "#eb6834", "#1baf7a"]
INK2, MUTED, GRID = "#52514e", "#898781", "#e1e0d9"
def fmt(x, nd=2):
    return "—" if x is None or (isinstance(x, float) and not np.isfinite(x)) else f"{x:.{nd}f}".replace(".", ",")


MIN_SEG = 5  # protocolo §6: o painel não exibe segmentos com menos de 5 respondentes


def layout(fig: go.Figure, h: int = 320, **kw) -> go.Figure:
    fig.update_layout(height=h, margin=dict(l=8, r=8, t=36, b=8), paper_bgcolor="rgba(0,0,0,0)",
                      plot_bgcolor="rgba(0,0,0,0)", font=dict(family="system-ui, -apple-system, Segoe UI, sans-serif", size=13),
                      hoverlabel=dict(font_size=13), **({"legend": dict(orientation="h", y=1.02, yanchor="bottom", x=0, xanchor="left")} | kw))
    fig.update_xaxes(gridcolor=GRID, zerolinecolor="#c3c2b7", tickfont=dict(color=MUTED))
    fig.update_yaxes(gridcolor=GRID, zerolinecolor="#c3c2b7", tickfont=dict(color=INK2))
    return fig


# ----------------------------------------------------------------- dados
@st.cache_data(show_spinner="Lendo a exportação bruta do Forms…")
def carregar(caminho: str | None, mtime: float):
    t = sv.carregar_tudo(Path(caminho) if caminho else None)
    sha = hashlib.sha256(Path(caminho).read_bytes()).hexdigest() if caminho else ""
    return t["d"], t["origem"], sha, t["d"].attrs.get("mediana_duracao_s")


@st.cache_data(show_spinner="Rodando os testes pré-registrados…")
def rodar_testes(ids: tuple[int, ...], mtime: float, n_boot: int):
    d, *_ = carregar(str(ARQ) if ARQ else None, mtime)
    v = d[d["id"].isin(ids)]
    return sv.testar(v, n_boot=n_boot), sv.confiabilidade(v[v["USA_IA"]]), sv.descritivas(v)


ARQ = sv.arquivo_bruto_mais_recente()
MTIME = ARQ.stat().st_mtime if ARQ else 0.0
d, origem, sha, mediana = carregar(str(ARQ) if ARQ else None, MTIME)
validas_all = d[d["valida"]]

# ----------------------------------------------------------------- filtros por segmento
st.sidebar.header("Filtros por segmento")
st.sidebar.caption("Valem para todas as abas. Segmentos com menos de 5 respondentes não são exibidos (protocolo, §6).")
FILTROS = {"CUR_c": ("Curso", sv.ROTULOS["CUR"]), "SIT_c": ("Situação", sv.ROTULOS["SIT"]),
           "ATU_c": ("Atuação na área", sv.ROTULOS["ATU"]), "MOM_c": ("Começou a aprender", sv.ROTULOS["MOM"])}
sel = {}
for col, (nome, rot) in FILTROS.items():
    cont = validas_all[col].value_counts()
    opcoes = [k for k in rot if cont.get(k, 0) >= MIN_SEG]
    escondidos = [rot[k] for k in rot if 0 < cont.get(k, 0) < MIN_SEG]
    sel[col] = st.sidebar.multiselect(nome, opcoes, format_func=lambda k, r=rot: f"{r[k]} ({cont.get(k, 0)})",
                                      help=("Ocultos por terem n < 5: " + ", ".join(escondidos)) if escondidos else None)
filtrado = any(sel.values())
v = validas_all.copy()
for col, vals in sel.items():
    if vals:
        v = v[v[col].isin(vals)]
if filtrado and len(v) < MIN_SEG:
    st.warning(f"O segmento selecionado tem {len(v)} respondente(s). Por privacidade (n < 5), os resultados não são exibidos.")
    st.stop()
u = v[v["USA_IA"]]
hs, conf, desc = rodar_testes(tuple(sorted(v["id"])), MTIME, 1000 if filtrado else sv.N_BOOT)

# ----------------------------------------------------------------- cabeçalho
st.title("Aprendizado de programação na era da IA generativa")
st.caption("Survey pré-registrado · Medição e Experimentação em ES · PUC Minas Lourdes · 2º/2026 · "
           f"fonte: `{origem}`")
if filtrado:
    st.info(f"**Filtro ativo** ({len(v)} respondentes válidos). Os testes abaixo são **exploratórios**; "
            "os resultados confirmatórios são os da amostra completa, sem filtro.", icon="🔎")
n_val = int(d["valida"].sum())
if n_val < sv.META_VALIDAS:
    st.warning(f"**Coleta parcial:** {n_val} respostas válidas, abaixo da meta de {sv.META_VALIDAS}. "
               "O dashboard relê o arquivo bruto: basta atualizar a exportação para recalcular tudo.", icon="⚠️")

abas = st.tabs(["Perfil e limpeza", "Itens Likert", "Questões de pesquisa", "Confiabilidade",
                "Resposta aberta", "Metodologia e desvios", "Dados brutos"])


# =================================================================== 1. PERFIL E LIMPEZA
with abas[0]:
    rec = len(d); pre = int((d["motivo"] == "E0").sum()); desc_n = int(((d["motivo"] != "") & (d["motivo"] != "E0")).sum())
    c = st.columns(5)
    c[0].metric("Respostas recebidas", rec)
    c[1].metric("Pré-teste (excluídas)", pre)
    c[2].metric("Descartadas na limpeza", desc_n)
    c[3].metric("Válidas", n_val, delta=f"{n_val - sv.META_VALIDAS} da meta de {sv.META_VALIDAS}", delta_color="normal" if n_val >= sv.META_VALIDAS else "inverse")
    c[4].metric("Margem de erro (p = 0,5)", f"±{fmt(100 * sv.margem_erro(n_val), 1)} p.p.", help="Nominal: a amostra não é probabilística.")

    st.subheader("Descartes e motivo de cada um")
    tab = pd.DataFrame([{"Regra": k, "Motivo": m, "Respostas": int((d["motivo"] == k).sum()),
                         "IDs no Forms": ", ".join(map(str, d.loc[d["motivo"] == k, "id"])) or "—"} for k, m in sv.MOTIVOS.items()])
    st.dataframe(tab, hide_index=True, use_container_width=True)
    st.caption(f"Ordem de aplicação E0 → E5; cada resposta recebe o primeiro motivo que se aplica. "
               f"E4 usa a mediana da coleta oficial ({mediana:.0f} s; limite = {mediana / 3:.0f} s). "
               f"Das {n_val} válidas, {int(validas_all['USA_IA'].sum())} usam IA e entram em QP2–QP4 (USA_IA do codebook).")

    st.subheader("Respostas por dia")
    por_dia = d.assign(dia=d["envio"].dt.date, grupo=np.where(d["motivo"] == "E0", "Pré-teste",
                       np.where(d["valida"], "Válida", "Descartada")))
    dias = pd.date_range(por_dia["dia"].min(), por_dia["dia"].max(), freq="D").date
    fig = go.Figure()
    for g, cor in [("Válida", CAT[0]), ("Descartada", CAT[1]), ("Pré-teste", MUTED)]:
        cnt = por_dia[por_dia["grupo"] == g].groupby("dia").size().reindex(dias, fill_value=0)
        fig.add_bar(x=[x.strftime("%d/%m") for x in dias], y=cnt.values, name=g, marker_color=cor,
                    marker_line=dict(color="#fcfcfb", width=1.5), hovertemplate="%{x}: %{y} " + g.lower() + "(s)<extra></extra>")
    layout(fig, 300, barmode="stack", yaxis_title="Respostas")
    st.plotly_chart(fig, use_container_width=True)
    st.caption("A taxa de resposta não é calculável (link aberto); relata-se o número de respostas por dia (protocolo, §5).")

    st.subheader(f"Perfil da amostra válida (n = {len(v)})")
    cols = st.columns(4)
    for i, (col, (nome, rot)) in enumerate(FILTROS.items()):
        cnt = v[col].value_counts().reindex(list(rot), fill_value=0)
        cnt = cnt[cnt.index != "NENHUM"]
        fig = go.Figure(go.Bar(x=cnt.values, y=[rot[k] for k in cnt.index], orientation="h", marker_color=CAT[0],
                               text=[f"{x} ({100 * x / len(v):.0f}%)" for x in cnt.values], textposition="outside",
                               cliponaxis=False, hovertemplate="%{y}: %{x}<extra></extra>"))
        layout(fig, 230, title=dict(text=nome, font=dict(size=14)), showlegend=False)
        fig.update_xaxes(visible=False, range=[0, cnt.max() * 1.45]); fig.update_yaxes(autorange="reversed")
        cols[i].plotly_chart(fig, use_container_width=True)
    st.caption("Metas por segmento do protocolo (§2): 8 por curso e 10 que atuam na área. "
               f"Atingidas: ES ({int((validas_all['CUR_c'] == 'ES').sum())}), SI ({int((validas_all['CUR_c'] == 'SI').sum())}) e atuação. "
               "Não atingidas: CC, ADS e outros cursos (ver Desvios).")


# =================================================================== 2. LIKERT
CURTO = {"CON1": "entender conceitos", "CON2": "entender por que funciona/falha", "CON3": "erros e documentação",
         "PRA1": "escrevo a maior parte do código", "PRA2": "consigo escrever do zero sem IA",
         "PRA3": "pratico sem nenhuma IA", "PRA4": "escrevo menos desde a IA (invertido)"}


def divergente(df: pd.DataFrame, itens: dict[str, str], titulo: str, rotulos=sv.LIKERT_ROT) -> go.Figure:
    st.markdown(f"**{titulo}**")
    linhas = []
    for col, txt in itens.items():
        s = df[col].dropna()
        pct = {k: 100 * (s == k).sum() / len(s) if len(s) else 0 for k in range(1, 6)}
        linhas.append((txt, pct, len(s)))
    fig = go.Figure()
    nomes = [t for t, _, _ in linhas]
    ordem = [(3, -0.5, False), (2, -1, True), (1, -1, True), (3, 0.5, True), (4, 1, True), (5, 1, True)]
    for k, fator, legenda in ordem:
        xs = [fator * p[k] for _, p, _ in linhas]
        fig.add_bar(y=nomes, x=xs, orientation="h", name=rotulos[k], marker_color=DIV[k], showlegend=legenda,
                    legendrank=k, marker_line=dict(color="#fcfcfb", width=1.5),
                    customdata=[[p[k], n] for _, p, n in linhas],
                    text=[f"{p[k]:.0f}%" if p[k] >= 8 and fator != -0.5 and fator != 0.5 else "" for _, p, _ in linhas],
                    textposition="inside", insidetextanchor="middle",
                    textfont=dict(color="#0b0b0b" if k in (2, 3, 4) else "#ffffff"),
                    hovertemplate="%{y}<br>" + rotulos[k] + ": %{customdata[0]:.1f}% (n = %{customdata[1]})<extra></extra>")
    layout(fig, 70 + 52 * len(linhas), barmode="relative", bargap=0.35,
           legend=dict(orientation="h", y=1.0, yanchor="bottom", x=0, xanchor="left", traceorder="normal"))
    fig.update_layout(margin=dict(l=8, r=8, t=56, b=8))
    fig.update_xaxes(range=[-100, 100], tickvals=[-100, -50, 0, 50, 100], ticktext=["100%", "50%", "0", "50%", "100%"])
    fig.update_yaxes(autorange="reversed")
    return fig


with abas[1]:
    st.markdown("Barras divergentes: discordância à esquerda, concordância à direita e o neutro dividido ao meio. "
                f"Base: usuários de IA válidos (n = {len(u)}).")
    st.plotly_chart(divergente(u, {f"{c}_n": f"{c} · {CURTO[c]}" for c in sv.CON}, "Aprendizado de conceitos com IA (CON)"),
                    use_container_width=True)
    st.plotly_chart(divergente(u, {f"{c}_n": f"{c} · {CURTO[c]}" for c in sv.PRA}, "Prática de escrita de código (PRA), respostas originais"),
                    use_container_width=True)
    st.caption("PRA4 aparece como respondido; na análise ele é invertido (6 − x), porque concordar significa praticar menos. "
               "Nenhum respondente marcou a coluna “Não uso IA” nas grades.")
    rot_avg = {1: "Piorou muito", 2: "Piorou um pouco", 3: "Não mudou", 4: "Melhorou um pouco", 5: "Melhorou muito"}
    rot_conf = {1: "Nada", 2: "Pouco", 3: "Razoavelmente", 4: "Confiante", 5: "Muito"}
    st.plotly_chart(divergente(v, {"AVG_n": "AVG"}, f"Efeito geral da IA no aprendizado (todos os válidos, n = {len(v)})", rot_avg), use_container_width=True)
    st.plotly_chart(divergente(v, {"CONF_n": "CONF"}, f"Confiança para escrever um programa do zero sem IA (todos os válidos, n = {len(v)})", rot_conf), use_container_width=True)
    with st.expander("Texto completo dos itens"):
        st.markdown("\n".join(f"- **{k}** — {t}" for k, t in sv.ITENS_TEXTO.items()))
    with st.expander("Tabela (frequências por item)"):
        linhas = []
        for c in sv.CON + sv.PRA:
            s = u[f"{c}_n"]
            linhas.append({"Item": c, **{sv.LIKERT_ROT[k]: int((s == k).sum()) for k in range(1, 6)},
                           "Mediana": s.median(), "IIQ": f"{s.quantile(.25):.1f}–{s.quantile(.75):.1f}"})
        st.dataframe(pd.DataFrame(linhas), hide_index=True, use_container_width=True)


# =================================================================== 3. QUESTÕES DE PESQUISA
def fmt_p(p):
    return "—" if p is None else ("< 0,001" if p < 0.001 else f"{p:.3f}".replace(".", ","))


def fmt(x, nd=2):
    return "—" if x is None or (isinstance(x, float) and not np.isfinite(x)) else f"{x:.{nd}f}".replace(".", ",")


def tabela_h(lista):
    linhas = []
    for h in lista:
        ic = h.efeito_ic
        linhas.append({"Hipótese": h.id, "Variável": h.variavel or "—", "Teste": h.teste, "n": h.n,
                       "Estatística": h.estatistica or "—", "p": fmt_p(h.p), "p (Holm)": fmt_p(h.p_holm),
                       "Efeito": f"{h.efeito_nome} = {fmt(h.efeito)}" if h.efeito is not None else "—",
                       "IC 95% (bootstrap)": f"[{fmt(ic[0])}; {fmt(ic[1])}]" if ic and np.isfinite(ic[0]) else "—",
                       "Magnitude": h.magnitude, "Margem (p.p.)": f"±{fmt(h.margem_erro_pp, 1)}", "Decisão": h.decisao})
    return pd.DataFrame(linhas)


def bolhas(df, x, y, xt, yt, xr=None, yr=None):
    c = df[[x, y]].dropna().round(2).value_counts().reset_index(name="n")
    fig = go.Figure(go.Scatter(x=c[x], y=c[y], mode="markers", marker=dict(size=8 + 7 * np.sqrt(c["n"]), color=CAT[0], opacity=0.75,
                    line=dict(color="#fcfcfb", width=2)), customdata=c["n"],
                    hovertemplate=f"{xt}: %{{x}}<br>{yt}: %{{y}}<br>%{{customdata}} respondente(s)<extra></extra>"))
    layout(fig, 300, showlegend=False, xaxis_title=xt, yaxis_title=yt)
    fig.update_xaxes(range=xr or [0.5, 5.5], dtick=1); fig.update_yaxes(range=yr or [0.5, 5.5], dtick=1)
    return fig


def caixas(grupos: dict[str, pd.Series], yt: str):
    fig = go.Figure()
    for i, (nome, s) in enumerate(grupos.items()):
        fig.add_box(y=s, name=f"{nome} (n = {len(s)})", marker_color=CAT[0] if i == 0 else CAT[1], boxpoints="all", jitter=0.5, pointpos=0,
                    line=dict(width=2), hovertemplate="%{y:.2f}<extra></extra>")
    layout(fig, 300, showlegend=False, yaxis_title=yt)
    fig.update_yaxes(range=[0.5, 5.5], dtick=1)
    return fig


def mostrar(hlist, chave):
    st.dataframe(tabela_h(hlist), hide_index=True, use_container_width=True)
    for h in hlist:
        st.markdown(f"- **{h.id}** — {h.descricao}. Esperado: *{h.direcao_esperada}*. {h.leitura}"
                    + (f" _{h.regra_condicional}_" if h.regra_condicional else ""))


H = {h.id: h for h in hs}
conf_ = [h for h in hs if h.familia == "confirmatória"]
ref_ = [h for h in hs if h.familia == "referência"]
separado = bool(ref_)

with abas[2]:
    n_testes = sum(1 for h in conf_ if h.status == "testada")
    st.markdown(f"α = 0,05 bilateral · **correção de Holm** sobre {n_testes} testes confirmatórios · tamanhos de efeito com IC 95% "
                f"por bootstrap ({1000 if filtrado else sv.N_BOOT} reamostragens) · QP2–QP4 usam só quem usa IA (n = {len(u)}).")
    if separado:
        st.info(f"O α de Cronbach de PRA foi {fmt(conf['PRA']['alfa'])} (< 0,60). Pela regra do protocolo (§5), os **itens de PRA "
                "são analisados separadamente**: cada hipótese que usava o escore M4 vira um teste por item (PRA1, PRA2, PRA3, PRA4ᴿ), "
                "todos na mesma família de Holm. O escore M4 aparece só como referência e na análise de sensibilidade.", icon="ℹ️")

    # QP1
    st.header("QP1 · Como a IA é usada para aprender programação e como o seu efeito é avaliado?")
    st.caption(f"Descritiva, com IC de Wilson (95%) e margem de erro de cada proporção. Base: todos os válidos (n = {desc['n']}).")
    c1, c2 = st.columns(2)
    for alvo, chave, titulo, rot in [(c1, "IAF", "Frequência de uso de IA ao estudar", None),
                                     (c2, "IAU", "Principal finalidade de uso", sv.ROTULOS["IAU"])]:
        dd = pd.DataFrame(desc[chave])
        nomes = [rot[k] if rot else k for k in dd["categoria"]]
        fig = go.Figure(go.Bar(y=nomes, x=dd["pct"], orientation="h", marker_color=CAT[0],
                               error_x=dict(type="data", symmetric=False, array=dd["ic95"].str[1] - dd["pct"],
                                            arrayminus=dd["pct"] - dd["ic95"].str[0], color=MUTED, thickness=1.5),
                               customdata=np.stack([dd["n"], dd["ic95"].str[0], dd["ic95"].str[1], dd["margem_pp"]], axis=1),
                               hovertemplate="%{y}: %{x:.1f}% (n = %{customdata[0]})<br>IC 95%: %{customdata[1]}–%{customdata[2]}%<br>margem ±%{customdata[3]} p.p.<extra></extra>"))
        fig.add_scatter(y=nomes, x=dd["ic95"].str[1] + 2, mode="text", text=[f"{p:.0f}% (n = {n})" for p, n in zip(dd["pct"], dd["n"])],
                        textposition="middle right", textfont=dict(color=INK2), hoverinfo="skip", cliponaxis=False)
        layout(fig, 280, title=dict(text=titulo, font=dict(size=14)), showlegend=False)
        fig.update_xaxes(range=[0, 100], ticksuffix="%"); fig.update_yaxes(autorange="reversed")
        alvo.plotly_chart(fig, use_container_width=True)
    pm = desc["pct_melhorou"]
    m3 = u["M3_CON"]
    k = st.columns(3)
    k[0].metric("Dizem que a IA melhorou o aprendizado", f"{fmt(pm['pct'], 1)}%", help="AVG = melhorou um pouco ou muito")
    k[1].metric("IC 95% (Wilson)", f"{fmt(pm['ic95'][0], 1)}–{fmt(pm['ic95'][1], 1)}%")
    k[2].metric("Margem de erro", f"±{fmt(pm['margem_pp'], 1)} p.p.")
    st.markdown(f"Usam IA **sempre ou frequentemente** {fmt(sum(x['pct'] for x in desc['IAF'] if x['categoria'] in ('Sempre', 'Frequentemente')), 1)}% "
                f"dos válidos. O escore de conceitos (M3) tem mediana {fmt(m3.median())} (IIQ {fmt(m3.quantile(.25))}–{fmt(m3.quantile(.75))}), "
                f"perto do teto da escala.")

    # QP2
    st.header("QP2 (central) · A IA favorece o aprendizado de conceitos em detrimento da prática de escrita?")
    mostrar([h for h in conf_ if h.qp == "QP2"], "qp2")
    c1, c2 = st.columns(2)
    alvo = {"Conceitos (M3)": u["M3_CON"], **{r: u[c] for r, c in sv.PRA_ITENS.items()}} if separado else {"Conceitos (M3)": u["M3_CON"], "Prática (M4)": u["M4_PRA"]}
    c1.plotly_chart(caixas(alvo, "Escore / item (1–5)").update_layout(title="H2a · Conceitos × prática de escrita"), use_container_width=True)
    c2.plotly_chart(bolhas(u, "IAF_n", "M3_CON", "Frequência de uso (1 = nunca … 5 = sempre)", "Conceitos (M3)").update_layout(title="H2b · Uso × conceitos"),
                    use_container_width=True)
    st.caption("H2a compara itens diferentes (CON × PRA), então indica um padrão relativo, não uma diferença na mesma régua (protocolo, §5).")

    # QP3
    st.header("QP3 · A finalidade de uso e a prática de escrita se associam à confiança para programar sem IA?")
    mostrar([h for h in conf_ if h.qp == "QP3"], "qp3")
    c1, c2 = st.columns(2)
    var3 = "PRA2_n" if separado else "M4_PRA"
    nome3 = "PRA2 (consigo escrever do zero)" if separado else "Prática (M4)"
    c1.plotly_chart(bolhas(u, var3, "CONF_n", nome3, "Confiança sem IA (CONF)").update_layout(title=f"H3b · {nome3} × confiança"), use_container_width=True)
    c2.plotly_chart(caixas({"Código pronto": u.loc[u["IAU_c"] == "CODIGO", var3], "Demais finalidades": u.loc[u["IAU_c"] != "CODIGO", var3]},
                           nome3).update_layout(title=f"H3a · {nome3} por finalidade"), use_container_width=True)

    # QP4
    st.header("QP4 · Quem começou a aprender depois da popularização da IA pratica menos a escrita?")
    mostrar([h for h in conf_ if h.qp == "QP4"], "qp4")
    c1, c2 = st.columns(2)
    c1.plotly_chart(caixas({sv.ROTULOS["MOM"]["ANTES"]: u.loc[u["MOM_c"] == "ANTES", var3],
                            sv.ROTULOS["MOM"]["DEPOIS"]: u.loc[u["MOM_c"] == "DEPOIS", var3]}, nome3).update_layout(title=f"H4a · {nome3}: antes × depois"),
                    use_container_width=True)
    t4 = H.get("H4c")
    if t4 and "tabela" in t4.grupos:
        tb = pd.DataFrame(t4.grupos["tabela"]).T
        fig = go.Figure()
        for i, fin in enumerate(tb.index):
            pct = 100 * tb.loc[fin] / tb.sum(axis=0)
            fig.add_bar(x=list(tb.columns), y=pct.values, name=fin, marker_color=CAT[i], marker_line=dict(color="#fcfcfb", width=1.5),
                        customdata=tb.loc[fin].values, text=[f"{p:.0f}%" for p in pct.values], textposition="inside",
                        hovertemplate="%{x} · " + fin + ": %{y:.0f}% (n = %{customdata})<extra></extra>")
        layout(fig, 300, barmode="stack", title="H4c · Finalidade por situação", yaxis_title="% do grupo",
               legend=dict(orientation="v", x=1.02, y=1, yanchor="top", xanchor="left"))
        c2.plotly_chart(fig, use_container_width=True)

    st.header("Análise de sensibilidade · plano original (M4 como escore)")
    sens = [h for h in hs if h.p_holm_plano_original is not None]
    st.markdown("Holm aplicado à família original de testes do protocolo, com M4 como escore único. "
                "Serve para mostrar quanto a decisão depende da regra de separação dos itens; **não substitui** a análise confirmatória acima.")
    df_s = tabela_h(sens)
    df_s["p (Holm, plano original)"] = [fmt_p(h.p_holm_plano_original) for h in sens]
    df_s["Decisão no plano original"] = ["Rejeita H0" if h.p_holm_plano_original < sv.ALFA else "Não rejeita H0" for h in sens]
    st.dataframe(df_s.drop(columns=["p (Holm)", "Decisão"]), hide_index=True, use_container_width=True)
    if ref_ and any(h.status == "descritiva" for h in ref_):
        st.caption("H4b ficou só descritiva nos dois cenários (regra iii: “Não atua” tem n < 10).")


# =================================================================== 4. CONFIABILIDADE
with abas[3]:
    st.markdown(f"α de Cronbach dos construtos com vários itens, nos usuários de IA válidos (n = {len(u)}). "
                "Critério do protocolo: ≥ 0,70 aceitável; entre 0,60 e 0,70 questionável; < 0,60 → itens analisados separadamente.")
    c = st.columns(2)
    for i, (nome, titulo) in enumerate([("CON", "Aprendizado de conceitos com IA (CON1–CON3)"), ("PRA", "Prática de escrita (PRA1–PRA3, PRA4ᴿ)")]):
        r = conf[nome]
        with c[i]:
            st.subheader(titulo)
            st.metric("α de Cronbach", fmt(r["alfa"]), help=f"IC 95% bootstrap: {fmt(r['ic95'][0])}–{fmt(r['ic95'][1])}")
            st.markdown(f"IC 95% (bootstrap): **{fmt(r['ic95'][0])} a {fmt(r['ic95'][1])}** · k = {r['k']} itens · n = {r['n']}  \n"
                        f"Avaliação: **{r['avaliacao']}**")
            st.dataframe(pd.DataFrame({"Item removido": list(r["alfa_sem_item"]), "α sem o item": [fmt(a) for a in r["alfa_sem_item"].values()]}),
                         hide_index=True, use_container_width=True)
    cols = [f"{c}_n" for c in sv.CON] + ["PRA1_n", "PRA2_n", "PRA3_n", "PRA4_inv"]
    nomes = sv.CON + ["PRA1", "PRA2", "PRA3", "PRA4ᴿ"]
    m = u[cols].corr(method="spearman").values
    fig = go.Figure(go.Heatmap(z=m, x=nomes, y=nomes, zmin=-1, zmax=1, colorscale=[[0, DIV[1]], [0.5, "#f0efec"], [1, DIV[5]]],
                               text=np.round(m, 2), texttemplate="%{text}", hovertemplate="%{y} × %{x}: ρ = %{z:.2f}<extra></extra>",
                               xgap=2, ygap=2, colorbar=dict(title="ρ")))
    layout(fig, 430, title="Correlação de Spearman entre os itens")
    fig.update_yaxes(autorange="reversed")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("**Leitura.** CON tem α questionável, em parte por efeito teto (quase todos concordam). Em PRA, PRA2 "
                "(“consigo escrever do zero”) quase não se correlaciona com os demais itens: ele mede mais **capacidade** que **hábito** "
                "de praticar, e se aproxima da confiança (CONF). Por isso PRA não forma um escore único confiável.")


# =================================================================== 5. RESPOSTA ABERTA
with abas[4]:
    cod_path = sv.ARQ_ABR_COD
    abr = v[v["ABR"].str.strip() != ""][["id", "ABR"]]
    st.markdown(f"**{len(abr)}** respostas abertas entre os válidos ({100 * len(abr) / max(len(v), 1):.0f}%). "
                "Análise temática indutiva (Braun e Clarke, 2006): dois integrantes codificam 20% de forma independente, calcula-se o κ de Cohen (meta ≥ 0,60), "
                "as divergências são resolvidas por consenso e o livro de códigos orienta o restante.")
    if cod_path.exists():
        cod = pd.read_csv(cod_path, dtype=str, keep_default_na=False)
        cod["id"] = cod["id"].astype(int)
        cod = cod[cod["id"].isin(v["id"])]
        dupla = cod[(cod["codificador_1"] != "") & (cod["codificador_2"] != "")]
        if len(dupla) >= max(2, int(np.ceil(0.2 * len(cod)))):
            cats = sorted(set(dupla["codificador_1"]) | set(dupla["codificador_2"]))
            a, b = dupla["codificador_1"], dupla["codificador_2"]
            po = (a == b).mean()
            pe = sum((a == c).mean() * (b == c).mean() for c in cats)
            kappa = (po - pe) / (1 - pe) if pe < 1 else float("nan")
            st.metric("κ de Cohen (dupla codificação)", fmt(kappa), help=f"{len(dupla)} respostas codificadas pelos dois")
            col_tema, aviso = "tema_final", None
        else:
            st.warning("Dupla codificação **pendente**: preencha `codificador_1` e `codificador_2` em "
                       "`analise/abr_codificacao.csv` em pelo menos 20% das respostas para calcular o κ. "
                       "Até lá, o gráfico mostra a **pré-codificação sugerida**, que não conta como codificador.", icon="📝")
            col_tema = "tema_sugerido"
        temas = cod[col_tema].replace("", np.nan).dropna() if col_tema in cod else pd.Series(dtype=str)
        if col_tema == "tema_final" and temas.empty:
            temas = cod["tema_sugerido"].replace("", np.nan).dropna()
        cnt = temas.value_counts()
        fig = go.Figure(go.Bar(x=cnt.values, y=cnt.index, orientation="h", marker_color=CAT[0], text=cnt.values, textposition="outside",
                               cliponaxis=False, hovertemplate="%{y}: %{x}<extra></extra>"))
        layout(fig, 80 + 45 * len(cnt), showlegend=False, title="Temas (tema principal de cada resposta)")
        fig.update_yaxes(autorange="reversed"); fig.update_xaxes(visible=False)
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(cod.rename(columns={"texto": "Resposta"}), hide_index=True, use_container_width=True)
    else:
        st.dataframe(abr, hide_index=True, use_container_width=True)


# =================================================================== 6. METODOLOGIA E DESVIOS
with abas[5]:
    st.header("Metodologia")
    st.markdown(f"""
- **Desenho:** survey transversal, descritivo e correlacional, por questionário on-line anônimo (Microsoft Forms), sem ramificações.
- **Amostragem:** não probabilística, por conveniência com bola de neve; margem de erro **nominal** (±{fmt(100 * sv.margem_erro(n_val), 1)} p.p. para n = {n_val}).
- **Fonte dos dados:** `{origem}` · SHA-256 `{sha[:16]}…` · o painel lê a exportação bruta e recalcula tudo a cada atualização.
- **Pré-teste:** respostas enviadas até 13/11/2026 23:59 (prazo da Parte 1) são o pré-teste e ficam fora da análise (E0).
- **Limpeza:** E0 pré-teste → E1 não cursou tecnologia → E2 falhou em ATN1 → E3 PRA todo em 1 ou todo em 5 → E4 duração < 1/3 da mediana → E5 duplicata.
- **Codificação:** Likert 1–5, PRA4 invertido (6 − x), sem imputação; M3 = média de CON; M4 = média de PRA1–PRA3 e PRA4ᴿ; usuário de IA = IAF ≠ Nunca e IAU ≠ “Não uso IA”.
- **Testes:** Wilcoxon, Spearman, Mann-Whitney / Kruskal-Wallis, Fisher / χ²; α = 0,05 bilateral com Holm; efeitos r, ρ, δ de Cliff, ε², V de Cramér, com IC por bootstrap ({sv.N_BOOT} reamostragens, semente {sv.SEED}).
- **Causalidade:** desenho transversal; os resultados são associações, não efeitos causais da IA.
""")
    st.header("Desvios em relação ao protocolo")
    desv = RAIZ / "DESVIOS.md"
    if desv.exists():
        texto = desv.read_text(encoding="utf-8")
        linhas = [l for l in texto.splitlines() if l.startswith("|")]
        cab = [c.strip() for c in linhas[0].strip("|").split("|")] if linhas else []
        regs = [[c.strip() for c in l.strip("|").split("|")] for l in linhas[2:]]
        intro = [l for l in texto.splitlines() if l.startswith(">")]
        st.markdown("\n".join(intro))
        for r in regs:
            reg = dict(zip(cab, r))
            with st.expander(f"**{reg.get('#', '')}** · {reg.get('Seção do protocolo', '')} · {reg.get('Data', '')}", expanded=False):
                for campo in cab[3:]:
                    st.markdown(f"**{campo}:** {reg.get(campo, '')}")
        resto = texto.split("### ", 1)
        if len(resto) > 1:
            st.markdown("### " + resto[1])


# =================================================================== 7. DADOS BRUTOS
with abas[6]:
    st.markdown("Exportação bruta como recebida do Forms (horário em Brasília), com a duração e o motivo de descarte calculados. "
                "As respostas são anônimas: o formulário não coleta nome, e-mail nem IP.")
    mostrar_cols = ["id", "envio", "duracao_s", "motivo", *sv.CODIGOS]
    st.dataframe(d[mostrar_cols].assign(envio=d["envio"].dt.strftime("%d/%m/%Y %H:%M"), duracao_s=d["duracao_s"].round(0)),
                 hide_index=True, use_container_width=True, height=520)
