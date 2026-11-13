# Instrumento de coleta: questionário completo

> **Estudo:** Fatores associados à dificuldade percebida no aprendizado de programação
> **Versão do instrumento:** 1.0, registrada com o protocolo em 13/11/2026. Mudanças feitas após o pré-teste exigem nova versão e registro em `DESVIOS.md`.
> **Plataforma:** Microsoft Forms (conta institucional), com 36 itens e duração estimada de 9 minutos.
> **Rastreabilidade:** cada ID abaixo é o nome da variável no `codebook.csv` e na matriz da Tabela 5 do protocolo.

---

## Configuração obrigatória do formulário

| Configuração | Valor | Motivo |
|---|---|---|
| Quem pode responder | **Qualquer pessoa com o link** | Evita login e, portanto, a identificação do respondente |
| Registrar nome | **Desativado** | Anonimização na origem (protocolo, §6) |
| Uma resposta por pessoa | **Desativado** (exige login) | Duplicatas são controladas por TRI3 e pela regra E8 |
| Ordem dos itens | Fixa, idêntica para todos | Comparabilidade entre respondentes |
| Itens fechados | Obrigatórios | Ausência só por desenho (protocolo, §5.2) |
| ABR1 | Opcional | Pergunta aberta, sem obrigatoriedade |
| Ramificação | Conforme as marcações **→ encerra** | Triagem da população |
| Mensagem de agradecimento | "Obrigado! Sua resposta foi registrada de forma anônima." | — |

---

## Página 1: Termo de Consentimento

Exibir o texto integral de [`tcle.md`](tcle.md).

**TRI1.** Li o Termo de Consentimento Livre e Esclarecido e concordo em participar desta pesquisa.
- ( ) Sim, concordo em participar
- ( ) Não concordo → **encerra**

**TRI2.** Você tem 18 anos ou mais?
- ( ) Sim
- ( ) Não → **encerra**

**TRI3.** Você já respondeu a este questionário em outra turma?
- ( ) Não
- ( ) Sim → **encerra** (mensagem: "Obrigado! Cada pessoa responde apenas uma vez.")

---

## Bloco A: Perfil

**PER1.** Qual é o seu curso?
- ( ) Ciência da Computação
- ( ) Engenharia de Software
- ( ) Outro → **encerra**

**PER2.** Em qual período você está? (Se cursa disciplinas de períodos diferentes, considere o período da maioria delas.)
- ( ) 1º  ( ) 2º  ( ) 3º  ( ) 4º
- ( ) 5º ou posterior → **encerra**

**PER3.** Código da turma em que você recebeu este convite (informado pela equipe no slide ou na mensagem):
- Lista suspensa: `T01` … `Tnn` (preencher após o sorteio) | ( ) Recebi o link por outro meio

**PER4.** Faixa etária:
- ( ) 18–19  ( ) 20–22  ( ) 23–25  ( ) 26–30  ( ) 31 ou mais

**PER5.** Antes de ingressar no curso, você já havia programado (em curso livre, ensino técnico, sozinho etc.)?
- ( ) Sim  ( ) Não (se *Não*, pular PER6)

**PER6.** Por quanto tempo você programou antes de ingressar no curso?
- ( ) Menos de 6 meses  ( ) De 6 meses a 1 ano  ( ) De 1 a 2 anos  ( ) Mais de 2 anos

**PER7.** Você cursou ensino médio técnico em informática ou área afim?
- ( ) Sim  ( ) Não

**PER8.** Qual é a sua situação de trabalho atual?
- ( ) Não trabalho  ( ) Estágio  ( ) Trabalho até 30 horas semanais  ( ) Trabalho mais de 30 horas semanais

**PER9.** Você já teve reprovação em alguma disciplina de programação neste curso?
- ( ) Sim  ( ) Não  ( ) Prefiro não responder

---

## Bloco B: Dificuldade percebida (construto DIF)

*Instrução:* "Pensando nas disciplinas de programação que você cursou ou está cursando, indique o quanto concorda com cada afirmação."

Escala (todos os pontos rotulados): **1** Discordo totalmente · **2** Discordo · **3** Nem concordo nem discordo · **4** Concordo · **5** Concordo totalmente

