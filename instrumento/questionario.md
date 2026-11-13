# Instrumento de coleta: questionário completo

> **Estudo:** Fatores associados à dificuldade percebida no aprendizado de programação
> **População:** estudantes de CC, ES, ADS e SI de instituições brasileiras, do 1º ao 4º período ou em estágio de TI, com 18 anos ou mais.
> **Versão do instrumento:** 1.0, registrada com o protocolo em 13/11/2026. Mudanças feitas após o pré-teste exigem nova versão e registro em `DESVIOS.md`.
> **Plataforma:** Microsoft Forms (conta institucional), com 37 itens e duração estimada de 9 minutos.
> **Rastreabilidade:** cada ID abaixo é o nome da variável no `codebook.csv` e na Tabela 5 do protocolo.

---

## Configuração obrigatória do formulário

| Configuração | Valor | Motivo |
|---|---|---|
| Quem pode responder | **Qualquer pessoa com o link** | O link circula entre várias instituições e não exige login |
| Registrar nome | **Desativado** | Anonimização na origem (protocolo, §6) |
| Uma resposta por pessoa | **Desativado** (exige login) | Duplicatas são controladas por TRI3 e pela regra E8 |
| Ordem dos itens | Fixa, idêntica para todos | Comparabilidade entre respondentes |
| Itens fechados | Obrigatórios | Ausência só por desenho (protocolo, §5.2) |
| ABR1 | Opcional | Pergunta aberta |
| Ramificação | Conforme as marcações **→ encerra** | Triagem da população |
| Mensagem final | "Obrigado! Sua resposta foi registrada de forma anônima. Se puder, repasse o link a colegas de CC, ES, ADS ou SI." | Bola de neve |

> **Se usarem o Google Forms:** ele não registra a hora de início, então a regra E7 (tempo mínimo) não funciona e precisa ser declarada como desvio.

---

## Página 1: Termo de Consentimento

Exibir o texto integral de [`tcle.md`](tcle.md).

**TRI1.** Li o Termo de Consentimento Livre e Esclarecido e concordo em participar desta pesquisa.
- ( ) Sim, concordo em participar
- ( ) Não concordo → **encerra**

**TRI2.** Você tem 18 anos ou mais?
- ( ) Sim
- ( ) Não → **encerra**

**TRI3.** Você já respondeu a este questionário antes?
- ( ) Não
- ( ) Sim → **encerra** (mensagem: "Obrigado! Cada pessoa responde apenas uma vez.")

---

## Bloco A: Perfil e elegibilidade

**PER1.** Qual é o seu curso?
- ( ) Ciência da Computação
- ( ) Engenharia de Software
- ( ) Análise e Desenvolvimento de Sistemas (ADS)
- ( ) Sistemas de Informação
- ( ) Outro → **encerra**

**PER2.** Em qual período você está? (Se cursa disciplinas de períodos diferentes, considere o período da maioria delas.)
- ( ) 1º  ( ) 2º  ( ) 3º  ( ) 4º  ( ) 5º ou posterior

**PER3.** Você faz estágio na área de TI atualmente?
- ( ) Sim
- ( ) Não → se PER2 = *5º ou posterior*, **encerra** (mensagem: "Obrigado! Este estudo é voltado a estudantes do 1º ao 4º período ou em estágio de TI.")

> No Microsoft Forms, faça a ramificação assim: PER2 = 5º ou posterior leva a uma seção com a pergunta PER3 em que "Não" encerra. PER2 = 1º a 4º leva a uma seção com PER3 sem encerramento.

**PER4.** Sua instituição de ensino é:
- ( ) Pública  ( ) Privada

**PER5.** Por onde você recebeu este convite?
- ( ) Professor(a) ou aula
- ( ) Grupo de WhatsApp, Discord ou Telegram
- ( ) Centro ou diretório acadêmico
- ( ) LinkedIn ou Instagram
- ( ) Indicação de colega
- ( ) Outro

