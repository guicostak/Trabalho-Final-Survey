# Resultados do survey (Parte 2), versão parcial com corte em 27/11/2026

> **Fonte:** exportação bruta do Microsoft Forms, lida pelo dashboard (`dashboard/app.py`) e pelo script `analise/survey.py`. Todos os números abaixo saem desses arquivos; ao atualizar a exportação, eles mudam sozinhos no dashboard.
> **Status:** **48 respostas válidas, abaixo da meta de 50.** A coleta segue aberta até 04/12 (desvio D3). Leia tudo como resultado parcial.
> **Linguagem:** o desenho é transversal; os resultados são **associações**, nunca efeitos causais da IA.

## 1. Coleta e limpeza

| Etapa | Respostas | Detalhe |
|---|---|---|
| Recebidas no Forms | 56 | IDs 1 a 56 |
| Pré-teste (E0) | −5 | Enviadas até 13/11 23:59 (IDs 1–5) — desvio D1 |
| Coleta oficial | 51 | 14/11 (2) e 25–26/11 (49) — desvio D2 |
| E1: não cursou tecnologia | −1 | ID 39 |
| E2: falhou na pergunta de atenção | −1 | ID 45 (marcou "Nem concordo nem discordo" em tudo) |
| E3: PRA todo em 1 | −1 | ID 47 |
| E4: duração < 1/3 da mediana (61 s) | 0 | Mediana de 183 s; a mais rápida levou 87 s |
| E5: duplicata técnica | 0 | — |
| **Válidas** | **48** | Margem de erro nominal de **±14,1 p.p.** |
| Usuários de IA (QP2 a QP4) | 46 | Fora: ID 12 (IAF = Nunca) e ID 22 (IAU = Não uso IA) |

**Perfil das válidas.** Curso: ES 24 (50%), SI 13 (27%), ADS 4, outro curso 4, CC 3. Situação: estudante do 5º período em diante 25 (52%), formado há até 3 anos 14, formado há mais de 3 anos 5, estudante do 1º ao 4º período 4. Atuam na área: 41 (85%). Começaram a aprender antes de 2023: 38 (79%). A amostra é, sobretudo, de **quem já atua e aprendeu antes da IA generativa**, o que limita QP4.

## 2. Confiabilidade dos construtos

| Construto | α de Cronbach | IC 95% (bootstrap) | Avaliação | Consequência |
|---|---|---|---|---|
| CON (3 itens) | 0,63 | 0,41 a 0,80 | Questionável (0,60–0,70) | Mantido como escore M3, com ressalva (efeito teto: 98% concordam com CON1) |
| PRA (4 itens) | 0,37 | −0,14 a 0,61 | Insuficiente (< 0,60) | **Itens analisados separadamente** (regra do protocolo; desvio D4) |

PRA2 ("consigo escrever do zero, sem IA") quase não se correlaciona com os outros itens de PRA (ρ entre −0,12 e 0,03) e se correlaciona com a confiança (ρ = 0,57). Ele mede **capacidade**, enquanto PRA1, PRA3 e PRA4 medem **hábito** de escrever. Essa é a principal lição de medição do estudo.

## 3. Respostas às questões de pesquisa

α = 0,05 bilateral; correção de **Holm** sobre **22 testes** confirmatórios (a família cresceu porque PRA foi separado). Tamanhos de efeito com IC 95% por bootstrap (5.000 reamostragens).

### QP1 — Como a IA é usada para aprender programação e como o seu efeito é avaliado? (descritiva, n = 48)

- **93,7%** usam IA **sempre** (60,4%) ou **frequentemente** (33,3%) ao estudar programação.
- Principal finalidade: **entender conceitos ou erros** (50,0%), revisar o próprio código (25,0%), obter código pronto (16,7%), gerar exemplos ou exercícios (6,2%).
- **68,8%** dizem que a IA **melhorou** o aprendizado (IC 95% de Wilson: 54,7% a 80,1%; margem ±13,1 p.p.). **22,9%** dizem que **piorou** (um pouco ou muito).
- Conceitos com IA (M3): mediana de 4,67 em 5, perto do teto.

### QP2 (central) — A IA favorece o aprendizado de conceitos em detrimento da prática de escrita? (n = 46)

| Hipótese | Resultado | Efeito [IC 95%] | p (Holm) | Decisão |
|---|---|---|---|---|
| H2a: conceitos > prática | Conceitos (mediana 4,67) acima de **todos** os itens de prática: PRA1 = 2, PRA2 = 4, PRA3 = 2, PRA4ᴿ = 1 | r de 0,72 a 0,88 (grandes) | < 0,001 em todos | **Rejeita H0** nos 4 itens |
| H2b: uso × conceitos | Quem usa mais IA avalia melhor o aprendizado de conceitos | ρ = 0,40 [0,10; 0,66], médio | 0,092 | Não rejeita (p bruto = 0,006) |
| H2c: uso × prática | Correlações negativas em 3 dos 4 itens (PRA1: ρ = −0,30) | ρ de −0,30 a 0,05 | ≥ 0,69 | Não rejeita |

