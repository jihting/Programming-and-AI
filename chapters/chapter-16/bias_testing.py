"""Week 6 Lab 3 starter: bias-probe runner.

This script can run in dry-run mode, or it can call the generic GenAI API client
from Lab 2 if your endpoint and key are configured.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

try:
    from genai_api_client import ask_genai
except ImportError:
    # This fallback lets the file run inside the starter-code folder before students
    # copy and rename genai_api_client_starter.py to genai_api_client.py.
    from genai_api_client_starter import ask_genai

PROBES_FILE = Path("bias_probes.json")
RESULTS_FILE = Path("bias_results.csv")


def load_probes(path: Path = PROBES_FILE) -> list[dict[str, str]]:
    """Load probe prompts from JSON."""
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def run_probe(prompt: str) -> str:
    """Run one probe prompt through the GenAI client."""
    return ask_genai(prompt, history=[])


def save_results(rows: list[dict[str, str]], path: Path = RESULTS_FILE) -> None:
    """Save probe results to CSV."""
    fieldnames = ["id", "domain", "prompt", "response", "severity", "notes"]
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    probes = load_probes()
    rows: list[dict[str, str]] = []

    for probe in probes:
        print(f"Running {probe['id']}: {probe['domain']}")
        response = run_probe(probe["prompt"])
        rows.append(
            {
                "id": probe["id"],
                "domain": probe["domain"],
                "prompt": probe["prompt"],
                "response": response.replace("\n", " "),
                "severity": "TODO: none / low / medium / high",
                "notes": "TODO: describe any pattern or concern",
            }
        )

    save_results(rows)
    print(f"Saved {len(rows)} rows to {RESULTS_FILE}")


if __name__ == "__main__":
    main()
