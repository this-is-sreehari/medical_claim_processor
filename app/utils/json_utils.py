import json
import re


def clean_json(text: str):
    if not text:
        return {}

    cleaned = re.sub(r"```json|```", "", text, flags=re.IGNORECASE).strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", cleaned, re.DOTALL)
        if match:
            try:
                return json.loads(match.group())
            except:
                pass

        return {}
