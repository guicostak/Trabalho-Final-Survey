# Survey pré-registrado: dificuldade percebida no aprendizado de programação

**Disciplina:** Medição e Experimentação em Engenharia de Software, 2º/2026
**Tema:** fatores associados à dificuldade percebida no aprendizado de programação entre estudantes dos períodos iniciais de Ciência da Computação e Engenharia de Software
**Entrega 1 (Planejamento):** 13/11/2026 às 23:59, com o protocolo em PDF de até 6 páginas

| | |
|---|---|
| **Método** | Survey transversal por questionário on-line (descritivo e correlacional) |
| **Amostragem** | Probabilística, estratificada (curso × período) por conglomerados (turmas sorteadas) |
| **Amostra** | Alvo de 100 respostas válidas (mínimo 50); margem de ±9,8 p.p. |
| **QPs** | 4 QPs e 7 hipóteses confirmatórias, com α = 0,05 e correção de Holm |
| **Coleta** | 18/11 a 04/12/2026 |

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
│   └── convites.md                ← textos de divulgação (sala, ambiente virtual e lembretes)
├── pre-teste/
│   └── roteiro-pre-teste.md       ← procedimento e formulário de registro do pré-teste
└── scripts/
    ├── sorteio_turmas.py          ← sorteio reprodutível das turmas (semente 20261113)
    └── quadro_turmas_MODELO.csv   ← modelo do quadro amostral (dados fictícios)
```

## Por onde começar

1. Leia [`docs/01-guia-padroes-survey.md`](docs/01-guia-padroes-survey.md) para entender o padrão científico seguido.
2. Abra [`protocolo/protocolo.pdf`](protocolo/protocolo.pdf). Os campos em **laranja** são pendências que o grupo precisa preencher.
3. Siga a seção **E** de [`docs/02-lista-de-requisitos.md`](docs/02-lista-de-requisitos.md), que lista as pendências em ordem.

## O que falta fazer hoje (13/11)

- [ ] Preencher nomes, instituição, URL do repositório, N estimado, ambiente virtual e data de exclusão dos dados (campos laranja em `protocolo.tex` e `tcle.md`).
- [ ] Montar o formulário no Microsoft Forms conforme `instrumento/questionario.md`.
- [ ] **Aplicar o pré-teste** com 3 a 5 pessoas (`pre-teste/roteiro-pre-teste.md`) e registrar as mudanças **reais** na Tabela 6.
- [ ] Recompilar o PDF e conferir que tem **até 6 páginas**.
- [ ] Registrar: commit + tag + push no GitHub **e** envio do PDF na plataforma até as 23:59.

## Como recompilar o PDF

```bash
cd protocolo && tectonic protocolo.tex
```

Também funciona com `xelatex protocolo.tex` ou no Overleaf, com o compilador **XeLaTeX**. Os campos pendentes usam o comando `\pend{...}`. Para conferir se sobrou algum:

```bash
grep -n '\\pend{' protocolo/protocolo.tex
```

## Como registrar o protocolo com data verificável

```bash
git init && git add . && git commit -m "Protocolo do survey v1.0 (pré-registro)"
```

```bash
git tag -a protocolo-v1.0 -m "Pré-registro do protocolo, Parte 1"
```

```bash
git remote add origin <URL-DO-REPOSITORIO> && git push -u origin main --tags
```

> A data do commit e da tag precisa ser **anterior à primeira resposta** (coleta a partir de 18/11). Não abra o formulário antes de registrar.

## Como sortear as turmas (16/11)

```bash
python3 scripts/sorteio_turmas.py quadro_turmas.csv --saida turmas_sorteadas.csv
```

O `quadro_turmas.csv` real segue o formato do modelo. Mantenha a semente pré-registrada (`20261113`); qualquer mudança vai para o `DESVIOS.md`.
