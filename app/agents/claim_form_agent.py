from app.services.gemini_client import GeminiClient


class ClaimFormAgent:
    def __init__(self):
        self.llm = GeminiClient()

    async def run(self, text: str):
        prompt = f"""
        You are a claim form extraction agent.
        Extract required fields in strict JSON format.

        TEXT:
        {text}

        Output JSON:
        {{
        "document_type": "claim_form",
        "patient_name": "",
        "policy_number": "",
        "insurance_company": "",
        "hospital_name": "",
        "claim_amount": "",
        "admission_date": "",
        "discharge_date": ""
        }}
        """
        return await self.llm.generate(prompt)