| ID | Afirmação |
|---|---|
| DIF1 | Aprender a programar tem sido difícil para mim. |
| DIF2 | Costumo precisar de muito mais tempo do que o previsto para resolver exercícios de programação. |
| DIF3 | Com frequência, não sei por onde começar a resolver um problema de programação. |
| DIF4 ᴿ | Consigo acompanhar o ritmo das disciplinas de programação sem grandes dificuldades. *(codificação invertida: 6 − x)* |

---

## Bloco C: Dificuldade por tópico (TOP)

*Instrução:* "Quão difícil foi (ou está sendo) para você aprender cada tópico abaixo? Se ainda não estudou o tópico, marque *Ainda não estudei*."

Escala: **1** Muito fácil · **2** Fácil · **3** Moderado · **4** Difícil · **5** Muito difícil · **NA** Ainda não estudei

| ID | Tópico |
|---|---|
| TOP1 | Estruturas condicionais (if/else, switch) |
| TOP2 | Estruturas de repetição (for, while) |
| TOP3 | Vetores e matrizes |
| TOP4 | Funções/métodos e passagem de parâmetros |
| TOP5 | Recursão |
| TOP6 | Ponteiros, referências e gerenciamento de memória |
| TOP7 | Depuração (localizar e corrigir erros) |
| TOP8 | Orientação a objetos (classes, herança, polimorfismo) |

---

## Bloco D: Autoeficácia em programação (construto AUT) e verificação de atenção

*Instrução:* "Pensando nas disciplinas de programação que você cursa agora, indique o quanto concorda." A escala é a mesma do Bloco B.

| ID | Afirmação |
|---|---|
| AUT1 | Consigo escrever um programa que resolva um problema simples proposto em aula. |
| AUT2 | Consigo localizar e corrigir erros em um programa de minha autoria. |
| AUT3 | Consigo entender um programa escrito por outra pessoa, de complexidade compatível com a disciplina. |
| ATN1 | **Para confirmar que você está lendo com atenção, marque "Discordo totalmente" nesta linha.** |
| AUT4 | Consigo concluir um exercício de programação sem ajuda de colegas, monitores ou ferramentas de IA. |

> ATN1 fica entre os itens AUT para não ser percebida como pergunta isolada. A resposta correta é **1**, e qualquer outro valor descarta a resposta pela regra **E5**.

---

## Bloco E: Ansiedade em programação (construto ANS)

A escala é a mesma do Bloco B.

| ID | Afirmação |
|---|---|
| ANS1 | Sinto nervosismo quando preciso programar em provas ou atividades avaliativas. |
| ANS2 | Sinto desânimo quando meu código apresenta erros que não consigo resolver. |
| ANS3 | Evito iniciar tarefas de programação por receio de não conseguir concluí-las. |

---

## Bloco F: Hábitos de estudo

**HAB1.** Em uma semana típica deste semestre, quantas horas você dedica a programar **fora do horário de aula**? (número inteiro de 0 a 40)

**HAB2.** Com que frequência você usa assistentes de IA generativa (por exemplo, ChatGPT, GitHub Copilot, Gemini) ao estudar programação?
- ( ) 1 Nunca  ( ) 2 Raramente  ( ) 3 Às vezes  ( ) 4 Frequentemente  ( ) 5 Sempre

**HAB3.** Quando usa IA ao estudar programação, qual é o **principal** uso?
- ( ) Obter código pronto para a tarefa
- ( ) Entender conceitos ou mensagens de erro
- ( ) Revisar ou melhorar o meu próprio código
- ( ) Outro
- ( ) Não uso IA

---

## Bloco G: Questão aberta (opcional)

**ABR1.** Na sua opinião, o que mais dificulta, ou o que mais ajudou, o seu aprendizado de programação? *(Não escreva nomes de pessoas, professores ou turmas.)*

---

## Origem dos itens

| Construto | Base | Adaptação |
|---|---|---|
| DIF | Elaborado pelo grupo, com base em Robins, Rountree e Rountree (2003) e Lahtinen, Ala-Mutka e Järvinen (2005) | Validade de conteúdo verificada no pré-teste com especialista |
| TOP | Lista de tópicos de Lahtinen, Ala-Mutka e Järvinen (2005) | Tradução livre; tópicos ajustados às ementas dos períodos iniciais |
| AUT | Ramalingam e Wiedenbeck (1998); Tsai, Wang e Hsu (2018) | Tradução livre e redução para 4 itens |
| ANS | Connolly, Murphy e Moore (2009) | Tradução livre e redução para 3 itens |
