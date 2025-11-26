from app.services.gemini_client import GeminiClient
from app.utils.json_utils import clean_json


class DischargeAgent:
    def __init__(self):
        self.llm = GeminiClient()

    async def run(self, text: str):
        prompt = f"""
        You are a medical discharge data extraction agent.
        Extract structured JSON from the discharge summary below.

        TEXT:
        {text}

        Return JSON only with:
        {{
            "document_type": "discharge_summary",
            "patient_name": "",
            "patient_id": "",
            "hospital_name": "",
            "admission_date": "",
            "discharge_date": "",
            "diagnosis": "",
            "doctor_name": "",
            "summary": ""
        }}
        """
        result = await self.llm.generate(prompt)
        cleaned_result = clean_json(result)

        return cleaned_result
