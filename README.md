# Survey pré-registrado: aprendizado de programação na era da IA generativa

**Instituição:** PUC Minas, Unidade Lourdes, Bacharelado em Engenharia de Software
**Disciplina:** Medição e Experimentação em Engenharia de Software, 2º/2026
**Grupo:** Ana Luiza Santos Gomes, Bruna Barbosa Portilho Bernardes, Guilherme Augustto Costa Barros e Vinícius Dias
**Entrega 1 (Planejamento):** 13/11/2026 às 23:59, no Canvas

| | |
|---|---|
| **Método** | Survey transversal por questionário on-line (descritivo e correlacional) |
| **População** | Estudantes e profissionais formados em CC, ES, ADS e SI de instituições brasileiras |
| **Amostragem** | Não probabilística: conveniência com bola de neve, em vários canais e com metas por segmento |
| **Amostra** | Meta de 50 respostas válidas (mínimo do enunciado); margem nominal de ±13,9 p.p. |
| **Instrumento** | Aceite + 10 perguntas (a última aberta e opcional), sem ramificações, cerca de 4 min, já montado no Microsoft Forms |
| **QPs** | 4 QPs (a central: a IA favorece conceitos em detrimento da prática de escrita?) e 7 hipóteses, com α = 0,05 e correção de Holm |
| **Coleta** | 18/11 a 04/12/2026 |

---

## O que entregar no Canvas hoje (Parte 1)

**Apenas o arquivo [`protocolo/protocolo.pdf`](protocolo/protocolo.pdf)**, com até 6 páginas e as 8 seções do enunciado. O envio no Canvas já comprova a data. A tag no GitHub é um reforço opcional.

Antes de enviar:
- [ ] **Aplicar o pré-teste** com 3 a 5 pessoas ([`pre-teste/roteiro-pre-teste.md`](pre-teste/roteiro-pre-teste.md)) e preencher a Tabela 6 com as mudanças **reais**.
- [ ] Preencher os campos em **laranja** do PDF: N estimado e dados do pré-teste.
- [ ] Recompilar e conferir que o PDF continua com **até 6 páginas**.
- [ ] Só abrir o formulário **depois** do envio.

Os demais arquivos não são entregues no Canvas. Eles servem para montar o formulário, fazer o pré-teste, divulgar o survey e preparar a Parte 2.

---

## Estrutura da pasta

```
Trabalho-Final-Survey/
├── README.md                      ← este arquivo
├── ENUNCIADO.md                   ← enunciado da disciplina
├── DESVIOS.md                     ← registro de desvios (alimenta o dashboard na Parte 2)
├── protocolo/
│   ├── protocolo.pdf              ← ENTREGÁVEL DA PARTE 1 (6 páginas)
│   └── protocolo.tex              ← fonte LaTeX do PDF
├── docs/
│   ├── 01-guia-padroes-survey.md  ← como surveys científicos são planejados e escritos (pesquisa)
│   └── 02-lista-de-requisitos.md  ← requisitos (enunciado + padrões) × onde são atendidos
├── instrumento/
│   ├── questionario.md            ← questionário completo e configuração do formulário
│   ├── tcle.md                    ← Termo de Consentimento Livre e Esclarecido
│   ├── codebook.csv               ← livro de códigos (variáveis, escalas e regras de limpeza)
│   └── convites.md                ← textos de divulgação (docentes, grupos, redes e lembretes)
└── pre-teste/
    └── roteiro-pre-teste.md       ← procedimento e formulário de registro do pré-teste
```

## Como recompilar o PDF

```bash
cd protocolo && tectonic protocolo.tex
```

Também funciona com `xelatex protocolo.tex` ou no Overleaf, com o compilador **XeLaTeX**. Os campos pendentes usam o comando `\pend{...}`. Para conferir se sobrou algum:

```bash
grep -n '\\pend{' protocolo/protocolo.tex
```

Para conferir o número de páginas:

```bash
pdfinfo protocolo/protocolo.pdf | grep Pages
```

## Registro no GitHub (reforço opcional da data)

O repositório público é <https://github.com/guicostak/Trabalho-Final-Survey>. Depois de preencher tudo:

```bash
git add -A && git commit -m "Protocolo do survey v1.0 (pré-registro)"
```

```bash
git tag -a protocolo-v1.0 -m "Pré-registro do protocolo, Parte 1"
```

```bash
git push && git push origin protocolo-v1.0
```
