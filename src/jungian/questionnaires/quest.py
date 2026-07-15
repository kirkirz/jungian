"""Module for loading, validating, and scoring psychometric questionnaires."""

import json
from pathlib import Path
from typing import Any, TypedDict, Union

Numeric = Union[int, float]
ScoreDict = dict[str, float]


class ScaleConfig(TypedDict, total=False):
    """Configuration representation for questionnaire evaluation scales."""

    min: int
    max: int
    labels: list[str]


def validate_quest(data: dict[str, Any]) -> None:
    """Validates that the questionnaire schema contains all required fields."""
    required = ["name", "items"]
    for field in required:
        if field not in data:
            raise ValueError(f"Malformed questionnaire: Missing required '{field}' field.")

    if "dimensions" not in data and "functions" not in data:
        raise ValueError("Questionnaire must define either 'dimensions' or 'functions' for scoring.")

    if not isinstance(data["items"], list) or len(data["items"]) == 0:
        raise ValueError("Questionnaire 'items' must be a non-empty list.")


def get_scale_config(data: dict[str, Any]) -> ScaleConfig:
    """Extracts scale configuration from JSON or falls back to a standard 0-4 scale."""
    scale = data.get("scale", {})
    fallback_labels = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
    return {
        "min": int(scale.get("min", 0)),
        "max": int(scale.get("max", 4)),
        "labels": list(scale.get("labels", fallback_labels)),
    }


def _compute_max_weights(data: dict[str, Any], max_raw_val: int) -> dict[str, float]:
    """Helper to calculate max possible weights across all mapped functions."""
    max_weights = {f: 0.0 for f in data["functions"]}
    for item in data["items"]:
        if "mapping" in item:
            for target, weight in item["mapping"].items():
                if target in max_weights:
                    max_weights[target] += max_raw_val * weight
        elif "target" in item:
            target = item["target"]
            if target in max_weights:
                max_weights[target] += max_raw_val
        elif "targets" in item:
            for target in item["targets"]:
                if target in max_weights:
                    max_weights[target] += max_raw_val
    return max_weights


def load_quest(path: str | Path) -> dict[str, Any]:
    """Loads, validates, and pre-computes metadata for a questionnaire."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    validate_quest(data)

    scale = get_scale_config(data)
    max_raw_val = scale["max"]

    if "dimensions" in data:
        data["_meta"] = {
            k: {"min": v["min"], "max": v["max"]}
            for k, v in data["dimensions"].items()
        }
    else:
        max_weights = _compute_max_weights(data, max_raw_val)
        data["_meta"] = {
            f: {"min": 0.0, "max": max_weights[f]} for f in data["functions"]
        }

    return data


def score_quest(data: dict[str, Any], answers: list[int]) -> ScoreDict:
    """Computes raw scores across dimensions based on answers."""
    scale = get_scale_config(data)
    min_val, max_val = scale["min"], scale["max"]
    scores = {k: 0.0 for k in data["_meta"].keys()}

    for i, item in enumerate(data["items"]):
        raw_score = answers[i]

        if item.get("reverse", False):
            raw_score = max_val + min_val - raw_score

        if "mapping" in item:
            for target, weight in item["mapping"].items():
                if target in scores:
                    scores[target] += raw_score * weight
        elif "target" in item:
            target = item["target"]
            if target in scores:
                scores[target] += raw_score
        elif "targets" in item:
            for target in item["targets"]:
                if target in scores:
                    scores[target] += raw_score

    return scores


def normalize_scores(scores: ScoreDict, data: dict[str, Any]) -> dict[str, float]:
    """Normalizes raw scores to percentages using pre-computed metadata."""
    normalized = {}
    meta = data["_meta"]

    for key, raw in scores.items():
        min_score = meta[key]["min"]
        max_score = meta[key]["max"]

        range_size = max_score - min_score
        if range_size > 0:
            normalized[key] = max(0.0, min(100.0, (raw - min_score) / range_size * 100))
        else:
            normalized[key] = 0.0

    return normalized
