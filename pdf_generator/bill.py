from fpdf import FPDF

def generate_pdf_report(data, filename="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    
    # Title
    pdf.cell(0, 10, txt=f"{data.get('document_type', '').title()} Report", ln=True, align="C")
    pdf.ln(10)
    
    # Patient and hospital details
    pdf.set_font("Arial", size=12)
    pdf.cell(50, 10, txt="Patient Name:")
    pdf.cell(0, 10, txt=data.get("patient_name", ""), ln=True)
    
    pdf.cell(50, 10, txt="Patient ID:")
    pdf.cell(0, 10, txt=data.get("patient_id", ""), ln=True)
    
    pdf.cell(50, 10, txt="Hospital Name:")
    pdf.cell(0, 10, txt=data.get("hospital_name", ""), ln=True)
    
    pdf.cell(50, 10, txt="Bill Amount:")
    pdf.cell(0, 10, txt=data.get("bill_amount", ""), ln=True)
    
    pdf.cell(50, 10, txt="Bill Date:")
    pdf.cell(0, 10, txt=data.get("bill_date", ""), ln=True)
    
    # Line items
    pdf.ln(10)
    pdf.cell(0, 10, txt="Line Items:", ln=True)
    line_items = data.get("line_items", [])
    
    if not line_items:
        pdf.cell(0, 10, txt="No line items available.", ln=True)
    else:
        # Table header
        pdf.set_font("Arial", "B", 12)
        pdf.cell(80, 10, "Description", border=1)
        pdf.cell(30, 10, "Quantity", border=1)
        pdf.cell(30, 10, "Price", border=1, ln=True)
        
        pdf.set_font("Arial", size=12)
        for item in line_items:
            pdf.cell(80, 10, item.get("description", ""), border=1)
            pdf.cell(30, 10, str(item.get("quantity", "")), border=1)
            pdf.cell(30, 10, str(item.get("price", "")), border=1, ln=True)
    
    pdf.output(filename)

# Example usage:
data = {
    "document_type": "bill",
    "patient_name": "John Doe",
    "patient_id": "12345",
    "hospital_name": "General Hospital",
    "bill_amount": "$500",
    "bill_date": "2025-11-23",
    "line_items": [
        {"description": "X-Ray", "quantity": 1, "price": "$100"},
        {"description": "Blood Test", "quantity": 2, "price": "$200"},
        {"description": "Consultation", "quantity": 1, "price": "$200"}
    ]
}

generate_pdf_report(data, "bill_report.pdf")
