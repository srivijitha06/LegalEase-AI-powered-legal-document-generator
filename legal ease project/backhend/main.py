from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uvicorn


# ============================================================
# LEGALEASE - SMART LEGAL DOCUMENT ASSISTANT
# ============================================================

app = FastAPI(
    title="LegalEase",
    description="Smart Legal Document Assistant",
    version="1.0.0"
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# ============================================================
# DATA MODELS
# ============================================================

class DocumentRequest(BaseModel):
    document_type: str = "General Agreement"
    party_one: str = "Party One"
    party_two: str = "Party Two"
    purpose: str = "General legal agreement"
    date: Optional[str] = None


class AnalyzeRequest(BaseModel):
    document: str


class RewriteRequest(BaseModel):
    document: str
    instruction: str = "Make this document clearer and more professional."


# ============================================================
# HOME PAGE
# ============================================================

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>LegalEase | Smart Legal Assistant</title>

<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family:
        "Segoe UI",
        Arial,
        sans-serif;

    background:
        linear-gradient(
            135deg,
            #fff8f3 0%,
            #f4f0ff 45%,
            #eefaff 100%
        );

    color: #30304a;
    min-height: 100vh;
}


/* ================= NAVBAR ================= */

.navbar {
    width: 100%;
    padding: 20px 7%;

    display: flex;
    justify-content: space-between;
    align-items: center;

    background: rgba(255,255,255,0.75);
    backdrop-filter: blur(15px);

    border-bottom: 1px solid rgba(120,100,160,0.12);

    position: sticky;
    top: 0;
    z-index: 10;
}

.logo {
    display: flex;
    align-items: center;
    gap: 12px;
}

.logo-icon {
    width: 45px;
    height: 45px;

    border-radius: 14px;

    display: flex;
    align-items: center;
    justify-content: center;

    background: #ded6ff;

    font-size: 23px;

    box-shadow:
        0 8px 20px rgba(105,90,180,0.15);
}

.logo-text {
    font-size: 24px;
    font-weight: 800;
    color: #39365c;
}

.logo-text span {
    color: #8d79c7;
}

.nav-status {
    display: flex;
    align-items: center;
    gap: 8px;

    background: #e9f8ef;

    padding: 8px 15px;

    border-radius: 30px;

    font-size: 13px;
    color: #46735a;
}

.status-dot {
    width: 8px;
    height: 8px;

    background: #76c893;

    border-radius: 50%;
}


/* ================= HERO ================= */

.hero {
    padding: 75px 7% 50px;

    display: grid;

    grid-template-columns:
        1.2fr
        0.8fr;

    gap: 50px;

    align-items: center;
}

.hero-badge {
    display: inline-block;

    background: #f0eaff;

    color: #7764b4;

    padding: 9px 17px;

    border-radius: 30px;

    font-size: 13px;
    font-weight: 700;

    margin-bottom: 20px;
}

.hero h1 {
    font-size: clamp(42px, 6vw, 72px);

    line-height: 1.05;

    color: #35334f;

    margin-bottom: 22px;
}

.hero h1 span {
    color: #907dcc;
}

.hero p {
    font-size: 18px;

    line-height: 1.7;

    color: #69677d;

    max-width: 650px;

    margin-bottom: 30px;
}

.hero-buttons {
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
}

.primary-button,
.secondary-button {
    border: none;

    padding: 14px 23px;

    border-radius: 14px;

    font-size: 15px;

    font-weight: 700;

    cursor: pointer;

    transition: 0.25s;
}

.primary-button {
    background: #9180d1;
    color: white;

    box-shadow:
        0 10px 25px rgba(117,98,181,0.25);
}

.primary-button:hover {
    transform: translateY(-3px);
    background: #7d6bbd;
}

.secondary-button {
    background: white;
    color: #68617d;

    border: 1px solid #e5e0ef;
}

.secondary-button:hover {
    transform: translateY(-3px);
}


/* ================= HERO CARD ================= */

.hero-card {
    position: relative;

    min-height: 350px;

    background: rgba(255,255,255,0.78);

    border: 1px solid rgba(255,255,255,0.9);

    border-radius: 30px;

    padding: 30px;

    box-shadow:
        0 25px 60px rgba(91,79,130,0.13);

    overflow: hidden;
}

