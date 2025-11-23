from app.services.classifier import PDFClassifier
from app.services.extractor import PDFExtractor
from app.services.validator import ClaimValidator
from app.agents.bill_agent import BillAgent
from app.agents.discharge_agent import DischargeAgent
from app.agents.id_agent import IDAgent
from app.agents.pharmacy_agent import PharmacyAgent
from app.agents.claim_form_agent import ClaimFormAgent

from app.utils.pdf_utils import PDFUtils
from app.utils.json_utils import clean_json


class Orchestrator:
    def __init__(self):
        self.classifier = PDFClassifier()
        self.extractor = PDFExtractor()
        self.validator = ClaimValidator()

        self.agents = {
            "bill": BillAgent(),
            "discharge_summary": DischargeAgent(),
            "id_card": IDAgent(),
            "pharmacy_bill": PharmacyAgent(),
            "claim_form": ClaimFormAgent(),
        }

    async def process(self, pdf_files) -> dict:
        results = {}
        
        for file in pdf_files:
            raw_text = await PDFUtils().extract_raw_text(await file.read())
            doc_type = await self.classifier.classify(raw_text)
            cleaned_text = await self.extractor.extract(raw_text)
            agent = self.agents.get(doc_type)
            structured = await agent.run(cleaned_text)

            results[doc_type] = structured
        missing = self.validator.detect_missing(results)
        discrepancies = await self.validator.detect_discrepancies(results)

        if missing:
            decision = {"status": "rejected", "reason": "Missing required documents"}
        elif discrepancies:
            decision = {"status": "manual_review", "reason": "Data inconsistencies found"}
        else:
            decision = {"status": "approved", "reason": "All documents consistent"}

        cleaned_results = []
        for doc_type, data in results.items():
            cleaned_results.append({
                doc_type: clean_json(data)
            })
        cleaned_discrepancies = clean_json(discrepancies)

        return {
            "documents": cleaned_results,
            "validation": {
                "missing_documents": missing,
                "discrepancies": cleaned_discrepancies
            },
            "claim_decision": decision
        }
