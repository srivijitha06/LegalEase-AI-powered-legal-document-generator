import json

from backend.config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
)

try:
    from google import genai
except ImportError:
    genai = None


def get_client():

    if not GEMINI_API_KEY:
        return None

    if genai is None:
        return None

    try:
        return genai.Client(
            api_key=GEMINI_API_KEY
        )
    except Exception:
        return None


def generate_with_gemini(
    document_type,
    parties,
    terms,
    effective_date,
    jurisdiction,
    language,
):

    client = get_client()

    if client is None:
        return None

    prompt = f"""
You are LegalEase, an AI-assisted legal document drafting system.

Create a professional draft for:

DOCUMENT TYPE:
{document_type}

PARTIES:
{parties}

EFFECTIVE DATE:
{effective_date}

JURISDICTION:
{jurisdiction}

LANGUAGE:
{language}

USER TERMS:
{terms}

Instructions:

1. Use only the facts supplied by the user.
2. Do not invent names, dates, addresses or financial values.
3. Create a professional document.
4. Use numbered sections.
5. Include signature sections.
6. Include an AI-generated draft notice.
7. Do not provide legal advice.
8. Do not use markdown code fences.
"""

    try:

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
        )

        text = getattr(
            response,
            "text",
            None,
        )

        if text:
            return text.strip()

    except Exception:
        return None

    return None


def analyze_with_gemini(document):

    client = get_client()

    if client is None:
        return None

    prompt = f"""
Analyze this legal document.

DOCUMENT:
{document}

Return ONLY JSON:

{{
    "summary": "short summary",
    "key_clauses": [],
    "review_items": [],
    "strengths": [],
    "completeness_score": 0
}}

The score must be between 0 and 100.

Do not give legal advice.
Identify information that should be reviewed.
"""

    try:

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
        )

        text = getattr(
            response,
            "text",
            "",
        )

        text = text.replace(
            "```json",
            "",
        ).replace(
            "```",
            "",
        ).strip()

        data = json.loads(text)

        score = int(
            data.get(
                "completeness_score",
                50,
            )
        )

        score = max(
            0,
            min(
                100,
                score,
            ),
        )

        return {
            "summary": str(
                data.get(
                    "summary",
                    "",
                )
            ),
            "key_clauses": [
                str(x)
                for x in data.get(
                    "key_clauses",
                    [],
                )
            ],
            "review_items": [
                str(x)
                for x in data.get(
                    "review_items",
                    [],
                )
            ],
            "strengths": [
                str(x)
                for x in data.get(
                    "strengths",
                    [],
                )
            ],
            "completeness_score": score,
        }

    except Exception:
        return None


def rewrite_with_gemini(
    document,
    instruction,
):

    client = get_client()

    if client is None:
        return None

    prompt = f"""
You are LegalEase.

Rewrite the document according to the instruction.

DOCUMENT:
{document}

INSTRUCTION:
{instruction}

Rules:

- Preserve all factual information.
- Do not invent facts.
- Do not remove important clauses unless requested.
- Return only the revised document.
- Do not use markdown code fences.
"""

    try:

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
        )

        text = getattr(
            response,
            "text",
            None,
        )

        if text:
            return text.strip()

    except Exception:
        return None

    return None