.hero-card::before {
    content: "";

    position: absolute;

    width: 180px;
    height: 180px;

    border-radius: 50%;

    background: #eee7ff;

    top: -80px;
    right: -50px;
}

.document-icon {
    width: 70px;
    height: 85px;

    background: #fff;

    border-radius: 10px;

    margin-bottom: 25px;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 38px;

    box-shadow:
        0 12px 30px rgba(80,70,110,0.12);
}

.hero-card h3 {
    font-size: 22px;
    margin-bottom: 12px;
}

.hero-card p {
    font-size: 14px;
    margin-bottom: 22px;
}

.feature-line {
    display: flex;
    align-items: center;

    gap: 10px;

    padding: 11px 0;

    color: #69677d;

    font-size: 14px;
}

.feature-line span {
    width: 27px;
    height: 27px;

    border-radius: 8px;

    display: flex;
    align-items: center;
    justify-content: center;

    background: #f1edff;
}


/* ================= FEATURES ================= */

.section {
    padding: 50px 7%;
}

.section-title {
    text-align: center;

    margin-bottom: 35px;
}

.section-title h2 {
    font-size: 34px;
    color: #39364f;
}

.section-title p {
    margin-top: 10px;
    color: #777388;
}

.feature-grid {
    display: grid;

    grid-template-columns:
        repeat(4, 1fr);

    gap: 18px;
}

.feature {
    padding: 25px;

    background: rgba(255,255,255,0.78);

    border-radius: 22px;

    border: 1px solid #eeeaf5;

    transition: 0.25s;
}

.feature:hover {
    transform: translateY(-6px);

    box-shadow:
        0 18px 35px rgba(88,78,120,0.10);
}

.feature-icon {
    width: 50px;
    height: 50px;

    border-radius: 15px;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 23px;

    margin-bottom: 17px;
}

.purple {
    background: #eee7ff;
}

.peach {
    background: #ffeadf;
}

.blue {
    background: #e2f4ff;
}

.green {
    background: #e4f7eb;
}

.feature h3 {
    margin-bottom: 9px;
}

.feature p {
    color: #777388;

    font-size: 14px;

    line-height: 1.6;
}


/* ================= GENERATOR ================= */

.generator {
    max-width: 1050px;

    margin: 20px auto 70px;

    background: rgba(255,255,255,0.84);

    border-radius: 30px;

    padding: 35px;

    box-shadow:
        0 25px 70px rgba(87,75,120,0.13);

    border: 1px solid #eeeaf5;
}

.generator-header {
    display: flex;
    align-items: center;

    gap: 15px;

    margin-bottom: 30px;
}

.generator-header-icon {
    width: 55px;
    height: 55px;

    background: #eee7ff;

    border-radius: 15px;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 25px;
}

.generator-header h2 {
    font-size: 25px;
}

.generator-header p {
    color: #777388;

    font-size: 13px;

    margin-top: 4px;
}

.form-grid {
    display: grid;

    grid-template-columns:
        1fr 1fr;

    gap: 20px;
}

.form-group {
    display: flex;
    flex-direction: column;

    gap: 8px;
}

.form-group.full {
    grid-column: 1 / -1;
}

label {
    font-size: 13px;

    font-weight: 700;

    color: #56536c;
}

input,
select,
textarea {
    width: 100%;

    border: 1px solid #e5e1ed;

    border-radius: 13px;

    padding: 13px 15px;

    font-size: 14px;

    color: #45435b;

    background: #fcfbff;

    outline: none;

    transition: 0.2s;
}

input:focus,
select:focus,
textarea:focus {
    border-color: #a596dc;

    box-shadow:
        0 0 0 4px rgba(165,150,220,0.12);
}

textarea {
    resize: vertical;

    min-height: 110px;
}

.generate-button {
    width: 100%;

    margin-top: 25px;

    padding: 15px;

    border: none;

    border-radius: 14px;

    background: #8e7ac9;

    color: white;

    font-size: 15px;

    font-weight: 700;

    cursor: pointer;

    transition: 0.25s;
}

.generate-button:hover {
    background: #7864b6;

    transform: translateY(-2px);
}


/* ================= RESULT ================= */

#result {
    display: none;

    margin-top: 25px;

    background: #f8f5ff;

    border: 1px solid #e5ddfa;

    border-radius: 18px;

    padding: 22px;
}

