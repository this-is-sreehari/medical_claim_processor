from fpdf import FPDF

def generate_discharge_summary_pdf(data, filename="discharge_summary.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)

    # Title
    pdf.cell(0, 10, txt=f"{data.get('document_type', '').replace('_', ' ').title()}", ln=True, align="C")
    pdf.ln(10)

    # Patient and hospital details
    pdf.set_font("Arial", size=12)
    pdf.cell(50, 10, "Patient Name:")
    pdf.cell(0, 10, data.get("patient_name", ""), ln=True)

    pdf.cell(50, 10, "Patient ID:")
    pdf.cell(0, 10, data.get("patient_id", ""), ln=True)

    pdf.cell(50, 10, "Hospital Name:")
    pdf.cell(0, 10, data.get("hospital_name", ""), ln=True)

    pdf.cell(50, 10, "Admission Date:")
    pdf.cell(0, 10, data.get("admission_date", ""), ln=True)

    pdf.cell(50, 10, "Discharge Date:")
    pdf.cell(0, 10, data.get("discharge_date", ""), ln=True)

    pdf.cell(50, 10, "Diagnosis:")
    pdf.cell(0, 10, data.get("diagnosis", ""), ln=True)

    pdf.cell(50, 10, "Doctor Name:")
    pdf.cell(0, 10, data.get("doctor_name", ""), ln=True)

    # Summary section with multi-line
    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Summary:")
    pdf.ln(5)
    pdf.set_font("Arial", size=12)
    summary_text = data.get("summary", "")
    pdf.multi_cell(0, 10, summary_text)

    pdf.output(filename)

# Example usage:
data = {
    "document_type": "discharge_summary",
    "patient_name": "John Doe",
    "patient_id": "98765",
    "hospital_name": "City Hospital",
    "admission_date": "2025-11-10",
    "discharge_date": "2025-11-18",
    "diagnosis": "Pneumonia",
    "doctor_name": "Dr. Emily Clark",
    "summary": "Patient admitted with pneumonia and treated with antibiotics. Patient's condition improved steadily and was discharged in stable condition."
}

generate_discharge_summary_pdf(data, "discharge_summary_report.pdf")
