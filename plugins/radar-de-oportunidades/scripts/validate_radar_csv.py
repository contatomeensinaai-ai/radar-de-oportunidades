#!/usr/bin/env python3
import csv
import sys
from pathlib import Path
from urllib.parse import urlparse

REQUIRED = [
    "nome_empresa",
    "categoria",
    "cidade",
    "estado_pais",
    "website",
    "instagram_publico",
    "google_maps_url",
    "telefone_comercial_publico",
    "email_comercial_publico",
    "sinais_observados",
    "oportunidade_identificada",
    "evidencias_urls",
    "pontuacao_0_100",
    "prioridade",
    "nivel_confianca",
    "abordagem_sugerida_rascunho",
    "data_pesquisa",
]


def normalized_domain(value):
    value = (value or "").strip()
    if not value:
        return ""
    parsed = urlparse(value if "://" in value else f"https://{value}")
    return parsed.netloc.lower().removeprefix("www.")


def main():
    if len(sys.argv) != 2:
        print("Uso: validate_radar_csv.py LEADS-QUALIFICADOS.csv", file=sys.stderr)
        return 2
    csv_path = Path(sys.argv[1])
    if not csv_path.exists():
        print(f"Arquivo não encontrado: {csv_path}", file=sys.stderr)
        return 2

    errors = []
    seen = set()
    with csv_path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != REQUIRED:
            errors.append("Cabeçalho diferente do modelo oficial.")
        for line_number, row in enumerate(reader, start=2):
            name = (row.get("nome_empresa") or "").strip()
            if not name:
                errors.append(f"Linha {line_number}: nome da empresa ausente.")
            try:
                score = int((row.get("pontuacao_0_100") or "").strip())
                if not 0 <= score <= 100:
                    raise ValueError
            except ValueError:
                errors.append(f"Linha {line_number}: pontuação deve ser um inteiro entre 0 e 100.")
            evidence = (row.get("evidencias_urls") or "").strip()
            if not evidence:
                errors.append(f"Linha {line_number}: evidência ausente.")
            key = (normalized_domain(row.get("website")), name.casefold(), (row.get("cidade") or "").strip().casefold())
            if key in seen:
                errors.append(f"Linha {line_number}: possível duplicata de empresa.")
            seen.add(key)

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("CSV do Radar de Oportunidades validado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
