# Autonomous Insurance Claims Processing Agent

## Overview

This project implements a lightweight Autonomous Insurance Claims Processing Agent capable of processing First Notice of Loss (FNOL) documents. The application extracts structured information from insurance claim documents, validates the extracted data, applies predefined business routing rules, and generates standardized JSON output.

The solution is designed using a modular architecture where each component has a single responsibility, making the codebase maintainable, extensible, and easy to understand.

The application supports both PDF and TXT document formats and automatically processes all supported files placed inside the input directory.

---

# Problem Statement

Insurance companies receive thousands of First Notice of Loss (FNOL) documents every day. Manual processing of these documents is time-consuming, repetitive, and prone to human error.

This project automates the initial stage of claim processing by:

* Reading FNOL documents
* Extracting important claim information
* Identifying missing mandatory information
* Detecting basic inconsistencies
* Applying predefined routing rules
* Producing structured JSON output for downstream systems

---

# Objectives

The primary objectives of this project are:

* Automate extraction of structured claim information.
* Reduce manual effort required during claim intake.
* Identify incomplete claim submissions.
* Apply deterministic business routing rules.
* Produce standardized JSON output.
* Demonstrate modular software design suitable for future enhancements.

---

# Features

The application currently provides the following functionality:

* Support for PDF and TXT FNOL documents
* Automatic batch processing of multiple documents
* Extraction of all mandatory claim fields
* Detection of missing mandatory fields
* Basic validation of extracted information
* Business rule based claim routing
* Automatic JSON generation
* Automatic output file creation
* Clean modular architecture
* Easily extendable design

---

# Project Structure

```
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
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# System Architecture

```
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

The system follows a sequential processing pipeline where each module performs a single well-defined responsibility.

---

# Processing Workflow

## Step 1 — Document Reading

The application scans the `input` directory and identifies all supported files.

Supported formats:

* PDF
* TXT

Each document is converted into plain text before further processing.

---

## Step 2 — Field Extraction

The extractor module identifies and extracts all required claim information using Regular Expressions.

The following information is extracted:

### Policy Information

* Policy Number
* Policyholder Name
* Effective Dates

### Incident Information

* Incident Date
* Incident Time
* Location
* Description

### Involved Parties

* Claimant
* Third Parties
* Contact Details

### Asset Information

* Asset Type
* Asset ID
* Estimated Damage

### Additional Information

* Claim Type
* Attachments
* Initial Estimate

Extracted data is stored as a Python dictionary for further processing.

---

## Step 3 — Validation

The validator checks the extracted information for completeness and consistency.

Current validation includes:

### Mandatory Field Validation

Checks whether all required fields are present.

Example:

```
Incident Time

Missing
```

---

### Empty Value Validation

Fields containing empty strings are treated as missing.

Example:

```
Location:
```

---

### Numeric Validation

The following fields must contain valid numeric values:

* Estimated Damage
* Initial Estimate

---

# Business Routing Rules

The routing engine applies deterministic business rules exactly as specified in the assessment.

The following routing logic is implemented.

## Rule 1

If the claim description contains any of the following keywords

* fraud
* staged
* inconsistent

The claim is routed to:

```
Investigation Flag
```

---

## Rule 2

If any mandatory field is missing

The claim is routed to

```
Manual Review
```

---

## Rule 3

If the claim type is

```
Injury
```

The claim is routed to

```
Specialist Queue
```

---

## Rule 4

If

```
Estimated Damage < ₹25,000
```

The claim is routed to

```
Fast-track
```

---

## Rule 5

If none of the above conditions apply

The claim is routed to

```
Normal Processing
```

---

# Routing Priority

Multiple routing rules may match the same claim.

To avoid ambiguity, the following priority order is used.

| Priority | Route              |
| -------- | ------------------ |
| 1        | Investigation Flag |
| 2        | Manual Review      |
| 3        | Specialist Queue   |
| 4        | Fast-track         |
| 5        | Normal Processing  |

For example,

If a claim contains the keyword "fraud" and also has damage below ₹25,000, the claim will be routed to **Investigation Flag** because investigation has higher priority.

---

# Output Format

Each processed document generates one JSON file.

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

# Module Description

## parser.py

Responsible for reading PDF and TXT files and converting them into plain text.

No extraction or validation is performed in this module.

---

## extractor.py

Responsible for extracting all required information using Regular Expressions.

The extractor is isolated from the remaining modules to improve maintainability.

---

## validator.py

Responsible for validating extracted information.

Current checks include:

* Missing fields
* Empty fields
* Numeric validation

---

## router.py

Contains all business routing rules.

No extraction or validation logic is implemented inside this module.

---

## json_builder.py

Constructs the final JSON object and writes it into the output directory.

---

## constants.py

Contains reusable constants including:

* Required fields
* Threshold values
* Routing keywords

Centralizing constants improves maintainability.

---

## main.py

Acts as the application entry point.

It orchestrates the complete workflow without containing business logic.

---

# Technologies Used

| Technology | Purpose                                    |
| ---------- | ------------------------------------------ |
| Python 3   | Core programming language                  |
| pdfplumber | PDF text extraction                        |
| pathlib    | File handling                              |
| json       | JSON generation                            |
| re         | Pattern matching using Regular Expressions |

---

# Installation

Clone the repository.

```
git clone <repository-url>
```

Navigate to the project.

```
cd insurance-claims-agent
```

Create a virtual environment.

Windows

```
python -m venv venv
```

Activate the virtual environment.

Command Prompt

```
venv\Scripts\activate
```

PowerShell

```
.\venv\Scripts\Activate.ps1
```

Install dependencies.

```
pip install -r requirements.txt
```

---

# Running the Application

Place all FNOL documents inside the `input` directory.

Run:

```
python main.py
```

The application automatically processes every supported document.

Generated JSON files are written to the `output` directory.

---

# Sample Execution

```
Processing File: claim1.txt

Document Read Successfully

Fields Extracted Successfully

Validation Completed

Routing Completed

JSON Generated

Output Saved:
output/claim1.json
```

---

# Assumptions

The following assumptions were made during implementation.

* FNOL documents contain machine-readable text.
* PDF files are not scanned images.
* Documents follow a reasonably structured format.
* Routing rules are deterministic.
* Business rules provided in the assessment are considered authoritative.

---

# Design Decisions

Several design decisions were made to improve maintainability.

* Business logic is separated into independent modules.
* Validation is independent of routing.
* JSON generation is isolated from processing logic.
* The application processes multiple files automatically.
* Each module follows the Single Responsibility Principle.

---

# Limitations

Current limitations include:

* OCR is not implemented for scanned PDFs.
* Extraction primarily relies on structured document labels.
* Validation is limited to basic consistency checks.
* Routing rules are static.

---

# Future Improvements

Potential enhancements include:

* AI-assisted extraction for unstructured documents
* OCR support for scanned PDFs
* Support for Microsoft Word documents
* REST API implementation using FastAPI or Django
* Database integration
* Claim history tracking
* Confidence scoring
* Machine learning based fraud detection
* Docker deployment
* Unit and integration testing

---

# Author

**Chandresh Kushal G R**

Assessment Submission

Autonomous Insurance Claims Processing Agent
#   i n s u r a n c e - c l a i m s - a g e n t  
 