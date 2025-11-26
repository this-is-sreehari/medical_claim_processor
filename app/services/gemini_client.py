from google import genai
from dotenv import load_dotenv
import os

load_dotenv()


class GeminiClient:
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.model_name = "gemini-2.5-flash"
    
    async def generate(self, prompt: str) -> dict:
        try:
            response = await self.client.aio.models.generate_content(
                model=self.model_name,
                contents=prompt
            )
            return response.text
        except Exception as e:
            return {"error": str(e)}
