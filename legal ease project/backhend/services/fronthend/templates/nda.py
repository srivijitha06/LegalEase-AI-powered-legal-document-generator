def create_template(
    parties,
    terms,
    effective_date,
    jurisdiction,
):

    return f"""
NON-DISCLOSURE AGREEMENT

Effective Date:
{effective_date}

Jurisdiction:
{jurisdiction}


1. PARTIES

{parties}


2. PURPOSE

The parties intend to protect confidential information
shared for an agreed business or professional purpose.


3. CONFIDENTIAL INFORMATION

Confidential information may include non-public business,
technical, financial and commercial information.


4. PROTECTION OF INFORMATION

Each party should take reasonable measures to protect
confidential information from unauthorized disclosure.


5. PERMITTED USE

Confidential information should only be used for
the purpose agreed by the parties.


6. DURATION

The parties should specify the applicable confidentiality
period.


7. ADDITIONAL TERMS

{terms}


8. SIGNATURES

Party 1:

Name: ______________________________

Signature: _________________________

Date: ______________________________


Party 2:

Name: ______________________________

Signature: _________________________

Date: ______________________________


AI-GENERATED DRAFT NOTICE

This document is an AI-assisted draft and should be
reviewed by a qualified legal professional.
"""