**Leitura.** O padrão central é forte: os respondentes **concordam que a IA ajuda a entender conceitos** e, ao mesmo tempo, **relatam pouca prática de escrita sem IA**. **96%** concordam que, "desde que passaram a usar IA, escrevem menos código por conta própria" (74% concordam totalmente). Como CON e PRA são itens diferentes, H2a mostra um padrão relativo, não uma diferença na mesma régua (protocolo, §5). A associação com a frequência de uso vai na direção esperada (H2b positiva, H2c negativa), mas não resiste à correção.

### QP3 — A finalidade de uso e a prática de escrita se associam à confiança para programar sem IA? (n = 46)

| Hipótese | Resultado | Efeito [IC 95%] | p (Holm) | Decisão |
|---|---|---|---|---|
| H3a: prática por finalidade (código pronto × demais; regra i) | δ negativo nos 4 itens: quem busca código pronto relata menos prática (PRA2: mediana 2 × 4) | δ de −0,13 a −0,38 | 1,000 | Não rejeita (só 8 no grupo "código pronto") |
| H3b: prática × confiança | **PRA2 × confiança: ρ = 0,57 [0,36; 0,73], grande**. PRA1, PRA3 e PRA4ᴿ: ρ entre −0,08 e 0,17 | — | **< 0,001** (PRA2) | **Rejeita H0 só para PRA2** |

**Leitura.** Quem diz **conseguir escrever do zero sem IA** é quem se sente confiante para programar sem IA. Escrever a maior parte do código ou praticar sem IA (hábito) **não** se associou à confiança. Cuidado: PRA2 e CONF são parecidos em conteúdo, então parte da correlação pode ser sobreposição de construtos (ameaça de construto).

### QP4 — Quem começou a aprender depois da popularização da IA pratica menos a escrita? (n = 46)

| Hipótese | Resultado | Efeito [IC 95%] | p (Holm) | Decisão |
|---|---|---|---|---|
| H4a: depois × antes de 2023 | PRA2 menor em quem começou depois (mediana 2 × 4); nos outros itens não há diferença | PRA2: δ = −0,58 [−0,85; −0,24], grande | 0,072 (p bruto = 0,004) | Não rejeita |
| H4b: atua × não atua | **Só descritiva** (não atua: n = 7; regra iii) | — | — | Sem teste |
| H4c: finalidade × situação (regra ii) | Código pronto: 21% dos estudantes × 12% dos formados | V = 0,11 [0,01; 0,36], pequeno | 1,000 | Não rejeita (Fisher) |

**Leitura.** O único sinal está em PRA2: quem começou a aprender depois da IA generativa diz conseguir escrever do zero **menos** do que quem começou antes. O efeito é grande, mas o grupo "depois" tem só 10 pessoas e o resultado não resiste a Holm. Fica como **hipótese para estudos futuros**, não como conclusão.

### Análise de sensibilidade (plano original, M4 como escore único)

Com M4 e a família original de 7 testes: H2a continua significativa (p Holm < 0,001) e **H2b também passa** (p Holm = 0,035); as demais não. Ou seja, a conclusão sobre QP2 não depende da regra de separação dos itens, mas a de H2b depende.

## 4. Resposta aberta (15 respostas válidas; codificação pendente)

Pré-codificação sugerida, a validar por dois integrantes (κ ≥ 0,60; desvio D7): **T2 Risco à prática e aos fundamentos** (4), **T1 IA facilita entender conceitos e erros** (3), **T3 Depende do modo de uso e da base prévia** (3), **T4 Mudança do papel do programador** (3), **T5 Pressão por produtividade e dependência** (2). Os temas repetem o achado quantitativo: a IA ajuda a entender, mas pode tirar a prática e os fundamentos, sobretudo de quem está começando.

## 5. Limitações (para a defesa)

1. **Parcial e abaixo da meta:** 48 válidas; margem nominal de ±14,1 p.p. e poder só para efeitos grandes.
2. **Amostra concentrada:** ES e SI, quem já atua e quem aprendeu antes de 2023; coleta em ~26 horas na rede do grupo (autosseleção e bola de neve).
3. **Medição de PRA:** α = 0,37; o construto mistura capacidade (PRA2) e hábito (PRA1, PRA3, PRA4). Para uma nova rodada, separar em dois construtos com 3 itens cada.
4. **Efeito teto em CON** e **desejabilidade social** (admitir dependência de IA).
5. **Não usuários de IA:** só 2 válidos; QP2 a QP4 descrevem apenas quem usa IA.
6. **Transversal:** não permite afirmar que a IA *causa* menos prática.

## 6. Checklist do enunciado (Parte 2)

| Exigência | Onde está |
|---|---|
| Lê os dados brutos | `dashboard/app.py` lê `dados/brutos/*.csv` ou `*.xlsx` (local) ou `dados/respostas_anonimizadas.csv` (público) |
| Perfil, recebidas, descartes e motivo | Aba "Perfil e limpeza" |
| Likert em barras divergentes | Aba "Itens Likert" |
| QP com teste, p, efeito e margem de erro | Aba "Questões de pesquisa" |
| Filtros por segmento | Barra lateral (curso, situação, atuação, momento; n < 5 ocultado) |
| α de Cronbach | Aba "Confiabilidade" |
| Metodologia e desvios | Aba "Metodologia e desvios" (lê `DESVIOS.md`) |
| Evidências da coleta | Exportação bruta com data e hora (aba "Dados brutos"); **falta**: capturas datadas dos canais de divulgação |
