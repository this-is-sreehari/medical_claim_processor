from app.services.classifier import PDFClassifier
from app.services.extractor import PDFExtractor
from app.services.validator import ClaimValidator
from app.agents.bill_agent import BillAgent
from app.agents.discharge_agent import DischargeAgent
from app.agents.id_agent import IDAgent
from app.agents.pharmacy_agent import PharmacyAgent
from app.agents.claim_form_agent import ClaimFormAgent

from app.utils.pdf_utils import PDFUtils


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
        if missing:
            decision = {"status": "rejected", "reason": "Missing required documents"}
            print("\n\n\n---------")
            print('decision\n\n', decision)
            print("\n\n\n---------")
        else:
            decision = {"status": "approved", "reason": "All documents consistent"}
        # discrepancies = self.validator.detect_discrepancies(results)

        # Final decision
        # elif discrepancies:
        #     decision = {"status": "manual_review", "reason": "Data inconsistencies found"}

        return {
            "documents": results,
            "validation": {
                "missing_documents": missing,
            #     "discrepancies": discrepancies
            },
            "claim_decision": decision
        }
