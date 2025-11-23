from app.services.gemini_client import GeminiClient


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
        return await self.llm.generate(prompt)
