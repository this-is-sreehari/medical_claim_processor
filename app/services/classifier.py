from .gemini_client import GeminiClient


class PDFClassifier:
    def __init__(self):
        self.llm = GeminiClient()

    async def classify(self, text: str) -> str:
        prompt = f"""
        You are a medical claim PDF classifier.
        Classify the document into one of the following:
        ["bill", "discharge_summary", "id_card", "pharmacy_bill", "claim_form"]

        TEXT:
        {text}

        Respond only with the label.
        """
        return await self.llm.generate(prompt)
