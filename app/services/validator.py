import json
from .gemini_client import GeminiClient


class ClaimValidator:
    def __init__(self):
        self.llm = GeminiClient()

    def detect_missing(self, docs):
        required = {"bill", "discharge_summary", "id_card"}
        found = set(docs.keys())
        return list(required - found)
    
    async def detect_discrepancies(self, docs: dict) -> str:
        prompt = f"""
        You are a strict JSON validator.
        Validate cross-document consistency across these insurance claim documents:

        ```json
        {json.dumps(docs, indent=2)}
        ```

        Check:
        - If patient_name matches across all docs
        - If patient_id matches
        - If hospital_name matches
        - If admission/discharge dates align
        - If bill amount matches line_items

        Return JSON only:

        {{
            "mismatches": ["list of mismatches"]
        }}
        """
        return await self.llm.generate(prompt)
