def create_template(
    parties,
    terms,
    effective_date,
    jurisdiction,
):

    return f"""
LEASE AGREEMENT

Effective Date:
{effective_date}

Jurisdiction:
{jurisdiction}


1. PARTIES

{parties}


2. PROPERTY

The complete property address and description
should be specified before execution.


3. RENT

The parties should specify rent, payment frequency,
deposit and other applicable charges.


4. LEASE PERIOD

The commencement date, end date and renewal
conditions should be clearly stated.


5. MAINTENANCE

The parties should identify responsibilities for
maintenance, repairs and utilities.


6. TERMINATION

Applicable notice and termination conditions
should be specified.


7. ADDITIONAL TERMS

{terms}


8. SIGNATURES

Landlord:

Name: ______________________________

Signature: _________________________

Date: ______________________________


Tenant:

Name: ______________________________

Signature: _________________________

Date: ______________________________


AI-GENERATED DRAFT NOTICE

This document is an AI-assisted draft and should be
reviewed by a qualified legal professional.
"""