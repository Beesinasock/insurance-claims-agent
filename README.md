# Autonomous Insurance Claims Processing Agent

## Developed By

**Chandresh Kushal G R**

---

## Overview

This project implements a lightweight **Autonomous Insurance Claims Processing Agent** that automates the initial processing of First Notice of Loss (FNOL) documents.

The application extracts structured information from insurance claim documents, validates the extracted information, applies predefined business routing rules, and generates standardized JSON output.

The project is designed using a modular architecture where every module has a single responsibility, making the application easy to understand, maintain, and extend.

---

## Features

- Supports PDF and TXT FNOL documents
- Automatically processes multiple documents
- Extracts all required claim information
- Detects missing mandatory fields
- Performs basic data validation
- Routes claims based on business rules
- Generates JSON output
- Saves one JSON file per processed document
- Modular and maintainable project structure

---

## Project Structure

```text
insurance-claims-agent/
│
├── input/
│   ├── claim1.txt
│   ├── claim2.txt
│   ├── claim3.txt
│   ├── claim4.txt
│   └── claim5.txt
│
├── output/
│   ├── claim1.json
│   ├── claim2.json
│   └── ...
│
├── src/
│   ├── __init__.py
│   ├── parser.py
│   ├── extractor.py
│   ├── validator.py
│   ├── router.py
│   ├── json_builder.py
│   ├── constants.py
│   └── utils.py
│
├── tests/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## System Architecture

```text
                 FNOL Document
              (PDF / TXT Input)
                      │
                      ▼
               Document Parser
                      │
                      ▼
               Field Extractor
                      │
                      ▼
                Claim Validator
                      │
                      ▼
                Routing Engine
                      │
                      ▼
                JSON Generator
                      │
                      ▼
               JSON Output File
```

---

## Workflow

1. Read every PDF/TXT document from the `input` folder.
2. Convert the document into plain text.
3. Extract required claim fields.
4. Validate extracted information.
5. Apply business routing rules.
6. Generate JSON output.
7. Save the JSON file inside the `output` folder.

---

## Extracted Fields

### Policy Information

- Policy Number
- Policyholder Name
- Effective Dates

### Incident Information

- Incident Date
- Incident Time
- Location
- Description

### Involved Parties

- Claimant
- Third Parties
- Contact Details

### Asset Details

- Asset Type
- Asset ID
- Estimated Damage

### Other Information

- Claim Type
- Attachments
- Initial Estimate

---

## Validation

The validator performs the following checks:

- Missing mandatory fields
- Empty field detection
- Numeric validation
  - Estimated Damage
  - Initial Estimate

---

## Business Rules

| Condition | Route |
|-----------|-------|
| Description contains **fraud**, **staged**, or **inconsistent** | Investigation Flag |
| Mandatory field missing | Manual Review |
| Claim Type = Injury | Specialist Queue |
| Estimated Damage < ₹25,000 | Fast-track |
| Otherwise | Normal Processing |

---

## Routing Priority

If multiple routing conditions are satisfied, the following priority is applied:

1. Investigation Flag
2. Manual Review
3. Specialist Queue
4. Fast-track
5. Normal Processing

---

## Output Format

Example:

```json
{
    "extractedFields": {
        "Policy Number": "POL100001",
        "Policyholder Name": "John Smith"
    },
    "missingFields": [],
    "recommendedRoute": "Fast-track",
    "reasoning": "Estimated damage is below ₹25,000."
}
```

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Core programming language |
| pdfplumber | Read PDF documents |
| re | Regular expression based extraction |
| json | JSON generation |
| pathlib | File handling |

---

## Installation

Clone the repository.

```bash
git clone https://github.com/Beesinasock/insurance-claims-agent.git
```

Move into the project directory.

```bash
cd insurance-claims-agent
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the environment.

### Windows (Command Prompt)

```bash
venv\Scripts\activate
```

### Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Running the Project

Place all FNOL documents inside the `input` folder.

Run:

```bash
python main.py
```

The application automatically processes every document and stores the generated JSON files inside the `output` directory.

---

## Sample Console Output

```text
Processing File: claim1.txt

Extracted Fields

Missing Fields: []

Recommended Route:
Fast-track

Reason:
Estimated damage is below ₹25,000.

JSON Saved:
output/claim1.json
```

---

## Assumptions

- FNOL documents contain machine-readable text.
- PDF files are text-based.
- Documents follow a structured format.
- Routing rules are deterministic.

---

## Future Improvements

- AI-assisted extraction for unstructured documents
- OCR support for scanned PDFs
- REST API implementation
- Database integration
- Confidence scoring
- Machine learning based fraud detection
- Docker deployment

---

## Demo Video

https://drive.google.com/file/d/1oZiby35GDlNG-dw7y5bXZCW-KaEh36IS/view?usp=sharing


---

## Author

**Chandresh Kushal G R**

Assessment Submission

Autonomous Insurance Claims Processing Agent
