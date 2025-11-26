from app.services.gemini_client import GeminiClient
from app.utils.json_utils import clean_json


class BillAgent:
    def __init__(self):
        self.llm = GeminiClient()

    async def run(self, text: str):
        prompt = f"""
        You are a medical bill extraction agent.
        Extract the following fields as JSON:

        {{
            "document_type": "bill",
            "patient_name": "",
            "patient_id": "",
            "hospital_name": "",
            "bill_amount": "",
            "bill_date": "",
            "line_items": [
                {{
                    "description": "",
                    "quantity": "",
                    "price": ""
                }}
            ]
        }}

        TEXT:
        {text}
        """
        result = await self.llm.generate(prompt)
        cleaned_result = clean_json(result)

        return cleaned_result
