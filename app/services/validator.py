class ClaimValidator:

    def detect_missing(self, docs):
        required = {"bill", "discharge_summary", "id_card"}
        found = set(docs.keys())
        return list(required - found)

    def detect_discrepancies(self, docs):
        mismatches = []

        # simple cross-check
        bill = docs.get("bill", {})
        discharge = docs.get("discharge_summary", {})

        if bill.get("patient_name") != discharge.get("patient_name"):
            mismatches.append("Patient name mismatch")

        return mismatches