#result h3 {
    margin-bottom: 12px;
}

#result pre {
    white-space: pre-wrap;

    font-family:
        "Segoe UI",
        Arial,
        sans-serif;

    line-height: 1.7;

    color: #48445b;

    font-size: 13px;
}


/* ================= FOOTER ================= */

footer {
    padding: 30px 7%;

    text-align: center;

    color: #858195;

    font-size: 13px;
}

footer strong {
    color: #7361a9;
}


/* ================= RESPONSIVE ================= */

@media(max-width: 900px) {

    .hero {
        grid-template-columns: 1fr;
    }

    .feature-grid {
        grid-template-columns:
            repeat(2, 1fr);
    }

}

@media(max-width: 600px) {

    .hero {
        padding-top: 45px;
    }

    .hero h1 {
        font-size: 43px;
    }

    .form-grid {
        grid-template-columns: 1fr;
    }

    .form-group.full {
        grid-column: auto;
    }

    .feature-grid {
        grid-template-columns: 1fr;
    }

    .navbar {
        padding: 16px 5%;
    }

    .nav-status {
        display: none;
    }

}

</style>

</head>


<body>


<!-- =====================================================
     NAVIGATION
====================================================== -->

<nav class="navbar">

    <div class="logo">

        <div class="logo-icon">
            ⚖️
        </div>

        <div class="logo-text">
            Legal<span>Ease</span>
        </div>

    </div>

    <div class="nav-status">
        <div class="status-dot"></div>
        AI Assistant Online
    </div>

</nav>


<!-- =====================================================
     HERO
====================================================== -->

<section class="hero">

    <div>

        <div class="hero-badge">
            ✨ SMART LEGAL DOCUMENT ASSISTANT
        </div>

        <h1>
            Legal work,
            <span>made easier.</span>
        </h1>

        <p>
            Create structured legal document drafts,
            review important clauses and organize your
            legal workflow with a simple, modern assistant.
        </p>

        <div class="hero-buttons">

            <button
                class="primary-button"
                onclick="scrollToGenerator()">
                Create a Document →
            </button>

            <button
                class="secondary-button"
                onclick="showFeatures()">
                Explore Features
            </button>

        </div>

    </div>


    <div class="hero-card">

        <div class="document-icon">
            📄
        </div>

        <h3>
            Your Legal Workspace
        </h3>

        <p>
            Draft, organize and review documents
            from one peaceful workspace.
        </p>

        <div class="feature-line">
            <span>✓</span>
            Smart document drafting
        </div>

        <div class="feature-line">
            <span>✓</span>
            Clause checklist
        </div>

        <div class="feature-line">
            <span>✓</span>
            Professional formatting
        </div>

        <div class="feature-line">
            <span>✓</span>
            Easy document workflow
        </div>

    </div>

</section>


<!-- =====================================================
     FEATURES
====================================================== -->

<section
    class="section"
    id="features">

    <div class="section-title">

        <h2>
            Everything in one place
        </h2>

        <p>
            A simple workspace designed for modern
            legal document preparation.
        </p>

    </div>


    <div class="feature-grid">

        <div class="feature">

            <div class="feature-icon purple">
                ✍️
            </div>

            <h3>
                Draft
            </h3>

            <p>
                Create structured document drafts
                using simple information.
            </p>

        </div>


        <div class="feature">

            <div class="feature-icon peach">
                🔍
            </div>

            <h3>
                Analyze
            </h3>

            <p>
                Check documents for common clauses
                and identify potentially missing sections.
            </p>

        </div>


        <div class="feature">

            <div class="feature-icon blue">
                🧠
            </div>

            <h3>
                Simplify
            </h3>

            <p>
                Turn complicated legal wording into
                clearer language.
            </p>

        </div>


        <div class="feature">

            <div class="feature-icon green">
                📁
            </div>

            <h3>
                Organize
            </h3>

            <p>
                Build a consistent workflow for
                frequently used document types.
            </p>

        </div>

    </div>

</section>


<!-- =====================================================
     DOCUMENT GENERATOR
====================================================== -->

