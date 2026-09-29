from io import BytesIO

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from backend.models import (
    AnalyzeRequest,
    DocumentRequest,
    RewriteRequest,
)

from backend.services.document_service import create_local_document

from backend.services.gemini_service import (
    generate_with_gemini,
    analyze_with_gemini,
    rewrite_with_gemini,
)

from backend.services.pdf_service import create_pdf
from backend.services.docx_service import create_docx


router = APIRouter(prefix="/api", tags=["LegalEase"])


def generate_document(request: DocumentRequest):

    ai_document = generate_with_gemini(
        document_type=request.document_type,
        parties=request.parties,
        terms=request.terms,
        effective_date=request.effective_date,
        jurisdiction=request.jurisdiction,
        language=request.language,
    )

    if ai_document:
        return ai_document, "Gemini AI"

    local_document = create_local_document(
        document_type=request.document_type,
        parties=request.parties,
        terms=request.terms,
        effective_date=request.effective_date,
        jurisdiction=request.jurisdiction,
    )

    return local_document, "LegalEase Local Engine"


@router.post("/generate")
def generate(request: DocumentRequest):

    document, mode = generate_document(request)

    return {
        "success": True,
        "document": document,
        "mode": mode,
        "message": "Document generated successfully.",
    }


@router.post("/analyze")
def analyze(request: AnalyzeRequest):

    result = analyze_with_gemini(request.document)

    if result:
        return {
            "success": True,
            "mode": "Gemini AI",
            **result,
        }

    text = request.document.lower()

    checks = {
        "signature": "Signature section should be reviewed.",
        "effective": "Effective date should be confirmed.",
        "termination": "Termination conditions should be reviewed.",
        "payment": "Payment terms should be confirmed.",
        "confidential": "Confidentiality provisions should be checked.",
    }

    review_items = []

    for keyword, message in checks.items():

        if keyword not in text:
            review_items.append(message)

    score = max(
        20,
        100 - (len(review_items) * 15),
    )

    clauses = []

    for line in request.document.splitlines():

        line = line.strip()

        if line:
            clauses.append(line)

    return {
        "success": True,
        "mode": "LegalEase Local Analyzer",
        "summary": (
            "LegalEase scanned the document using its "
            "local clause-analysis engine."
        ),
        "key_clauses": clauses[:8],
        "review_items": review_items,
        "strengths": [
            "Document was successfully processed.",
            "Content is available for editing and review.",
        ],
        "completeness_score": score,
    }


@router.post("/rewrite")
def rewrite(request: RewriteRequest):

    rewritten = rewrite_with_gemini(
        request.document,
        request.instruction,
    )

    if rewritten:

        return {
            "success": True,
            "document": rewritten,
            "mode": "Gemini AI",
        }

    return {
        "success": True,
        "document": request.document,
        "mode": "Local Safe Mode",
        "message": (
            "Gemini is unavailable. The original document "
            "was preserved safely."
        ),
    }


@router.post("/export/pdf")
def export_pdf(request: DocumentRequest):

    document, _ = generate_document(request)

    pdf_data = create_pdf(
        document,
        request.document_type,
    )

    return StreamingResponse(
        BytesIO(pdf_data),
        media_type="application/pdf",
        headers={
            "Content-Disposition":
            'attachment; filename="LegalEase_Document.pdf"'
        },
    )


@router.post("/export/docx")
def export_docx(request: DocumentRequest):

    document, _ = generate_document(request)

    docx_data = create_docx(
        document,
        request.document_type,
    )

    return StreamingResponse(
        BytesIO(docx_data),
        media_type=(
            "application/vnd.openxmlformats-officedocument."
            "wordprocessingml.document"
        ),
        headers={
            "Content-Disposition":
            'attachment; filename="LegalEase_Document.docx"'
        },
    )