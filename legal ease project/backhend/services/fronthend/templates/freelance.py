def create_template(
    parties,
    terms,
    effective_date,
    jurisdiction,
):

    return f"""
FREELANCE SERVICES AGREEMENT

Effective Date:
{effective_date}

Jurisdiction:
{jurisdiction}


1. PARTIES

{parties}


2. SERVICES

The freelancer will provide the services and
deliverables agreed between the parties.


3. PAYMENT

The parties should specify fees, invoices,
payment dates and applicable expenses.


4. INTELLECTUAL PROPERTY

Ownership and permitted use of work product
should be clearly established.


5. CONFIDENTIALITY

The parties should protect confidential information
exchanged during the engagement.


6. TERMINATION

The parties should specify termination requirements
and applicable notice periods.


7. ADDITIONAL TERMS

{terms}


8. SIGNATURES

Client:

Name: ______________________________

Signature: _________________________

Date: ______________________________


Freelancer:

Name: ______________________________

Signature: _________________________

Date: ______________________________


AI-GENERATED DRAFT NOTICE

This document is an AI-assisted draft and should be
reviewed by a qualified legal professional.
"""