<section
    class="generator"
    id="generator">

    <div class="generator-header">

        <div class="generator-header-icon">
            ✨
        </div>

        <div>

            <h2>
                Smart Document Creator
            </h2>

            <p>
                Fill in the details and create a structured draft.
            </p>

        </div>

    </div>


    <div class="form-grid">


        <div class="form-group">

            <label>
                Document Type
            </label>

            <select id="document_type">

                <option>
                    Employment Agreement
                </option>

                <option>
                    Non-Disclosure Agreement
                </option>

                <option>
                    Lease Agreement
                </option>

                <option>
                    Freelance Agreement
                </option>

                <option>
                    Service Agreement
                </option>

                <option>
                    General Agreement
                </option>

            </select>

        </div>


        <div class="form-group">

            <label>
                Date
            </label>

            <input
                type="date"
                id="date">

        </div>


        <div class="form-group">

            <label>
                First Party
            </label>

            <input
                type="text"
                id="party_one"
                placeholder="Enter first party name">

        </div>


        <div class="form-group">

            <label>
                Second Party
            </label>

            <input
                type="text"
                id="party_two"
                placeholder="Enter second party name">

        </div>


        <div class="form-group full">

            <label>
                Purpose / Agreement Details
            </label>

            <textarea
                id="purpose"
                placeholder="Describe the purpose of the agreement..."></textarea>

        </div>


    </div>


    <button
        class="generate-button"
        onclick="generateDocument()">

        ✨ Generate Legal Document

    </button>


    <div id="result">

        <h3>
            📄 Generated Draft
        </h3>

        <pre id="resultText"></pre>

    </div>

</section>


<!-- =====================================================
     FOOTER
====================================================== -->

<footer>

    <strong>LegalEase</strong>
    · Smart legal document assistance

    <br><br>

    AI-assisted drafts should be reviewed carefully
    before signing or relying upon them.

</footer>


<script>


function scrollToGenerator() {

    document
        .getElementById("generator")
        .scrollIntoView({
            behavior: "smooth"
        });

}


function showFeatures() {

    document
        .getElementById("features")
        .scrollIntoView({
            behavior: "smooth"
        });

}


async function generateDocument() {

    const documentType =
        document.getElementById(
            "document_type"
        ).value;

    const date =
        document.getElementById(
            "date"
        ).value;

    const partyOne =
        document.getElementById(
            "party_one"
        ).value;

    const partyTwo =
        document.getElementById(
            "party_two"
        ).value;

    const purpose =
        document.getElementById(
            "purpose"
        ).value;


    if (!partyOne || !partyTwo || !purpose) {

        alert(
            "Please complete the party names and purpose."
        );

        return;
    }


    const button =
        document.querySelector(
            ".generate-button"
        );

    button.innerText =
        "Creating your document...";

    button.disabled = true;


    try {

        const response =
            await fetch(
                "/generate",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({

                        document_type:
                            documentType,

                        party_one:
                            partyOne,

                        party_two:
                            partyTwo,

                        purpose:
                            purpose,

                        date:
                            date

                    })
                }
            );


        const data =
            await response.json();


        document
            .getElementById("result")
            .style.display = "block";


        document
            .getElementById("resultText")
            .textContent =
                data.document;


        document
            .getElementById("result")
            .scrollIntoView({
                behavior: "smooth"
            });

    }

    catch (error) {

        alert(
            "Something went wrong. Please make sure the server is running."
        );

    }

    finally {

        button.innerText =
            "✨ Generate Legal Document";

        button.disabled = false;

    }

}


</script>


</body>

</html>
"""


# ============================================================
# ROUTES
# ============================================================

@app.get("/", response_class=HTMLResponse)
def home():
    return HTML_PAGE


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "application": "LegalEase",
        "message": "LegalEase server is running."
    }


@app.get("/status")
def status():

    return {
        "application": "LegalEase",
        "version": "1.0.0",
        "status": "online",
        "time": datetime.now().isoformat()
    }


@app.get("/about")
def about():

    return {
        "application": "LegalEase",
        "description": "Smart Legal Document Assistant",
        "features": [
            "Document drafting",
            "Document analysis",
            "Document rewriting",
            "Legal templates",
            "Pastel user interface"
        ]
    }


@app.get("/templates")
def templates():

    return {
        "templates": [
            {
                "name": "Employment Agreement",
                "type": "employment"
            },
            {
                "name": "Non-Disclosure Agreement",
                "type": "nda"
            },
            {
                "name": "Lease Agreement",
                "type": "lease"
            },
            {
                "name": "Freelance Agreement",
                "type": "freelance"
            },
            {
                "name": "Service Agreement",
                "type": "service"
            }
        ]
    }


# ============================================================
# DOCUMENT GENERATION
# ============================================================

@app.post("/generate")
def generate_document(request: DocumentRequest):

    date_value = request.date

    if not date_value:
        date_value = datetime.now().strftime("%d %B %Y")


    document = f"""
