# Lista de requisitos do protocolo (Parte 1) e matriz de conformidade

> **Para que serve:** listar **tudo o que o protocolo precisa atender**, juntando o enunciado da disciplina e os padrões científicos internacionais, e mostrar **onde** cada requisito é atendido.
> **Como ler:** cada requisito tem um ID estável, uma fonte, uma prioridade, o local em que é atendido e um status.

**Prioridade**
- **OBR (obrigatório):** exigido pelo enunciado ou atributo *essencial* dos Empirical Standards.
- **DES (desejável):** atributo *desejável* dos Empirical Standards, que diferencia um trabalho bom de um excelente.

**Status**
- ✅ Atendido no material entregue.
- ⏳ **Pendente do grupo:** depende de informação ou ação que só o grupo tem, por exemplo nomes, pré-teste ou dados da coordenação.
- 🔜 **Parte 2:** planejado agora e executado depois da coleta.

---

## A. Requisitos do enunciado (Parte 1)

### A.1 Forma de entrega

| ID | Requisito | Prioridade | Onde | Status |
|---|---|---|---|---|
| RE-01 | Protocolo em **PDF** | OBR | `protocolo/protocolo.pdf` | ✅ |
| RE-02 | **Até 6 páginas** | OBR | PDF com exatamente 6 páginas | ✅ (reconferir após preencher) |
| RE-03 | As **8 seções** na ordem pedida | OBR | Seções 1–8 do PDF | ✅ |
| RE-04 | Data de entrega **comprovada** e **anterior à 1ª resposta** | OBR | Tag `protocolo-v1.0` no GitHub e envio na plataforma (13/11); coleta a partir de 18/11 | ⏳ fazer o commit e o envio |

### A.2 Seção 1: Objetivo e questões de pesquisa

| ID | Requisito | Prioridade | Onde | Status |
|---|---|---|---|---|
| RE-05 | Objetivo no **template GQM** | OBR | Tabela 1 | ✅ |
| RE-06 | **De 2 a 4** questões de pesquisa | OBR | Tabela 2 (QP1–QP4) | ✅ |

### A.3 Seção 2: População e amostragem

| ID | Requisito | Prioridade | Onde | Status |
|---|---|---|---|---|
| RE-07 | População-alvo definida | OBR | §2.1 | ✅ |
| RE-08 | Origem dos contatos | OBR | §2.2 (quadro de turmas da coordenação) | ✅ |
| RE-09 | Estratégia de amostragem (probabilística, conveniência ou bola de neve) | OBR | §2.2: probabilística estratificada por conglomerados | ✅ |
| RE-10 | Tamanho de amostra pretendido | OBR | §2.3: 100 respostas (mínimo 50) | ✅ |
| RE-11 | Margem de erro correspondente | OBR | Tabela 4: ±9,8 p.p. | ✅ |
| RE-12 | Justificativa de estudantes como população | OBR (§05 do enunciado) | §2.1 | ✅ |
| RE-13 | Colegas da turma não contam como amostra | OBR (§05) | §2.1 (exclusão de MEES e do grupo) | ✅ |
| RE-14 | Tamanho da população N | OBR | §2.1, onde N ≈ 400 é uma estimativa | ⏳ confirmar com a coordenação |

### A.4 Seção 3: Questionário com rastreabilidade

| ID | Requisito | Prioridade | Onde | Status |
|---|---|---|---|---|
| RE-15 | Cada item ligado a **uma QP e uma métrica** | OBR | Tabela 5 | ✅ |
| RE-16 | **Escala declarada** por item (nominal, ordinal, intervalar ou razão) | OBR | Tabela 5, coluna *Escala* | ✅ |
| RE-17 | Construtos medidos por **mais de um item** | OBR | DIF (4), AUT (4), ANS (3) | ✅ |
| RE-18 | **Pergunta de atenção** | OBR | ATN1 + regra E5 | ✅ |

### A.5 Seção 4: Pré-teste

| ID | Requisito | Prioridade | Onde | Status |
|---|---|---|---|---|
| RE-19 | Aplicação do questionário a **3 a 5 pessoas** | OBR | §4 + `pre-teste/roteiro-pre-teste.md` | ⏳ **aplicar hoje** |
| RE-20 | **Mudanças feitas** a partir do pré-teste | OBR | Tabela 6 | ⏳ preencher com resultados reais |

### A.6 Seção 5: Plano de análise

| ID | Requisito | Prioridade | Onde | Status |
|---|---|---|---|---|
| RE-21 | Estatística descritiva | OBR | §5.4 | ✅ |
| RE-22 | Testes **coerentes com as escalas** | OBR | Tabela 8 (Mann-Whitney, χ², Spearman, Kruskal-Wallis) | ✅ |
| RE-23 | **Tamanho de efeito** | OBR | Tabela 8 (δ de Cliff, V de Cramér, ρ, ε²) | ✅ |
| RE-24 | **Correção para múltiplas comparações** | OBR | §5.5 (Holm) | ✅ |
| RE-25 | Codificação das **respostas abertas** | OBR | §5.6 (análise temática, κ de Cohen) | ✅ |

