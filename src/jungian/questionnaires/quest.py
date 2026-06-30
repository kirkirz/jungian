import json
from pathlib import Path
from typing import Any


def load_quest(path: str | Path) -> dict[str, Any]:
    """Load a questionnaire"""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def score_quest(data: dict[str, Any], answers: list[int]) -> dict[str, int]:
    if "dimensions" in data:
        keys = list(data["dimensions"].keys())
    elif "functions" in data:
        keys = data["functions"]
    else:
        raise ValueError("Questionnaire must have 'dimensions' or 'functions'")

    scores = {k: 0 for k in keys}

    for i, item in enumerate(data["items"]):
        raw_score = answers[i]

        if item.get("reverse", False):
            raw_score = 4 - raw_score

        if "mapping" in item:
            # Weighted mapping: {"Ti": 2, "Te": 1}
            for target, weight in item["mapping"].items():
                if target in scores:
                    scores[target] += raw_score * weight
        elif "target" in item:
            # Single target (old format)
            target = item["target"]
            if target in scores:
                scores[target] += raw_score
        elif "targets" in item:
            # Multiple targets (old format)
            for target in item["targets"]:
                if target in scores:
                    scores[target] += raw_score

    return scores


def normalize_scores(scores: dict[str, int], data: dict[str, Any]) -> dict[str, float]:
    normalized = {}

    if "dimensions" in data:
        meta = data["dimensions"]
    elif "functions" in data:
        # Calculate max possible per function from mapping weights
        max_weights = {f: 0 for f in data["functions"]}
        for item in data["items"]:
            if "mapping" in item:
                for target, weight in item["mapping"].items():
                    if target in max_weights:
                        max_weights[target] += weight * 4
            elif "target" in item:
                target = item["target"]
                if target in max_weights:
                    max_weights[target] += 4
            elif "targets" in item:
                for target in item["targets"]:
                    if target in max_weights:
                        max_weights[target] += 4

        meta = {f: {"min": 0, "max": max_weights.get(f, 0)} for f in data["functions"]}
    else:
        raise ValueError("Questionnaire must have 'dimensions' or 'functions'")

    for key, raw in scores.items():
        min_score = meta[key]["min"]
        max_score = meta[key]["max"]
        if max_score > 0:
            normalized[key] = (raw - min_score) / (max_score - min_score) * 100
        else:
            normalized[key] = 0.0

    return normalized
