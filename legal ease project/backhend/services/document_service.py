from templates.employment import create_template as employment
from templates.nda import create_template as nda
from templates.lease import create_template as lease
from templates.freelance import create_template as freelance
from templates.service import create_template as service


def normalize(value):

    return (
        value.lower()
        .replace("-", " ")
        .replace("_", " ")
        .strip()
    )


def create_local_document(
    document_type,
    parties,
    terms,
    effective_date,
    jurisdiction,
):

    key = normalize(document_type)

    if "employment" in key:

        return employment(
            parties,
            terms,
            effective_date,
            jurisdiction,
        )

    if "nda" in key or "non disclosure" in key:

        return nda(
            parties,
            terms,
            effective_date,
            jurisdiction,
        )

    if "lease" in key:

        return lease(
            parties,
            terms,
            effective_date,
            jurisdiction,
        )

    if "freelance" in key:

        return freelance(
            parties,
            terms,
            effective_date,
            jurisdiction,
        )

    if "service" in key:

        return service(
            parties,
            terms,
            effective_date,
            jurisdiction,
        )

    return f"""
LEGALEASE GENERAL AGREEMENT

Effective Date: {effective_date}

Jurisdiction:
{jurisdiction}

1. PARTIES

{parties}

2. PURPOSE

The parties intend to establish the terms described in this agreement.

3. TERMS AND CONDITIONS

{terms}

4. GENERAL PROVISIONS

The parties should review all factual information before execution.

5. SIGNATURES

Party 1:

Name: ______________________________

Signature: _________________________

Date: ______________________________


Party 2:

Name: ______________________________

Signature: _________________________

Date: ______________________________


AI-GENERATED DRAFT NOTICE

This document is an AI-assisted draft.
It should be reviewed by a qualified legal professional
before signing or relying upon it.
"""