# Instrumento de coleta: conceitos e prática de escrita de código na era da IA

> **Estudo:** Aprendizado de programação na era da IA generativa: conceitos e prática de escrita de código entre estudantes e profissionais de tecnologia
> **População:** estudantes e profissionais formados em CC, ES, ADS, SI e cursos afins, de instituições brasileiras, com 18 anos ou mais.
> **Versão:** 1.0, registrada com o protocolo em 13/11/2026. Mudanças após o pré-teste exigem nova versão e registro em `DESVIOS.md`.
> **Plataforma:** Microsoft Forms (conta PUC Minas), formulário "Experiência de estudantes com o aprendizado de programação". Já está montado; ainda não foi divulgado.
> **Link de resposta:** https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=ZIEqXraHC0OsawjWIp5wWbdFJRrrPlxBl43UGrMMybJUMVhBRFFDVDM3VzRRQkgzSjBLUlU5QTU2Ti4u
> **Estrutura:** aceite obrigatório e **11 perguntas**, a última aberta e opcional. **Sem ramificações:** todas as perguntas aparecem juntas. Duração estimada: **cerca de 4 minutos**.
> **Rastreabilidade:** cada ID abaixo é o nome da variável no `codebook.csv` e na Quadro 2 do protocolo.

---

## Configuração aplicada no Microsoft Forms

| Configuração | Valor | Motivo |
|---|---|---|
| Quem pode responder | **Qualquer pessoa** (resposta anônima, sem login) | Link aberto a várias instituições; anonimização na origem |
| Nome e e-mail | **Não coletados** | Protocolo, §6 |
| Ocultar "Enviar outra resposta" | **Ativado** | Reduz duplicatas (regra E5) |
| Ramificações | **Nenhuma** | O formulário aparece inteiro; quem não usa IA marca "Não uso IA" |
| Perguntas fechadas | Obrigatórias | Ausência só por escolha "Não uso IA" e na aberta |
| Título | "Experiência de estudantes com o aprendizado de programação" (neutro) | Evita autosseleção por interesse em IA |

---

## Aceite (obrigatório)

**ACE.** Li o termo acima, tenho 18 anos ou mais e concordo em participar desta pesquisa.
- ( ) Sim, concordo em participar *(única opção)*

## Perguntas 1 a 4: perfil

**CUR.** Qual curso de tecnologia você cursa ou cursou? — Ciência da Computação · Engenharia de Software · Análise e Desenvolvimento de Sistemas (ADS) · Sistemas de Informação · Outro curso de tecnologia · Não cursei curso de tecnologia *(fora da população: regra E1)*

**SIT.** Qual é a sua situação atual em relação à graduação e ao mercado? — Estudante, do 1º ao 4º período · Estudante, do 5º período em diante · Formado(a) há até 3 anos · Formado(a) há mais de 3 anos

**ATU.** Você já atua profissionalmente na área de tecnologia (inclui estágio)? — Sim, já atuo na área · Não, ainda não atuo na área

**MOM.** Você começou a aprender programação antes ou depois da popularização da IA generativa (ChatGPT, no fim de 2022)? — Antes (comecei a aprender até 2022) · Depois (comecei a aprender a partir de 2023)

## Perguntas 5 e 6: uso da IA

**IAF.** Com que frequência você usa assistentes de IA generativa (por exemplo, ChatGPT, GitHub Copilot, Gemini) ao estudar ou aprender programação? — Nunca · Raramente · Às vezes · Frequentemente · Sempre

**IAU.** Quando usa IA ao estudar programação, qual é a principal finalidade? — Obter código pronto para a tarefa · Entender conceitos ou mensagens de erro · Revisar ou melhorar o meu próprio código · Gerar exemplos ou exercícios para praticar · Não uso IA para estudar programação

## Pergunta 7: grade de aprendizado de conceitos com IA (CON)

*Enunciado:* "Sobre ENTENDER conceitos de programação com ajuda de IA, indique o quanto você concorda com cada afirmação. Se não usa IA, marque 'Não uso IA'."
Colunas: 1 Discordo totalmente · 2 Discordo · 3 Nem concordo nem discordo · 4 Concordo · 5 Concordo totalmente · **Não uso IA**

| ID | Linha |
|---|---|
| CON1 | A IA me ajuda a entender conceitos de programação. |
| CON2 | Com a IA, entendo mais rápido por que um código funciona ou falha. |
| CON3 | A IA me ajuda a compreender mensagens de erro e documentação. |

## Pergunta 8: grade de prática de escrita de código (PRA) e verificação de atenção

*Enunciado:* "Sobre PRATICAR a escrita de código, indique o quanto você concorda com cada afirmação. Se não usa IA, marque 'Não uso IA'." (mesmas colunas)

| ID | Linha |
|---|---|
| PRA1 | Escrevo eu mesmo(a) a maior parte do código das minhas atividades. |
| PRA2 | Consigo escrever do zero, sem IA, um código parecido com o que ela me ajudou a fazer. |
| PRA3 | Com frequência, pratico escrevendo código sem nenhuma ajuda de IA. |
| PRA4 ᴿ | Desde que passei a usar IA, escrevo menos código por conta própria. *(invertido: 6 − x)* |
| ATN1 | **Para confirmar que você está lendo com atenção, marque "Discordo totalmente" nesta linha.** *(correta = 1; regra E2)* |

## Perguntas 9 e 10: confiança e avaliação geral

**CONF.** Hoje, quão confiante você se sente para escrever um programa do zero, sem ajuda de IA? — Nada confiante · Pouco confiante · Razoavelmente confiante · Confiante · Muito confiante

**AVG.** No geral, como a IA generativa afetou o seu aprendizado de programação? — Piorou muito · Piorou um pouco · Não mudou · Melhorou um pouco · Melhorou muito · Não uso IA

## Pergunta 11: aberta (opcional)

**ABR.** (Opcional) Você sente que a IA mudou o equilíbrio entre entender conceitos e praticar a escrita de código? Conte como. Não escreva nomes de pessoas, professores ou instituições.

---

## Base na literatura

| Construto ou item | Base |
|---|---|
| Hipótese central (conceitos × prática) | Prather et al. (2024): a IA acelera quem já sabe o que quer, mas agrava dificuldades metacognitivas e gera ilusão de competência |
| CON (conceitos) | Amoozadeh et al. (2024): survey com 253 estudantes sobre o efeito da IA no desempenho; Zastudil et al. (2023) |
| PRA (prática) | Prather et al. (2024); PRA2 e CONF investigam se o respondente consegue escrever sem IA |
| IAU (finalidade) | Categorias de uso em Prather et al. (2024) e Zastudil et al. (2023) |
| MOM (antes/depois) | Becker et al. (2023): a IA generativa muda o ensino de programação |
| SIT e IAF | Margulieux et al. (2024): como iniciantes e outros perfis usam LLMs |
