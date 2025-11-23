from google import genai
from google.genai import types
import os


class PDFUtils:
    def __init__(self, model_name: str = "gemini-2.5-flash"):
        # Use the new SDK client
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.model_name = model_name
    
    async def extract_raw_text(self, pdf_bytes: bytes) -> str:
        prompt = """
        You are an OCR extraction agent. Extract ALL text from this PDF.
        Return ONLY raw text with no explanations.
        """
        
        # Create contents with both text prompt and PDF bytes
        contents = [
            types.Part.from_text(text=prompt),
            types.Part.from_bytes(data=pdf_bytes, mime_type="application/pdf")
        ]
        
        response = await self.client.aio.models.generate_content(
            model=self.model_name,
            contents=contents
        )
        
        return response.text or ""
