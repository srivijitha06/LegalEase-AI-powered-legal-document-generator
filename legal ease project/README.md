# ⚖️ LegalEase

LegalEase is an AI-assisted legal document platform.

## Features

- AI document generation
- Employment contracts
- NDA generation
- Lease agreements
- Freelance agreements
- Service agreements
- Document analysis
- Completeness indicator
- AI rewriting
- Editable document workspace
- PDF export
- DOCX export
- TXT export
- Pastel UI
- Gemini AI
- Local fallback mode

## Project Structure

LegalEase/

├── backend/
│   ├── main.py
│   ├── routes.py
│   ├── models.py
│   ├── config.py
│   └── services/
│       ├── gemini_service.py
│       ├── document_service.py
│       ├── pdf_service.py
│       └── docx_service.py
│
├── frontend/
│   ├── app.py
│   ├── styles.py
│   └── components.py
│
├── templates/
│   ├── employment.py
│   ├── nda.py
│   ├── lease.py
│   ├── freelance.py
│   └── service.py
│
├── .env
├── .env.example
├── requirements.txt
└── README.md

## Installation

Create a virtual environment:

python -m venv venv

Activate on Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

## Start Backend

IMPORTANT:

Run this command from the LegalEase root directory:

uvicorn backhend.main:app --reload

Do NOT use:

uvicorn app:app --reload

because the FastAPI app is defined in `backhend/main.py`.

Backend:

http://127.0.0.1:8000

Swagger API:

http://127.0.0.1:8000/docs

## Start Frontend

Open another terminal.

Activate the environment:

venv\Scripts\activate

Then:

streamlit run frontend/app.py

Frontend:

http://localhost:8501

## Gemini

Add your Gemini API key to .env:

GEMINI_API_KEY=your_key

The application also has local fallback functionality when Gemini is unavailable.

## Legal Notice

LegalEase is an AI-assisted drafting application.

Generated documents should be reviewed by a qualified legal professional before signing, filing or relying on them.