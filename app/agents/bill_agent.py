from app.services.gemini_client import GeminiClient


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
            "line_items": []
        }}

        TEXT:
        {text}
        """
        return await self.llm.generate(prompt)
