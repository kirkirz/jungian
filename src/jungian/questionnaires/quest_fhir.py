"""Module to construct standard FHIR representations of inventories and responses."""

import datetime
from typing import Any, List
from .quest import get_scale_config

EXT_ORDINAL = "http://hl7.org/fhir/StructureDefinition/ordinalValue"


def _get_namespaces(base_domain: str) -> tuple[str, str, str]:
    """Helper to dynamically construct professional namespaces from any domain."""
    clean_domain = base_domain.rstrip("/")
    return (
        f"{clean_domain}/fhir/CodeSystem/inventory-dimensions",
        f"{clean_domain}/fhir/CodeSystem/likert-scale-codes",
        f"{clean_domain}/fhir/StructureDefinition/scale-score",
    )


def questionnaire_to_fhir(data: dict[str, Any], base_domain: str) -> dict[str, Any]:
    """Compiles custom IR Questionnaire schema into a professional FHIR template."""
    quest_id = data.get("name", "unknown").lower().replace(" ", "-")
    sys_dimensions, sys_answers, _ = _get_namespaces(base_domain)

    fhir_questionnaire = {
        "resourceType": "Questionnaire",
        "id": quest_id,
        "status": "active",
        "title": data["name"],
        "item": [],
    }

    scale = get_scale_config(data)
    min_val, max_val, labels = scale["min"], scale["max"], scale["labels"]

    for i, item in enumerate(data["items"], start=1):
        dimension_codes = []
        if "mapping" in item:
            dimension_codes = [
                {"system": sys_dimensions, "code": k} for k in item["mapping"].keys()
            ]
        elif "target" in item:
            dimension_codes = [{"system": sys_dimensions, "code": item["target"]}]
        elif "targets" in item:
            dimension_codes = [
                {"system": sys_dimensions, "code": t} for t in item["targets"]
            ]

        fhir_item = {
            "linkId": f"q{i}",
            "text": item["text"],
            "type": "choice",
            "code": dimension_codes,
            "answerOption": [],
        }

        for val in range(min_val, max_val + 1):
            label_idx = val - min_val
            display_label = labels[label_idx] if label_idx < len(labels) else str(val)

            fhir_item["answerOption"].append(  # type: ignore[attr-defined]
                {
                    "valueCoding": {
                        "system": sys_answers,
                        "code": str(val),
                        "display": display_label,
                    },
                    "extension": [{"url": EXT_ORDINAL, "valueDecimal": float(val)}],
                }
            )

        fhir_questionnaire["item"].append(fhir_item)  # type: ignore[attr-defined]

    return fhir_questionnaire


def response_to_fhir(
    data: dict[str, Any],
    answers: list[int],
    norm_scores: dict[str, float],
    base_domain: str,
) -> dict[str, Any]:
    """Compiles user answers into a professional FHIR response submission."""
    quest_id = data.get("name", "unknown").lower().replace(" ", "-")
    _, sys_answers, ext_scale = _get_namespaces(base_domain)

    scale = get_scale_config(data)
    min_val, labels = scale["min"], scale["labels"]

    # Explicit list instantiation to satisfy static checkers like mypy/pylint
    items_payload: List[dict[str, Any]] = []
    extensions_payload: List[dict[str, Any]] = []

    fhir_response = {
        "resourceType": "QuestionnaireResponse",
        "id": f"{quest_id}-response",
        "questionnaire": f"Questionnaire/{quest_id}",
        "status": "completed",
        "authored": datetime.datetime.now(datetime.timezone.utc)
        .isoformat()
        .replace("+00:00", "Z"),
        "item": items_payload,
        "extension": extensions_payload,
    }

    for i, item in enumerate(data["items"]):
        answer_val = answers[i]
        label_idx = answer_val - min_val
        display_label = (
            labels[label_idx] if 0 <= label_idx < len(labels) else str(answer_val)
        )

        items_payload.append(
            {
                "linkId": f"q{i+1}",
                "text": item["text"],
                "answer": [
                    {
                        "valueCoding": {
                            "system": sys_answers,
                            "code": str(answer_val),
                            "display": display_label,
                        }
                    }
                ],
            }
        )

    for score_key, score_percent in norm_scores.items():
        extensions_payload.append(
            {
                "url": ext_scale,
                "extension": [
                    {"url": "dimension", "valueCode": score_key},
                    {
                        "url": "scorePercentage",
                        "valueDecimal": round(score_percent, 2),
                    },
                ],
            }
        )

    return fhir_response
