from io import BytesIO
from html import escape

from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import (
    ParagraphStyle,
    getSampleStyleSheet,
)
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)


def create_pdf(
    text,
    document_type,
):

    output = BytesIO()

    document = SimpleDocTemplate(
        output,
        pagesize=A4,
        leftMargin=20 * mm,
        rightMargin=20 * mm,
        topMargin=25 * mm,
        bottomMargin=20 * mm,
        title=f"LegalEase - {document_type}",
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "LegalEaseTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        alignment=TA_CENTER,
        spaceAfter=12,
    )

    heading_style = ParagraphStyle(
        "LegalEaseHeading",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=16,
        spaceBefore=8,
        spaceAfter=5,
    )

    body_style = ParagraphStyle(
        "LegalEaseBody",
        parent=styles["BodyText"],
        fontName="Times-Roman",
        fontSize=10.5,
        leading=15,
        spaceAfter=7,
    )

    story = []

    story.append(
        Paragraph(
            "LEGALEASE",
            title_style,
        )
    )

    story.append(
        Paragraph(
            escape(document_type.upper()),
            heading_style,
        )
    )

    for line in text.splitlines():

        line = line.strip()

        if not line:

            story.append(
                Spacer(1, 5)
            )

            continue

        safe_line = escape(line)

        is_heading = (
            line.isupper()
            or (
                len(line) > 2
                and line[0].isdigit()
                and "." in line[:4]
            )
        )

        story.append(
            Paragraph(
                safe_line,
                heading_style
                if is_heading
                else body_style,
            )
        )

    def footer(canvas, doc):

        canvas.saveState()

        canvas.setFont(
            "Helvetica",
            7,
        )

        canvas.drawCentredString(
            A4[0] / 2,
            10 * mm,
            "LegalEase | AI-assisted legal document draft",
        )

        canvas.restoreState()

    document.build(
        story,
        onFirstPage=footer,
        onLaterPages=footer,
    )

    return output.getvalue()