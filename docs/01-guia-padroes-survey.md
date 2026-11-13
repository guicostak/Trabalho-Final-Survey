# Guia de padrões para surveys científicos em Engenharia de Software

> **Para que serve:** reunir, em um só lugar, **como a comunidade científica planeja, estrutura e escreve** um survey por questionário pré-registrado. Foi a base de todas as decisões do nosso protocolo.
> **Como foi feito:** pesquisa na web em 13/11/2026 nas fontes primárias listadas abaixo. A seção 10 traz a lista completa com links.

---

## 1. Fontes de referência

| Fonte | O que define | Como usamos |
|---|---|---|
| **ACM SIGSOFT Empirical Standards: Questionnaire Surveys** (Ralph et al.) | Atributos **essenciais**, **desejáveis** e **extraordinários** de um survey, além de críticas inválidas e desvios aceitáveis | Checklist de qualidade (ver [`02-lista-de-requisitos.md`](02-lista-de-requisitos.md)) |
| **Empirical Standards: General Standard** | Atributos comuns a qualquer estudo empírico, como propósito, motivação, método nomeado e limitações | Estrutura geral do texto |
| **Empirical Standards: Registered Reports (suplemento)** | O que um plano pré-registrado (fase RR1) deve e **não deve** conter, e como justificar desvios | Formato do protocolo e do `DESVIOS.md` |
| **Empirical Standards: Sampling (suplemento)** | Como descrever população, quadro amostral, estratégia e representatividade | Seção 2 do protocolo e script de sorteio |
| **Kitchenham & Pfleeger (2008)**, *Personal Opinion Surveys* | Processo clássico de survey em ES e regras de redação de itens | Processo e redação do questionário |
| **Linåker et al. (2015)**, *Guidelines for Conducting Surveys in SE* (Lund) | Guia passo a passo: abordagem em equipe, definição do que medir, alinhamento das perguntas aos objetivos, amostragem e pré-teste | Ordem das etapas |
| **Molléri, Petersen & Mendes (2020)**, *An empirically evaluated checklist for surveys in SE* (IST) | Checklist validado empiricamente para planejar e relatar surveys | Conferência final |
| **Baltes & Ralph (2022)**, *Sampling in SE research* (EMSE) | Taxonomia de estratégias de amostragem e antipadrões | Justificativa da amostragem por conglomerados |
| **Wohlin et al. (2012)** | Classificação das ameaças à validade (construto, interna, externa e de conclusão) | Tabela de ameaças |
| **Basili, Caldiera & Rombach (1994)**, GQM | Template de objetivo: *Analisar… com o propósito de… com respeito a… do ponto de vista de… no contexto de…* | Seção 1 do protocolo |
| **Resolução CNS 510/2016** e **LGPD (Lei 13.709/2018)** | Ética em pesquisas com pessoas nas ciências humanas e sociais; proteção de dados | Seção 6 do protocolo |

---

## 2. Tipos de survey (Empirical Standards)

- **Descritivo:** relata as propriedades de um fenômeno ou de uma população. É o caso da nossa QP1.
- **Exploratório:** gera hipóteses e modelos para pesquisas futuras.
- **Confirmatório:** testa proposições formais. É o caso das nossas QP2–QP4, com hipóteses H2a–H4c.

> O padrão **não** cobre questionários com perguntas predominantemente abertas, revisões de literatura nem estudos longitudinais. O nosso estudo é transversal e majoritariamente fechado, portanto se enquadra no padrão.

---

## 3. Processo padrão de um survey

O processo de Kitchenham & Pfleeger (2008) e Linåker et al. (2015) segue as etapas abaixo. A última coluna mostra onde cada etapa aparece no nosso trabalho.

