def create_template(
    parties,
    terms,
    effective_date,
    jurisdiction,
):

    return f"""
EMPLOYMENT AGREEMENT

Effective Date:
{effective_date}

Jurisdiction:
{jurisdiction}


1. PARTIES

{parties}


2. POSITION AND RESPONSIBILITIES

The employee will perform the duties and responsibilities
agreed between the parties.


3. COMPENSATION

The parties should specify salary, payment frequency,
benefits and other applicable compensation.


4. WORKING ARRANGEMENT

The parties should specify the working location,
working hours and applicable policies.


5. CONFIDENTIALITY

Confidential business and professional information
should be protected in accordance with the agreed terms.


6. TERMINATION

The parties should specify applicable notice periods
and termination conditions.


7. ADDITIONAL TERMS

{terms}


8. SIGNATURES

Employer:

Name: ______________________________

Signature: _________________________

Date: ______________________________


Employee:

Name: ______________________________

Signature: _________________________

Date: ______________________________


AI-GENERATED DRAFT NOTICE

This document is an AI-assisted draft and should be
reviewed by a qualified legal professional.
"""
