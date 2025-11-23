from google import generativeai as genai


class PDFUtils:
    def __init__(self, model_name: str = "gemini-1.5-pro"):
        self.model = genai.GenerativeModel(model_name)

    async def extract_raw_text(self, pdf_bytes: bytes) -> str:
        """
        Use Gemini OCR for text extraction from scanned PDFs.
        """
        prompt = """
        You are an OCR extraction agent. Extract ALL text from this PDF.
        Return ONLY raw text with no explanations.
        """

        response = await self.model.generate_content_async(
            prompt,
            mime_type="application/pdf",
            data=pdf_bytes,
        )

        return response.text or ""