============================================================
                         LEGALEASE
                 {request.document_type.upper()}
============================================================

DATE
{date_value}


PARTY ONE
{request.party_one}


PARTY TWO
{request.party_two}


1. PURPOSE
------------------------------------------------------------

{request.purpose}


2. AGREEMENT
------------------------------------------------------------

The parties identified above agree to enter into this
agreement based on the purpose described above.

The specific rights, responsibilities, obligations,
payments, timelines and other applicable terms should
be clearly defined by the parties.


3. RESPONSIBILITIES
------------------------------------------------------------

Each party shall perform the responsibilities agreed
between the parties and shall provide the information
or services required under the agreement.


4. CONFIDENTIALITY
------------------------------------------------------------

Where applicable, confidential information should be
protected from unauthorized disclosure.


5. PAYMENT
------------------------------------------------------------

Where payment is applicable, the parties should clearly
define the amount, payment schedule, method of payment
and applicable conditions.


6. TERMINATION
------------------------------------------------------------

The parties should define the circumstances under which
this agreement may be terminated and any applicable
notice requirements.


7. DISPUTE RESOLUTION
------------------------------------------------------------

The parties should specify the appropriate process for
handling disputes arising from this agreement.


8. GOVERNING LAW
------------------------------------------------------------

The applicable governing law and jurisdiction should be
specified by the parties.


9. SIGNATURES
------------------------------------------------------------


PARTY ONE

Name:
_______________________________________________

Signature:
_______________________________________________

Date:
_______________________________________________



PARTY TWO

Name:
_______________________________________________

Signature:
_______________________________________________

Date:
_______________________________________________


============================================================
                       LEGALEASE NOTICE
============================================================

This document is an AI-assisted draft.

Review names, dates, amounts, obligations, jurisdiction
and all other information carefully before using it.

This application provides document assistance and does
not replace advice from a qualified legal professional.

============================================================
"""

    return {
        "success": True,
        "document_type": request.document_type,
        "created_at": datetime.now().isoformat(),
        "document": document
    }


# ============================================================
# DOCUMENT ANALYSIS
# ============================================================

@app.post("/analyze")
def analyze_document(request: AnalyzeRequest):

    document = request.document.strip()

    if not document:

        return {
            "success": False,
            "message": "Please provide a document."
        }


    text = document.lower()


    checks = {

        "Signature": "signature" in text,

        "Payment": "payment" in text,

        "Termination": "termination" in text,

        "Confidentiality":
            "confidential" in text,

        "Jurisdiction":
            "jurisdiction" in text,

        "Governing Law":
            "governing law" in text,

        "Effective Date":
            "effective date" in text

    }


    completed = sum(checks.values())

    total = len(checks)

    score = int(
        (completed / total) * 100
    )


    missing = [

        name

        for name, found
        in checks.items()

        if not found

    ]


    return {

        "success": True,

        "score": score,

        "checks": checks,

        "missing_sections": missing,

        "message":
            "Basic document checklist completed."

    }


# ============================================================
# DOCUMENT REWRITE
# ============================================================

@app.post("/rewrite")
def rewrite_document(request: RewriteRequest):

    document = request.document.strip()

    if not document:

        return {
            "success": False,
            "message": "Please provide document text."
        }


    rewritten = f"""
============================================================
                    LEGALEASE
                 DOCUMENT REVIEW
============================================================

REQUESTED IMPROVEMENT

{request.instruction}


DOCUMENT

{document}


============================================================

REVIEW NOTE

This feature currently prepares the document for review.
For actual legal interpretation or advice, consult a
qualified legal professional.

============================================================
"""


    return {

        "success": True,

        "instruction":
            request.instruction,

        "document":
            rewritten

    }


# ============================================================
# SERVER START
# ============================================================

if __name__ == "__main__":

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        reload=False
    )