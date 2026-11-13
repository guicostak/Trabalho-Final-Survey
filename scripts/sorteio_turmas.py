#!/usr/bin/env python3
"""Sorteio reprodutível de turmas (amostragem estratificada por conglomerados).

Pré-registrado no protocolo (Seção 2.2):
  - estratos h = curso x período (1º a 4º);
  - em cada estrato com M_h turmas, sorteiam-se m_h = min(M, M_h) turmas
    por amostragem aleatória simples sem reposição (padrão M = 2);
  - semente fixa e pré-registrada: 20261113.

O resultado depende apenas do quadro amostral (CSV) e da semente. Quem rodar
o script com o mesmo quadro obtém exatamente a mesma amostra.

Uso:
    python3 scripts/sorteio_turmas.py quadro_turmas.csv
    python3 scripts/sorteio_turmas.py quadro_turmas.csv --m 2 --seed 20261113 --saida turmas_sorteadas.csv

Colunas exigidas no CSV de entrada:
    turma_id, curso, periodo, disciplina, matriculados
"""
from __future__ import annotations

import argparse
import csv
import random
import sys
from collections import defaultdict

SEMENTE_PREREGISTRADA = 20261113
COLUNAS = ("turma_id", "curso", "periodo", "disciplina", "matriculados")


def ler_quadro(caminho: str) -> list[dict[str, str]]:
    with open(caminho, newline="", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        faltantes = [c for c in COLUNAS if c not in (leitor.fieldnames or [])]
        if faltantes:
            sys.exit(f"Colunas ausentes no quadro amostral: {', '.join(faltantes)}")
        linhas = [dict(l) for l in leitor]
    ids = [l["turma_id"] for l in linhas]
    if len(ids) != len(set(ids)):
        sys.exit("turma_id repetido no quadro amostral.")
    return linhas


def sortear(linhas: list[dict[str, str]], m: int, semente: int) -> list[dict[str, str]]:
    estratos: dict[tuple[str, int], list[dict[str, str]]] = defaultdict(list)
    for l in linhas:
        estratos[(l["curso"].strip().upper(), int(l["periodo"]))].append(l)

    rng = random.Random(semente)
    sorteadas = []
    # Ordem determinística: estratos e turmas ordenados antes do sorteio.
    for chave in sorted(estratos):
        turmas = sorted(estratos[chave], key=lambda t: t["turma_id"])
        k = min(m, len(turmas))
        escolhidas = rng.sample(turmas, k)
        for t in sorted(escolhidas, key=lambda t: t["turma_id"]):
            sorteadas.append({**t, "estrato": f"{chave[0]}-P{chave[1]}", "M_h": len(turmas), "m_h": k})
    return sorteadas


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("quadro", help="CSV do quadro amostral de turmas")
    ap.add_argument("--m", type=int, default=2, help="turmas por estrato (padrão: 2)")
    ap.add_argument("--seed", type=int, default=SEMENTE_PREREGISTRADA, help="semente (padrão pré-registrado: 20261113)")
    ap.add_argument("--saida", default="turmas_sorteadas.csv", help="CSV de saída")
    args = ap.parse_args()

    if args.seed != SEMENTE_PREREGISTRADA:
        print(f"AVISO: semente diferente da pré-registrada ({SEMENTE_PREREGISTRADA}). Registre em DESVIOS.md.", file=sys.stderr)

    sorteadas = sortear(ler_quadro(args.quadro), args.m, args.seed)

    campos = ["estrato", "M_h", "m_h", *COLUNAS]
    with open(args.saida, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
        w.writeheader()
        w.writerows(sorteadas)

    total = sum(int(t["matriculados"]) for t in sorteadas)
    print(f"Semente: {args.seed} | turmas sorteadas: {len(sorteadas)} | estudantes convidados: {total}")
    for t in sorteadas:
        print(f"  {t['estrato']:<8} {t['turma_id']:<6} {t['disciplina']:<40} matric.={t['matriculados']:>3}  (m_h={t['m_h']} de M_h={t['M_h']})")
    print(f"Arquivo gerado: {args.saida}")


if __name__ == "__main__":
    main()
