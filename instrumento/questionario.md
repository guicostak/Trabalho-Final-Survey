# Instrumento de coleta: aprendizado de programação na era da IA generativa

> **Estudo:** Aprendizado de programação na era da IA generativa: uso, dependência e aprendizado percebido entre estudantes de tecnologia
> **População:** estudantes de CC, ES, ADS e SI de instituições brasileiras, do 1º ao 4º período ou em estágio de TI, com 18 anos ou mais.
> **Versão:** 1.0, registrada com o protocolo em 13/11/2026. Mudanças após o pré-teste exigem nova versão e registro em `DESVIOS.md`.
> **Plataforma:** Microsoft Forms (conta PUC Minas), formulário "Experiência de estudantes com o aprendizado de programação". Já está montado e configurado; ainda não foi divulgado.
> **Link de resposta:** https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=ZIEqXraHC0OsawjWIp5wWbdFJRrrPlxBl43UGrMMybJUMVhBRFFDVDM3VzRRQkgzSjBLUlU5QTU2Ti4u
> **Estrutura:** aceite (porteira) e **10 perguntas**, a última aberta e opcional. Duração estimada: **cerca de 4 minutos**.
> **Rastreabilidade:** cada ID abaixo é o nome da variável no `codebook.csv` e na Tabela 5 do protocolo.

---

## Configuração aplicada no Microsoft Forms

| Configuração | Valor | Motivo |
|---|---|---|
| Quem pode responder | **Qualquer pessoa** (resposta anônima, sem login) | Link aberto a várias instituições; anonimização na origem |
| Nome e e-mail | **Não coletados** | Protocolo, §6 |
| Ocultar "Enviar outra resposta" | **Ativado** | Reduz duplicatas (regra E6) |
| Mensagem de agradecimento | Pede para repassar o link a colegas de CC, ES, ADS ou SI | Bola de neve |
| Perguntas fechadas | Obrigatórias | Ausência só por ramificação e na aberta |
| Título | "Experiência de estudantes com o aprendizado de programação" (neutro) | Evita autosseleção por interesse em IA |

### Ramificações

| Pergunta | Resposta | Vai para |
|---|---|---|
| Aceite | Não concordo | Fim do formulário |
| 1 (curso) | Outro | Fim do formulário |
| 2 (etapa) | 5º período ou posterior, sem estágio | Fim do formulário |
| 5 (frequência de IA) | Nunca | Pergunta 10 (aberta) |

---

## Aceite (porteira)

**ACE.** Li o termo acima, tenho 18 anos ou mais e concordo em participar desta pesquisa.
- ( ) Sim, concordo em participar
- ( ) Não concordo → **encerra**

## Perguntas 1 a 3: perfil e elegibilidade

**CUR.** Qual é o seu curso? — Ciência da Computação · Engenharia de Software · Análise e Desenvolvimento de Sistemas (ADS) · Sistemas de Informação · Outro → **encerra**

**ETA.** Em que etapa do curso você está? (Se cursa disciplinas de períodos diferentes, considere o período da maioria delas.) — 1º ao 4º período · 5º período ou posterior, fazendo estágio em TI · 5º período ou posterior, sem estágio → **encerra**

**EXP.** Antes de ingressar no curso, você já havia programado (em curso livre, ensino técnico, sozinho etc.)? — Sim · Não

## Pergunta 4: grade de dificuldade percebida (DIF) e verificação de atenção

*Enunciado:* "Pensando em todo o seu aprendizado de programação até agora, indique o quanto você concorda com cada afirmação."
Colunas: 1 Discordo totalmente · 2 Discordo · 3 Nem concordo nem discordo · 4 Concordo · 5 Concordo totalmente

| ID | Linha |
|---|---|
| DIF1 | Tenho dificuldade para compreender novos conceitos de programação. |
| DIF2 | Tenho dificuldade para transformar a lógica de uma solução em código. |
| DIF3 | Com frequência, não sei por onde começar a resolver um problema de programação. |
| DIF4 ᴿ | Consigo acompanhar o ritmo das disciplinas de programação sem grandes dificuldades. *(invertido: 6 − x)* |
| ATN1 | **Para confirmar que você está lendo com atenção, marque "Discordo totalmente" nesta linha.** *(correta = 1; regra E3)* |

## Perguntas 5 e 6: uso da IA

**IAF.** Com que frequência você usa assistentes de IA generativa (por exemplo, ChatGPT, GitHub Copilot, Gemini) ao estudar programação? — 1 Nunca (→ vai para a pergunta 10) · 2 Raramente · 3 Às vezes · 4 Frequentemente · 5 Sempre

**IAU.** Quando usa IA ao estudar programação, qual é a principal finalidade? — Obter código pronto para a tarefa · Entender conceitos ou mensagens de erro · Revisar ou melhorar o meu próprio código · Gerar exemplos ou exercícios para praticar

## Pergunta 7: grade de dependência da IA (DEP)

*Enunciado:* "Sobre o uso de IA nos seus estudos de programação, indique o quanto você concorda com cada afirmação." (mesma escala da pergunta 4)

| ID | Linha |
|---|---|
| DEP1 | Recorro à IA antes de tentar resolver o problema sozinho(a). |
| DEP2 | Sem a IA, eu teria dificuldade para concluir os exercícios de programação. |
| DEP3 | Sinto que não conseguiria programar sem a ajuda da IA. |
| DEP4 ᴿ | Consigo resolver exercícios de programação sem IA quando preciso. *(invertido: 6 − x)* |

## Pergunta 8: grade de aprendizado percebido com IA (APR)

*Enunciado:* "Pensando no que você aprende quando usa IA, indique o quanto você concorda com cada afirmação." (mesma escala)

| ID | Linha |
|---|---|
| APR1 | A IA me ajuda a entender conceitos de programação. |
| APR2 | Com a IA, aprendo programação mais rápido. |
| APR3 | Consigo explicar, com minhas palavras, o código que a IA me ajudou a escrever. |

## Pergunta 9: avaliação geral

**AVG.** No geral, como a IA generativa afetou o seu aprendizado de programação? — 1 Piorou muito · 2 Piorou um pouco · 3 Não mudou · 4 Melhorou um pouco · 5 Melhorou muito

## Pergunta 10: aberta (opcional)

**ABR.** (Opcional) Como a IA generativa mudou a forma como você aprende programação? Não escreva nomes de pessoas, professores ou instituições.

---

## Base na literatura

| Construto ou item | Base |
|---|---|
| Foco geral | Becker et al. (2023): a IA generativa muda o ensino de programação; Zastudil et al. (2023): percepções de estudantes e professores |
| DEP (dependência) | Prather et al. (2024): a IA acelera quem já sabe e agrava as dificuldades de quem tem dificuldade; Margulieux et al. (2024): autoeficácia e autorregulação influenciam como iniciantes usam LLMs |
| APR (aprendizado percebido) | Amoozadeh et al. (2024): survey com 253 estudantes sobre confiança na IA e efeito no desempenho; APR3 investiga a "ilusão de competência" de Prather et al. (2024) |
| IAU (finalidade) | Categorias de uso descritas em Prather et al. (2024) e Zastudil et al. (2023) |
| DIF (dificuldade) | Robins, Rountree e Rountree (2003); DIF1 e DIF2 vêm da versão preliminar do grupo |