| # | Etapa | Entregável | Onde está no trabalho |
|---|---|---|---|
| 1 | Definir objetivos e questões de pesquisa | Objetivo GQM, QPs e hipóteses | Protocolo, §1 |
| 2 | Definir o que será medido | Construtos, métricas e escalas | Protocolo, Tabela 3 |
| 3 | Definir a população e o quadro amostral | População-alvo, quadro e critérios de exclusão | Protocolo, §2.1–2.2 |
| 4 | Planejar a amostra | Estratégia, tamanho, margem de erro e poder | Protocolo, §2.3 e `scripts/` |
| 5 | Construir o instrumento | Questionário com rastreabilidade | Protocolo, §3 e `instrumento/` |
| 6 | Pré-testar | Registro do pré-teste e mudanças feitas | Protocolo, §4 e `pre-teste/` |
| 7 | Planejar a análise | Limpeza, testes, tamanho de efeito e correções | Protocolo, §5 |
| 8 | Tratar a ética | TCLE, anonimização e armazenamento | Protocolo, §6 e `instrumento/tcle.md` |
| 9 | Avaliar ameaças | Ameaças e mitigações | Protocolo, §7 |
| 10 | Distribuir e monitorar | Canais, cronograma, lembretes e contingência | Protocolo, §8 e `instrumento/convites.md` |
| 11 | Analisar e relatar (Parte 2) | Dashboard e desvios | `DESVIOS.md` (Parte 2) |

> **Princípio de Linåker et al.:** toda pergunta do questionário precisa estar **alinhada a um objetivo de pesquisa**. Se um item não alimenta nenhuma métrica ou QP, ele sai do questionário. Daí a matriz de rastreabilidade.

---

## 4. Pré-registro (Registered Reports, fase RR1)

**O que o pré-registro é:** um plano depositado de forma **verificável e datada** antes da coleta. Ele serve para evitar *HARKing* (formular hipóteses depois de conhecer os resultados), *p-hacking* e viés do pesquisador.

**O protocolo RR1 deve:**
- cumprir os atributos essenciais do General Standard que **não dependem de dados**;
- justificar a importância do problema;
- descrever o método com detalhe suficiente para que um pesquisador independente **replique exatamente** a coleta e a análise;
- conter hipóteses que **possam ser testadas** com os dados que serão coletados;
- *(desejável)* incluir uma **estrutura condicional de análise**, por exemplo "se X, então teste Y". O padrão alerta que omiti-la é "extraordinariamente arriscado".

**O protocolo RR1 não deve:** apresentar resultados, validar pressupostos dos testes com dados reais nem discutir implicações.

**Antipadrões:** desvios *postdictive* (feitos já sabendo como afetam o resultado) e pré-registros **sem carimbo de data verificável**.

**Desvios:** são aceitos se forem **justificados e não motivados pelos dados**. Análises não registradas devem ser rotuladas como **exploratórias**.

> **No nosso trabalho:** o registro datado é feito com tag Git (`protocolo-v1.0`) e envio na plataforma. A análise condicional está no §5.5, e os desvios vão para o `DESVIOS.md`.

---

## 5. Como escrever: convenções textuais

| Convenção | Regra | Exemplo no protocolo |
|---|---|---|
| **Voz** | Impessoal (voz passiva ou partícula *se*), sem "nós achamos" | "Calcula-se o α de Cronbach…" |
| **Tempo verbal** | Futuro ou presente para procedimentos planejados, pois no RR1 nada foi executado ainda | "O pré-teste será aplicado…" |
| **Precisão** | Todo critério deve ser **operacional**, com número, limiar e item de origem | "Duração menor que 1/3 da mediana (E7)" em vez de "respostas rápidas demais" |
| **Identificadores** | IDs estáveis e consistentes em todo o material: QP*n*, H*n*, M*n*, itens (DIF1…) e regras (E1…) | Os mesmos IDs aparecem no protocolo, no codebook e no dashboard |
| **Siglas** | Definidas no primeiro uso | "Ciência da Computação (CC)" |
| **Causalidade** | Estudo transversal só fala em **associação**, nunca em "efeito" ou "causa" | "está associada à…" |
| **Evidência × interpretação** | Na Parte 2, separe resultados (dados) de discussão (interpretação) | Exigência dos Empirical Standards |
| **Limitações** | Declare-as explicitamente e não escreva as conclusões como se elas não existissem | Tabela de ameaças |
| **Citações** | ABNT (NBR 10520): autor-data, com sobrenome em caixa alta entre parênteses | (WATSON; LI, 2014) |
| **Hipóteses** | Bilaterais, com a direção esperada informada à parte | "H3a: ρ ≠ 0 (negativa)" |