### A.7 Seção 6: Ética e LGPD

| ID | Requisito | Prioridade | Onde | Status |
|---|---|---|---|---|
| RE-26 | Termo de consentimento | OBR | §6 + `instrumento/tcle.md` | ✅ (preencher contatos) |
| RE-27 | Anonimização | OBR | §6 | ✅ |
| RE-28 | Forma de armazenamento | OBR | §6 | ✅ (confirmar a data de exclusão) |
| RE-29 | Seguir as orientações da instituição sobre pesquisa com pessoas | OBR (§05) | §6 | ⏳ confirmar com o professor se há norma local |

### A.8 Seção 7: Ameaças à validade

| ID | Requisito | Prioridade | Onde | Status |
|---|---|---|---|---|
| RE-30 | Ameaças típicas: **não resposta, autosseleção, desejabilidade social** e outras | OBR | Tabela 9 (10 ameaças) | ✅ |
| RE-31 | Como cada ameaça será mitigada | OBR | Tabela 9, coluna *Mitigação* | ✅ |

### A.9 Seção 8: Plano de divulgação

| ID | Requisito | Prioridade | Onde | Status |
|---|---|---|---|---|
| RE-32 | Canais que serão usados | OBR | §8 (C1–C3) + `instrumento/convites.md` | ✅ |
| RE-33 | Período de coleta | OBR | Tabela 10 (18/11 a 04/12) | ✅ |

### A.10 Requisitos da Parte 2 que o protocolo já prepara

| ID | Requisito (Parte 2) | Onde foi preparado | Status |
|---|---|---|---|
| RE-P2-01 | Mínimo de **50 respostas válidas** | Alvo 100 + contingência (§8) | 🔜 |
| RE-P2-02 | Dashboard **lê os dados brutos** | §5.7 + `codebook.csv` | 🔜 |
| RE-P2-03 | Respostas descartadas **com o motivo** | Tabela 7 (E1–E8) | 🔜 |
| RE-P2-04 | Likert em **barras divergentes** | §5.4 | 🔜 |
| RE-P2-05 | QP respondida com teste, *p*, efeito e margem | §5.5 e Tabela 8 | 🔜 |
| RE-P2-06 | **Filtros por segmento** | M8 (período), M10 (curso), M3 (experiência); supressão de n < 5 | 🔜 |
| RE-P2-07 | **α de Cronbach** dos construtos | §5.3 | 🔜 |
| RE-P2-08 | Página de **metodologia e desvios** | `DESVIOS.md` | 🔜 |
| RE-P2-09 | **Evidências** da coleta: exportação bruta datada e capturas dos canais | `convites.md` (capturas do slide) e cronograma (exportação em 04/12) | 🔜 |

---

## B. ACM SIGSOFT Empirical Standards: Questionnaire Surveys

### B.1 Atributos essenciais (aplicáveis antes da coleta)

| ID | Atributo | Prioridade | Onde | Status |
|---|---|---|---|---|
| ES-01 | Identifica a população-alvo e define a estratégia de amostragem | OBR | §2 | ✅ |
| ES-02 | Descreve como o instrumento foi criado | OBR | §3 + quadro "Origem dos itens" em `questionario.md` | ✅ |
| ES-03 | Descreve como os participantes são selecionados e recrutados | OBR | §2.2 + §8 | ✅ |
| ES-04 | Usa escalas validadas **ou** analisa a validade de construto *ex post* | OBR | AUT e ANS adaptadas de escalas validadas; DIF com validade de conteúdo no pré-teste e α *ex post* | ✅ |
| ES-05 | Descreve o monitoramento das respostas e a contingência para não resposta | OBR | §8 (lembretes e contingência) | ✅ |
| ES-06 | Explica o tratamento de dados ausentes | OBR | §5.2 | ✅ |
| ES-07 | Descrição passo a passo, sistemática e **replicável** da coleta e da análise | OBR | Script com semente, regras E1–E8 e Tabela 8 | ✅ |
| ES-08 | Analisa a taxa de resposta | OBR | Planejada por turma (§5.1) | 🔜 |
| ES-09 | Avalia a suficiência do número de participantes (poder) | OBR | Tabela 4 | ✅ |
| ES-10 | Reconhece ameaças à generalização | OBR | Tabela 9 | ✅ |
| ES-11 | Disponibiliza o instrumento | OBR | `instrumento/questionario.md` | ✅ |
| ES-12 | O desenho do questionário corresponde aos objetivos e à população | OBR | Matriz de rastreabilidade + pré-teste | ✅ |