**PER6.** Faixa etária:
- ( ) 18–19  ( ) 20–22  ( ) 23–25  ( ) 26–30  ( ) 31 ou mais

**PER7.** Antes de ingressar no curso, você já havia programado (em curso livre, ensino técnico, sozinho etc.)?
- ( ) Sim  ( ) Não (se *Não*, pular PER8)

**PER8.** Por quanto tempo você programou antes de ingressar no curso?
- ( ) Menos de 6 meses  ( ) De 6 meses a 1 ano  ( ) De 1 a 2 anos  ( ) Mais de 2 anos

**PER9.** Você cursou ensino médio técnico em informática ou área afim?
- ( ) Sim  ( ) Não

**PER10.** Você já teve reprovação em alguma disciplina de programação neste curso?
- ( ) Sim  ( ) Não  ( ) Prefiro não responder

---

## Bloco B: Dificuldade percebida (construto DIF)

*Instrução:* "Pensando em todo o seu aprendizado de programação até agora, indique o quanto concorda com cada afirmação."

Escala (todos os pontos rotulados): **1** Discordo totalmente · **2** Discordo · **3** Nem concordo nem discordo · **4** Concordo · **5** Concordo totalmente

| ID | Afirmação |
|---|---|
| DIF1 | Tenho dificuldade para compreender novos conceitos de programação. |
| DIF2 | Tenho dificuldade para transformar a lógica de uma solução em código. |
| DIF3 | Com frequência, não sei por onde começar a resolver um problema de programação. |
| DIF4 ᴿ | Consigo acompanhar o ritmo das disciplinas de programação sem grandes dificuldades. *(codificação invertida: 6 − x)* |

> DIF1 e DIF2 vieram da versão preliminar do grupo. Os itens dessa versão sobre depuração e sobre resolver exercícios sem ajuda ficaram de fora porque repetem AUT2 e AUT4. Mantê-los inflaria artificialmente a correlação testada em H3a.

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

*Instrução:* "Pensando nas suas habilidades de programação hoje, indique o quanto concorda." A escala é a mesma do Bloco B.

| ID | Afirmação |
|---|---|
| AUT1 | Consigo escrever um programa que resolva um problema simples proposto em aula. |
| AUT2 | Consigo localizar e corrigir erros em um programa de minha autoria. |
| AUT3 | Consigo entender um programa escrito por outra pessoa, de complexidade compatível com a disciplina. |
| ATN1 | **Para confirmar que você está lendo com atenção, marque "Discordo totalmente" nesta linha.** |
| AUT4 | Consigo concluir um exercício de programação sem ajuda de colegas, monitores ou ferramentas de IA. |

> A resposta correta de ATN1 é **1**. Qualquer outro valor descarta a resposta pela regra **E5**.

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

**HAB1.** Em uma semana típica deste semestre, quantas horas você dedica a programar **fora do horário de aula e do estágio**? (número inteiro de 0 a 40)

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

**ABR1.** Na sua opinião, o que mais dificulta, ou o que mais ajudou, o seu aprendizado de programação? *(Não escreva nomes de pessoas, professores ou instituições.)*

---

## Origem dos itens

| Construto | Base | Adaptação |
|---|---|---|
| DIF | Elaborado pelo grupo (DIF1 e DIF2 vêm da versão preliminar), com base em Robins, Rountree e Rountree (2003) e Lahtinen, Ala-Mutka e Järvinen (2005) | Validade de conteúdo verificada no pré-teste com especialista |
| TOP | Lista de tópicos de Lahtinen, Ala-Mutka e Järvinen (2005) | Tradução livre; tópicos ajustados às ementas iniciais |
| AUT | Ramalingam e Wiedenbeck (1998); Tsai, Wang e Hsu (2018) | Tradução livre e redução para 4 itens |
| ANS | Connolly, Murphy e Moore (2009) | Tradução livre e redução para 3 itens |