---

## 6. Como redigir os itens do questionário

Regras consolidadas de Kitchenham & Pfleeger (2008), dos Empirical Standards e de Linåker et al. (2015):

1. **Uma ideia por item.** Evite perguntas duplas, do tipo "X e Y". *Errado:* "Programar é difícil e cansativo."
2. **Sem negação dupla** e, se possível, sem negação simples.
3. **Redação neutra**, que não induza a resposta. *Errado:* "Você concorda que a IA atrapalha o aprendizado?"
4. **Escalas balanceadas e com todos os pontos rotulados.** Na Likert de 5 pontos, o ponto neutro só é omitido com justificativa.
5. **Opções mutuamente exclusivas e exaustivas**, com "Outro" ou "Prefiro não responder" quando for o caso.
6. **Vocabulário do público-alvo.** Calouros podem não conhecer termos como "complexidade ciclomática".
7. **Cada construto com vários itens**, com 1 item invertido para detectar aquiescência.
8. **Item de atenção** inserido entre itens do mesmo formato.
9. **Itens sensíveis** (reprovação, trabalho) devem oferecer a opção *prefiro não responder*.
10. **Preferir escalas validadas.** Quando a escala for adaptada ou traduzida, cite a origem e verifique a validade (pré-teste e α).
11. **Triagem no início, perguntas abertas no fim.** Perguntas abertas são opcionais e pedem que o respondente não escreva nomes.
12. **Duração máxima de cerca de 10 minutos.** Questionários longos aumentam o abandono e o descuido.

---

## 7. Escala de medição, teste e tamanho de efeito

| Escala | Descritiva | Teste (2 grupos) | Teste (3 ou mais grupos) | Associação | Tamanho de efeito |
|---|---|---|---|---|---|
| **Nominal** | Frequência, % e moda | χ² ou Fisher | χ² | χ² | V de Cramér |
| **Ordinal** (Likert) | Mediana, IIQ e barras divergentes | Mann-Whitney U | Kruskal-Wallis e Dunn | Spearman ρ | δ de Cliff; ε²; ρ |
| **Intervalar/Razão** | Média, DP, mediana e IIQ | *t* de Welch (se os pressupostos valerem) ou Mann-Whitney | ANOVA ou Kruskal-Wallis | Pearson ou Spearman | *d* de Cohen; η²; *r* |

- **Múltiplas comparações:** use Holm-Bonferroni, que é mais poderoso que Bonferroni e controla o erro por família.
- **Margem de erro (95%, pior caso p = 0,5):** e = 1,96·√(p(1−p)/n). Com n = 50, ±13,9 p.p.; com n = 100, ±9,8 p.p.
- **Poder:** informe o menor efeito detectável com o *n* pretendido. O General Standard considera crítica **inválida** exigir um *n* mínimo arbitrário sem análise de poder.
- **Confiabilidade de construtos:** α de Cronbach ≥ 0,70 é adequado; entre 0,60 e 0,70 é aceitável com ressalva.

---

## 8. Design do documento

Decisões de design adotadas no `protocolo.pdf` e por quê:

| Elemento | Decisão | Motivo |
|---|---|---|
| Formato | A4, 10 pt, margens de 1,8 cm, **6 páginas** | Limite do enunciado; densidade parecida com artigos ACM/IEEE |
| Tipografia | Libertinus Serif no corpo e Libertinus Sans nos títulos e cabeçalhos de tabela | Família única e coesa, com boa legibilidade em tamanho pequeno |
| Bloco de abertura | Título, autores, registro e uma **"Ficha do estudo"** em caixa de destaque | O avaliador entende o estudo inteiro em cerca de 10 segundos |
| Tabelas | Estilo *booktabs* (sem linhas verticais), legenda **acima**, faixas de bloco em cinza-azulado | Padrão de publicações científicas; leitura rápida |
| Numeração | Seções 1–8 **idênticas** às 8 seções exigidas pelo enunciado | O avaliador encontra cada critério da rubrica sem procurar |
| Cor | Azul-marinho para estrutura e **laranja apenas para campos pendentes** | A cor tem função; o laranja some quando o grupo preenche tudo |
| Cabeçalho e rodapé | Título curto, disciplina, **versão e data de registro**, "página X de Y" | Rastreabilidade do documento registrado |
| Rastreabilidade | Matriz item → escala → métrica → QP como tabela contínua | É o critério de maior peso na rubrica (0,75 pt) |
| Referências | ABNT, com DOI | Padrão acadêmico brasileiro; verificabilidade |