### B.2 Atributos desejáveis

| ID | Atributo | Onde | Status |
|---|---|---|---|
| ES-D01 | Materiais suplementares: instrumento, livro de códigos, scripts e dados | `instrumento/`, `scripts/` | ✅ |
| ES-D02 | Mecanismo para detectar respostas automatizadas ou geradas por IA | E7 (tempo), ATN1, inspeção de ABR1 | ✅ |
| ES-D03 | Itens de atenção, com exclusão de quem falhar | ATN1 / E5 | ✅ |
| ES-D04 | Caracteriza a população-alvo | §2.1 + bloco PER | ✅ |
| ES-D05 | Considera princípios de ética em pesquisa | §6 | ✅ |
| ES-D06 | Justifica o desenho do instrumento e a escolha das escalas | §3 | ✅ |
| ES-D07 | Valida itens, layout, duração e tecnologia (piloto) | §4 | ⏳ |
| ES-D08 | Relata como o instrumento evoluiu na validação | Tabela 6 | ⏳ |
| ES-D09 | Aplica técnicas para aumentar a taxa de resposta | Aplicação presencial + 2 lembretes | ✅ |
| ES-D10 | Descreve a estratificação da análise | §2.2 + análise condicional (§5.5) | ✅ |
| ES-D11 | Define e estima o tamanho dos estratos | `quadro_turmas` (coordenação) | ⏳ |
| ES-D12 | Distingue evidência de interpretação | Exigência para a Parte 2 | 🔜 |

---

## C. Registered Reports (fase RR1)

| ID | Atributo | Prioridade | Onde | Status |
|---|---|---|---|---|
| RR-01 | Não apresenta resultados nem implicações | OBR | Todo o PDF | ✅ |
| RR-02 | Justifica a importância do problema | OBR | §1, parágrafo de contexto | ✅ |
| RR-03 | Método detalhado para **replicação exata** | OBR | §2–§5 + script | ✅ |
| RR-04 | Hipóteses testáveis com os dados planejados | OBR | Tabela 2 × Tabela 5 | ✅ |
| RR-05 | Estrutura condicional de análise | DES | §5.5 (i)–(iii) | ✅ |
| RR-06 | Registro com **carimbo de data verificável** | OBR | Tag Git + envio na plataforma | ⏳ |
| RR-07 | Política de desvios | DES | Ficha do estudo + `DESVIOS.md` | ✅ |

---

## D. Suplemento de amostragem (Sampling)

| ID | Atributo | Onde | Status |
|---|---|---|---|
| SA-01 | Explica o objetivo da amostragem (representatividade na instituição) | §2.2 | ✅ |
| SA-02 | Explica a estratégia e as etapas de filtragem | §2.2 + TRI/PER | ✅ |
| SA-03 | Justifica por que a estratégia é razoável | §2.2 (turma como conglomerado natural) | ✅ |
| SA-04 | Informa o tamanho da amostra | §2.3 | ✅ |
| SA-05 | Define a população teórica | §2.1 | ✅ |
| SA-06 | Fornece um relato **algorítmico** e replicável de como obter a mesma amostra | `scripts/sorteio_turmas.py` (semente 20261113) | ✅ |
| SA-07 | Argumenta a representatividade (IC e margem) | Tabela 4 | ✅ |
| SA-08 | Explica como a amostra pode ser enviesada | Tabela 9 | ✅ |
| SA-09 | Informa o tamanho da população e do quadro amostral | §2.1 (N estimado) | ⏳ |

---

## E. Pendências do grupo, consolidadas e em ordem

| # | Ação | Requisitos | Prazo |
|---|---|---|---|
| 1 | Preencher **nomes, instituição e URL do repositório** no PDF e no TCLE | — | 13/11 |
| 2 | Confirmar **N** e a lista de turmas com a coordenação (ou estimar pelo quadro de horários) | RE-14, ES-D11, SA-09 | 13/11 |
| 3 | Montar o formulário conforme `instrumento/questionario.md` | — | 13/11 |
| 4 | **Aplicar o pré-teste** (3–5 pessoas) e registrar as mudanças **reais** | RE-19, RE-20, ES-D07, ES-D08 | 13/11 |
| 5 | Atualizar a Tabela 6 e a mediana de duração; recompilar o PDF (≤ 6 páginas) | RE-02 | 13/11 |
| 6 | Confirmar com o professor se há norma institucional adicional (CEP) | RE-29 | 13/11 |
| 7 | **Commit + tag `protocolo-v1.0` + push** e **envio do PDF na plataforma** | RE-04, RR-06 | **13/11 às 23:59** |
| 8 | Rodar o sorteio com o quadro real e publicar `turmas_sorteadas.csv` | ES-07 | 16/11 |
