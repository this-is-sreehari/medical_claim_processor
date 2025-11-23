from .gemini_client import GeminiClient


class PDFExtractor:
    def __init__(self):
        self.llm = GeminiClient()

    async def extract(self, raw_text: str) -> str:
        prompt = f"""
        Extract clean readable text from this noisy PDF content.
        Ensure formatting is preserved.

        TEXT:
        {raw_text}
        """
        return await self.llm.generate(prompt)