---

## 9. Checklist rápido antes do envio

- [ ] Todos os campos **laranja** do PDF foram preenchidos (nomes, instituição, N, URL, pré-teste, datas).
- [ ] O PDF tem **até 6 páginas** e o texto não estoura as margens.
- [ ] As 8 seções estão presentes, na ordem do enunciado.
- [ ] A matriz de rastreabilidade cobre **todos** os itens do formulário real.
- [ ] O pré-teste foi feito e a Tabela 6 está preenchida com mudanças **reais**.
- [ ] O formulário está configurado conforme `instrumento/questionario.md` (anônimo, ramificações).
- [ ] Commit e tag `protocolo-v1.0` foram enviados ao GitHub **e** o PDF foi enviado na plataforma até 13/11 às 23:59.
- [ ] O formulário só é aberto **depois** do registro.

---

## 10. Fontes consultadas (13/11/2026)

- ACM SIGSOFT Empirical Standards, Questionnaire Surveys: <https://github.com/acmsigsoft/EmpiricalStandards/blob/master/docs/standards/QuestionnaireSurveys.md>
- ACM SIGSOFT Empirical Standards, General Standard: <https://github.com/acmsigsoft/EmpiricalStandards/blob/master/docs/standards/GeneralStandard.md>
- ACM SIGSOFT Empirical Standards, Registered Reports: <https://github.com/acmsigsoft/EmpiricalStandards/blob/master/docs/supplements/RegisteredReports.md>
- ACM SIGSOFT Empirical Standards, Sampling: <https://github.com/acmsigsoft/EmpiricalStandards/blob/master/docs/supplements/Sampling.md>
- Linåker, J. et al. (2015). *Guidelines for Conducting Surveys in Software Engineering*. Lund University: <https://portal.research.lu.se/en/publications/guidelines-for-conducting-surveys-in-software-engineering/>
- Molléri, J. S.; Petersen, K.; Mendes, E. (2020). DOI: [10.1016/j.infsof.2019.106240](https://doi.org/10.1016/j.infsof.2019.106240)
- Baltes, S.; Ralph, P. (2022). DOI: [10.1007/s10664-021-10072-8](https://doi.org/10.1007/s10664-021-10072-8)
- Kitchenham, B.; Pfleeger, S. L. (2008). DOI: [10.1007/978-1-84800-044-5_3](https://doi.org/10.1007/978-1-84800-044-5_3)
- Resolução CNS nº 510/2016, art. 1º, parágrafo único, I (pesquisa de opinião com participantes não identificados não é registrada no sistema CEP/CONEP). O texto foi confirmado em páginas de CEPs universitários (UFG, UFRN, UFSCar).
- Literatura do tema, com DOIs verificados no Crossref: Watson & Li (2014) [10.1145/2591708.2591749](https://doi.org/10.1145/2591708.2591749); Lahtinen et al. (2005) [10.1145/1067445.1067453](https://doi.org/10.1145/1067445.1067453); Ramalingam & Wiedenbeck (1998) [10.2190/C670-Y3C8-LTJ1-CT3P](https://doi.org/10.2190/C670-Y3C8-LTJ1-CT3P); Tsai et al. (2018) [10.1177/0735633117746747](https://doi.org/10.1177/0735633117746747); Connolly et al. (2009) [10.1109/TE.2008.917193](https://doi.org/10.1109/TE.2008.917193); Robins et al. (2003) [10.1076/csed.13.2.137.14200](https://doi.org/10.1076/csed.13.2.137.14200); Becker et al. (2023) [10.1145/3545945.3569759](https://doi.org/10.1145/3545945.3569759).
