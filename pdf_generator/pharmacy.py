from fpdf import FPDF

def generate_pharmacy_bill_pdf(data, filename="pharmacy_bill.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)

    # Title
    pdf.cell(0, 10, txt=f"{data.get('document_type', '').replace('_', ' ').title()}", ln=True, align="C")
    pdf.ln(10)

    # Pharmacy and patient details
    pdf.set_font("Arial", size=12)
    pdf.cell(50, 10, "Pharmacy Name:")
    pdf.cell(0, 10, data.get("pharmacy_name", ""), ln=True)

    pdf.cell(50, 10, "Patient Name:")
    pdf.cell(0, 10, data.get("patient_name", ""), ln=True)

    pdf.cell(50, 10, "Patient ID:")
    pdf.cell(0, 10, data.get("patient_id", ""), ln=True)

    pdf.cell(50, 10, "Date:")
    pdf.cell(0, 10, data.get("date", ""), ln=True)

    # Items header
    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(70, 10, "Medicine", border=1)
    pdf.cell(30, 10, "Quantity", border=1)
    pdf.cell(30, 10, "Rate", border=1)
    pdf.cell(30, 10, "Amount", border=1, ln=True)

    # Items rows
    pdf.set_font("Arial", size=12)
    items = data.get("items", [])
    if not items:
        pdf.cell(160, 10, "No items available", border=1, ln=True)
    else:
        for item in items:
            pdf.cell(70, 10, item.get("medicine", ""), border=1)
            pdf.cell(30, 10, str(item.get("quantity", "")), border=1)
            pdf.cell(30, 10, str(item.get("rate", "")), border=1)
            pdf.cell(30, 10, str(item.get("amount", "")), border=1, ln=True)

    # Total amount
    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(130, 10, "Total Amount:", align="R")
    pdf.cell(30, 10, str(data.get("total_amount", "")), ln=True)

    pdf.output(filename)

# Example usage:
data = {
    "document_type": "pharmacy_bill",
    "pharmacy_name": "HealthPlus Pharmacy",
    "patient_name": "John Doe",
    "patient_id": "12345",
    "date": "2025-11-23",
    "items": [
        {"medicine": "Paracetamol", "quantity": 10, "rate": "$0.50", "amount": "$5.00"},
        {"medicine": "Amoxicillin", "quantity": 5, "rate": "$1.00", "amount": "$5.00"},
    ],
    "total_amount": "$10.00"
}

generate_pharmacy_bill_pdf(data, "pharmacy_bill_report.pdf")
