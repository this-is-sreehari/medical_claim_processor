from app.services.gemini_client import GeminiClient


class IDAgent:
    def __init__(self):
        self.llm = GeminiClient()

    async def run(self, text: str):
        prompt = f"""
        You are an OCR identity extraction agent.
        Extract structured JSON ONLY from the ID card text below.

        TEXT:
        {text}

        Required JSON:
        {{
        "document_type": "id_card",
        "name": "",
        "dob": "",
        "gender": "",
        "id_number": "",
        "issuer": ""
        }}
        """
        return await self.llm.generate(prompt)
