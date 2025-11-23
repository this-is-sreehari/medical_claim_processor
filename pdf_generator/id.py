from fpdf import FPDF

def generate_id_card_pdf(data, filename="id_card.pdf"):
    pdf = FPDF('P', 'mm', (85.60, 53.98))  # Standard ID card size in mm (credit card size)
    pdf.add_page()
    
    pdf.set_auto_page_break(auto=False)
    
    # Background color (optional)
    pdf.set_fill_color(220, 220, 220)
    pdf.rect(0, 0, 85.60, 53.98, 'F')
    
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, data.get("document_type", "").replace('_', ' ').title(), 0, 1, 'C')
    
    pdf.ln(2)
    pdf.set_font("Arial", '', 12)
    
    pdf.cell(30, 8, "Name:", 0, 0)
    pdf.cell(0, 8, data.get("name", ""), 0, 1)
    
    pdf.cell(30, 8, "DOB:", 0, 0)
    pdf.cell(0, 8, data.get("dob", ""), 0, 1)
    
    pdf.cell(30, 8, "Gender:", 0, 0)
    pdf.cell(0, 8, data.get("gender", ""), 0, 1)
    
    pdf.cell(30, 8, "ID Number:", 0, 0)
    pdf.cell(0, 8, data.get("id_number", ""), 0, 1)
    
    pdf.cell(30, 8, "Issuer:", 0, 0)
    pdf.cell(0, 8, data.get("issuer", ""), 0, 1)
    
    pdf.cell(30, 8, "Patient ID:", 0, 0)
    pdf.cell(0, 8, data.get("patient_id", ""), 0, 1)
    
    pdf.output(filename)

# Example usage:
data = {
    "document_type": "id_card",
    "name": "John Doe",
    "dob": "1990-01-01",
    "gender": "Female",
    "id_number": "ABC1234567",
    "issuer": "City Hospital",
    "patient_id": "98765"
}

generate_id_card_pdf(data, "patient_id_card.pdf")
