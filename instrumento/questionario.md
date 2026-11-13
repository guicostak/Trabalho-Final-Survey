# Instrumento de coleta: questionário enxuto (5 perguntas)

> **Estudo:** Fatores associados à dificuldade percebida no aprendizado de programação
> **População:** estudantes de CC, ES, ADS e SI de instituições brasileiras, do 1º ao 4º período ou em estágio de TI, com 18 anos ou mais.
> **Versão:** 1.0, registrada com o protocolo em 13/11/2026. Mudanças após o pré-teste exigem nova versão e registro em `DESVIOS.md`.
> **Plataforma:** Microsoft Forms (conta PUC Minas), formulário "Experiência de estudantes com o aprendizado de programação". Já está montado e configurado; ainda não foi divulgado.
> **Estrutura:** aceite (porteira), **5 perguntas** e 1 pergunta aberta opcional. Duração estimada: **cerca de 2 minutos**.
> **Rastreabilidade:** cada ID abaixo é o nome da variável no `codebook.csv` e na Tabela 5 do protocolo.

---

## Configuração aplicada no Microsoft Forms

| Configuração | Valor | Motivo |
|---|---|---|
| Quem pode responder | **Qualquer pessoa pode responder** (resposta anônima, sem login) | O link circula entre várias instituições; anonimização na origem |
| Registro de nome e e-mail | **Não coletado** | Protocolo, §6 |
| Ocultar "Enviar outra resposta" | **Ativado** | Reduz duplicatas (regra E6) |
| Mensagem de agradecimento | "Obrigado! Sua resposta foi registrada de forma anônima. Se puder, repasse o link a colegas de CC, ES, ADS ou SI (1º ao 4º período ou em estágio de TI)." | Bola de neve |
| Perguntas fechadas | Obrigatórias | Ausência só na aberta |
| Pergunta aberta | Opcional, resposta longa | Não prejudica a adesão |
| Ramificação | Conforme as marcações **→ encerra** | Triagem da população |

> **Título do formulário (neutro):** "Experiência de estudantes com o aprendizado de programação". O título evita a palavra "dificuldade" para não induzir autosseleção.
> **Descrição:** texto do TCLE em [`tcle.md`](tcle.md), na versão resumida exibida no formulário.

---

## Aceite (porteira, antes das perguntas)

**ACE.** Li o termo acima, tenho 18 anos ou mais e concordo em participar desta pesquisa.
- ( ) Sim, concordo em participar
- ( ) Não concordo → **encerra**

## Pergunta 1: curso

**CUR.** Qual é o seu curso?
- ( ) Ciência da Computação
- ( ) Engenharia de Software
- ( ) Análise e Desenvolvimento de Sistemas (ADS)
- ( ) Sistemas de Informação
- ( ) Outro → **encerra**

## Pergunta 2: etapa do curso

**ETA.** Em que etapa do curso você está? (Se cursa disciplinas de períodos diferentes, considere o período da maioria delas.)
- ( ) 1º ao 4º período
- ( ) 5º período ou posterior, fazendo estágio em TI
- ( ) 5º período ou posterior, sem estágio → **encerra**

## Pergunta 3: experiência prévia

**EXP.** Antes de ingressar no curso, você já havia programado (em curso livre, ensino técnico, sozinho etc.)?
- ( ) Sim
- ( ) Não

## Pergunta 4: grade Likert (construto DIF e verificação de atenção)

*Enunciado:* "Pensando em todo o seu aprendizado de programação até agora, indique o quanto você concorda com cada afirmação."

Colunas: **1** Discordo totalmente · **2** Discordo · **3** Nem concordo nem discordo · **4** Concordo · **5** Concordo totalmente

| ID | Linha da grade |
|---|---|
| DIF1 | Tenho dificuldade para compreender novos conceitos de programação. |
| DIF2 | Tenho dificuldade para transformar a lógica de uma solução em código. |
| DIF3 | Com frequência, não sei por onde começar a resolver um problema de programação. |
| DIF4 ᴿ | Consigo acompanhar o ritmo das disciplinas de programação sem grandes dificuldades. *(codificação invertida: 6 − x)* |
| ATN1 | **Para confirmar que você está lendo com atenção, marque "Discordo totalmente" nesta linha.** *(correta = 1; qualquer outra resposta descarta pela regra E3)* |

## Pergunta 5: uso de IA generativa

**IAF.** Com que frequência você usa assistentes de IA generativa (por exemplo, ChatGPT, GitHub Copilot, Gemini) ao estudar programação?
- ( ) Nunca  ( ) Raramente  ( ) Às vezes  ( ) Frequentemente  ( ) Sempre

## Pergunta aberta (opcional)

**ABR.** (Opcional) Na sua opinião, o que mais dificulta, ou o que mais ajudou, o seu aprendizado de programação? Não escreva nomes de pessoas, professores ou instituições.

---

## Por que 5 perguntas

Formulários longos têm adesão menor, sobretudo quando o link é aberto e a participação é voluntária. A versão enxuta mantém o que o enunciado exige:
- um **construto medido por vários itens**: DIF, com 4 itens, um deles invertido;
- uma **pergunta de atenção** (ATN1);
- variáveis em **várias escalas**: nominal (CUR, ETA, EXP), ordinal (DIF, IAF) e texto codificado (ABR);
- testes que cobrem os exemplos do enunciado: Mann-Whitney, Kruskal-Wallis, χ² e Spearman.

Ficaram de fora autoeficácia, ansiedade, tópicos e horas de estudo. Essa limitação está declarada no protocolo (Tabela 9, "Fatores não medidos").

## Origem dos itens

| Item | Base |
|---|---|
| DIF1, DIF2 | Versão preliminar do grupo, com base em Robins, Rountree e Rountree (2003) e Lahtinen, Ala-Mutka e Järvinen (2005) |
| DIF3, DIF4 | Elaborados pelo grupo; validade de conteúdo a verificar no pré-teste com especialista |
| EXP | Fator de entrada descrito em Robins, Rountree e Rountree (2003) |
| IAF | Contexto de IA generativa no ensino (Becker et al., 2023) |
