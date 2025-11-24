# Medical Claim Processor using LLM-powered Agents

A FastAPI application that uses LLM-powered AI agents to process medical insurance claim documents and return a final claim decision.
## Tech Stack

FastAPI (async), PostgreSQL, SQLAlchemy, Gemini 2.5 Flash (LLM), Docker + Docker Compose

## Setup Steps
- Create Gemini API Key from [Google AI Studio](https://aistudio.google.com/app/api-keys)
- Clone the github repository in your local machine.
- Make sure `docker` and `docker-compose` is installed, if not please install it.
- After cloning create a `.env` file by referring the .env.example file provided in repo. Give proper values to the .env variables including the Gemini API key.
- Run the following command via cmd/terminal

```bash
docker-compose up --build
```
- API will be accesible from the following URL
  - **Method**: POST
  - **URL**: `http://localhost:8000/process-claim`
  - **Content-Type**: multipart/form-data

## Architecture

API Request (Content-Type: multipart/form-data) ➡ Orchestrator ➡ Extraction (LLM) ➡ Classification(LLM) ➡ Validation(LLM) ➡ Final Decision ➡ API Response (JSON)

## AI Tool Usage

- **Primary LLM:** Gemini 2.5 Flash
- Other tools used during development: GPT, Perplexity, Claude
## Prompt Examples

#### Extraction
```
Extract clean readable text from this noisy PDF content.
Ensure formatting is preserved.

TEXT:
{raw_text}
```
#### Classification
```
You are a medical claim PDF classifier.
Classify the document into one of the following:
["bill", "discharge_summary", "id_card", "pharmacy_bill", "claim_form"]

TEXT:
{text}
Respond only with the label.
```
#### Validation
```
You are a strict JSON validator.
Validate cross-document consistency across these insurance claim documents:

```json
{json.dumps(docs, indent=2)}```
 
Check:
 - If patient_name matches across all docs
 - If patient_id matches
 - If hospital_name matches
 - If admission/discharge dates align
 - If bill amount matches line_items

  Return JSON only:

  {{
      "mismatches": ["list of mismatches"]
  }}
```
## Drawbacks

- Lack of comprehensive unit and integration tests
- Limited error handling around AI responses and document parsing
- AI model rate limits affected consistent validation during development
- `Pydantic` models are not fully utilized for strict data validation and schema enforcement

## Bonus
- Fully containerized using `Docker`
- Integrated with `PostgreSQL` to persist processed claim data
- Supports multiple PDF uploads in a single request (Max 3 documents for the Gemini model used here)
- Modular architecture with separate agents for each document type
- Added python scripts for generating pdf which will be needed for testing
## Sample Request / Response 

#### Request:
```
Send PDF documents to the API with Content Type as mutipart/form-data.
```

#### Response Sample 1:

```
{
    "data": {
        "documents": [
            {
                "bill": {
                    "document_type": "bill",
                    "patient_name": "John Doe",
                    "patient_id": "12345",
                    "hospital_name": "General Hospital",
                    "bill_amount": "$500",
                    "bill_date": "2025-11-23",
                    "line_items": [
                        {
                            "description": "X-Ray",
                            "quantity": 1,
                            "price": "$100"
                        },
                        {
                            "description": "Blood Test",
                            "quantity": 2,
                            "price": "$200"
                        },
                        {
                            "description": "Consultation",
                            "quantity": 1,
                            "price": "$200"
                        }
                    ]
                }
            },
            {
                "id_card": {
                    "document_type": "id_card",
                    "name": "John Doe",
                    "dob": "1990-01-01",
                    "gender": "Female",
                    "id_number": "ABC1234567",
                    "issuer": ""
                }
            }
        ],
        "validation": {
            "missing_documents": [
                "discharge_summary"
            ],
            "discrepancies": {
                "mismatches": [
                    "Patient ID mismatch: bill.patient_id '12345' does not match id_card.id_number 'ABC1234567'.",
                    "Admission/discharge dates could not be checked as relevant fields are missing in the provided documents.",
                    "Bill amount mismatch: bill.bill_amount '$500' does not match calculated total from line items '$700'."
                ]
            }
        },
        "claim_decision": {
            "status": "rejected",
            "reason": "Missing required documents"
        }
    }
}

```

#### Response Sample 2:

```
{
    "data": {
        "documents": [
            {
                "bill": {
                    "document_type": "bill",
                    "patient_name": "John Doe",
                    "patient_id": "12345",
                    "hospital_name": "General Hospital",
                    "bill_amount": "$500",
                    "bill_date": "2025-11-23",
                    "line_items": [
                        {
                            "description": "X-Ray",
                            "quantity": 1,
                            "price": "$100"
                        },
                        {
                            "description": "Blood Test",
                            "quantity": 2,
                            "price": "$200"
                        },
                        {
                            "description": "Consultation",
                            "quantity": 1,
                            "price": "$200"
                        }
                    ]
                }
            },
            {
                "id_card": {
                    "document_type": "id_card",
                    "name": "John Doe",
                    "dob": "1990-01-01",
                    "gender": "Female",
                    "id_number": "ABC1234567",
                    "issuer": ""
                }
            },
            {
                "discharge_summary": {
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
            }
        ],
        "validation": {
            "missing_documents": [],
            "discrepancies": {
                "mismatches": [
                    "Patient ID mismatch between Bill and Discharge Summary",
                    "Hospital name mismatch between Bill and Discharge Summary",
                    "Bill date does not fall within the admission and discharge dates",
                    "Bill amount mismatch with line items total"
                ]
            }
        },
        "claim_decision": {
            "status": "manual_review",
            "reason": "Data inconsistencies found"
        }
    }
}
```
