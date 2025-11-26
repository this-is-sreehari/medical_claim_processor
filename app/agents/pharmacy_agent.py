from app.services.gemini_client import GeminiClient
from app.utils.json_utils import clean_json


class PharmacyAgent:
    def __init__(self):
        self.llm = GeminiClient()

    async def run(self, text: str):
        prompt = f"""
        You are a pharmacy bill extraction agent.
        Parse the following text and return structured JSON ONLY.

        TEXT:
        {text}

        JSON format:
        {{
            "document_type": "pharmacy_bill",
            "pharmacy_name": "",
            "patient_name": "",
            "patient_id": "",
            "date": "",
            "items": [
                {{
                    "medicine": "",
                    "quantity": "",
                    "rate": "",
                    "amount": ""
                }}
            ],
            "total_amount": ""
        }}
        """
        result = await self.llm.generate(prompt)
        cleaned_result = clean_json(result)

        return cleaned_result
