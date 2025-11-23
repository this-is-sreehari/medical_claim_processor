from fpdf import FPDF

def generate_claim_form_pdf(data, filename="claim_form.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    
    # Title
    pdf.cell(0, 10, txt=f"{data.get('document_type', '').title()} Report", ln=True, align="C")
    pdf.ln(10)
    
    # Patient and policy details
    pdf.set_font("Arial", size=12)
    pdf.cell(50, 10, txt="Patient Name:")
    pdf.cell(0, 10, txt=data.get("patient_name", ""), ln=True)
    
    pdf.cell(50, 10, txt="Patient ID:")
    pdf.cell(0, 10, txt=data.get("patient_id", ""), ln=True)
    
    pdf.cell(50, 10, txt="Policy Number:")
    pdf.cell(0, 10, txt=data.get("policy_number", ""), ln=True)
    
    pdf.cell(50, 10, txt="Insurance Company:")
    pdf.cell(0, 10, txt=data.get("insurance_company", ""), ln=True)
    
    pdf.cell(50, 10, txt="Hospital Name:")
    pdf.cell(0, 10, txt=data.get("hospital_name", ""), ln=True)
    
    pdf.cell(50, 10, txt="Claim Amount:")
    pdf.cell(0, 10, txt=data.get("claim_amount", ""), ln=True)
    
    pdf.cell(50, 10, txt="Admission Date:")
    pdf.cell(0, 10, txt=data.get("admission_date", ""), ln=True)
    
    pdf.cell(50, 10, txt="Discharge Date:")
    pdf.cell(0, 10, txt=data.get("discharge_date", ""), ln=True)
    
    pdf.output(filename)

# Example usage:
data = {
    "document_type": "claim_form",
    "patient_name": "John Doe",
    "patient_id": "12345",
    "policy_number": "POL123456789",
    "insurance_company": "ABC Insurance",
    "hospital_name": "General Hospital",
    "claim_amount": "$2000",
    "admission_date": "2025-11-15",
    "discharge_date": "2025-11-20"
}

generate_claim_form_pdf(data, "claim_form_report.pdf")
