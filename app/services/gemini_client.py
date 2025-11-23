import google.generativeai as genai
import os, json


class GeminiClient:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel("gemini-1.5-pro")

    async def generate(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        try:
            return json.loads(response)
        except:
            return {"error": "Invalid discharge summary output", "raw": response}
