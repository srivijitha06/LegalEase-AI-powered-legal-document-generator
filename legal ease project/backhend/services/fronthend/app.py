import html
import requests
import streamlit as st

from frontend.styles import apply_theme
from frontend.components import (
    show_hero,
    show_metrics,
    show_document,
)


st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="wide",
)


apply_theme()

show_hero()
show_metrics()


if "document" not in st.session_state:

    st.session_state.document = ""


if "analysis" not in st.session_state:

    st.session_state.analysis = None


with st.sidebar:

    st.markdown("## ⚖️ LegalEase")

    st.caption(
        "AI-assisted legal workspace"
    )

    backend_url = st.text_input(
        "Backend URL",
        value="http://127.0.0.1:8000",
    ).rstrip("/")

    st.divider()

    page = st.radio(
        "Workspace",
        [
            "📝 Create Document",
            "🔎 Analyze Document",
            "✨ Rewrite Document",
            "ℹ️ About",
        ],
    )

    st.divider()

    st.caption(
        "Generated documents should be reviewed "
        "by a qualified legal professional."
    )


def call_api(
    endpoint,
    payload,
):

    response = requests.post(
        f"{backend_url}{endpoint}",
        json=payload,
        timeout=120,
    )

    response.raise_for_status()

    return response.json()


if page == "📝 Create Document":

    left, right = st.columns(
        [0.9, 1.1],
        gap="large",
    )

    with left:

        st.markdown(
            """
            <div class="card">

                <div class="card-title">
                    Create Your Document
                </div>

                <p>
                Fill in the important details
                and LegalEase will prepare your draft.
                </p>

            </div>
            """,
            unsafe_allow_html=True,
        )

        document_type = st.selectbox(
            "Document Type",
            [
                "Employment Contract",
                "Non-Disclosure Agreement",
                "Lease Agreement",
                "Freelance Work Contract",
                "Service Agreement",
                "General Agreement",
            ],
        )

        parties = st.text_area(
            "Parties",
            placeholder=(
                "Example: ABC Technologies Pvt Ltd "
                "and Jane Doe"
            ),
            height=100,
        )

        effective_date = st.text_input(
            "Effective Date",
            placeholder="25 September 2026",
        )

        jurisdiction = st.text_input(
            "Jurisdiction",
            placeholder="Example: India",
        )

        language = st.selectbox(
            "Language",
            [
                "English",
                "Hindi",
                "Tamil",
                "Telugu",
                "Malayalam",
                "Kannada",
            ],
        )

        terms = st.text_area(
            "Terms and Conditions",
            placeholder=(
                "Payment within 30 days; "
                "confidentiality required; "
                "termination with 15 days notice"
            ),
            height=170,
        )

        generate = st.button(
            "✨ Generate LegalEase Document",
            use_container_width=True,
        )

        if generate:

            if not parties.strip():

                st.error(
                    "Please enter the parties."
                )

            elif not effective_date.strip():

                st.error(
                    "Please enter the effective date."
                )

            elif not terms.strip():

                st.error(
                    "Please enter the terms."
                )

            else:

                payload = {
                    "document_type": document_type,
                    "parties": parties,
                    "terms": terms,
                    "effective_date": effective_date,
                    "jurisdiction": jurisdiction
                    or "Not specified",
                    "language": language,
                }

                try:

                    with st.spinner(
                        "Creating your legal document..."
                    ):

                        result = call_api(
                            "/api/generate",
                            payload,
                        )

                    st.session_state.document = (
                        result["document"]
                    )

                    st.success(
                        "Document created successfully!"
                    )

                    st.caption(
                        f"Mode: {result['mode']}"
                    )

                except Exception as error:

                    st.error(
                        "Unable to connect to LegalEase backend."
                    )

                    st.code(
                        str(error)
                    )

    with right:

        st.markdown(
            """
            <div class="card">

                <div class="card-title">
                    📄 Document Workspace
                </div>

                <p>
                Edit your generated document
                before exporting it.
                </p>

            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.session_state.document:

            edited_document = st.text_area(
                "Edit document",
                value=st.session_state.document,
                height=500,
                label_visibility="collapsed",
            )

            st.session_state.document = (
                edited_document
            )

            st.markdown("### 👁️ Preview")

            show_document(
                st.session_state.document
            )

            st.markdown("### 📥 Export")

            st.download_button(
                "📄 Download TXT",
                data=st.session_state.document,
                file_name="LegalEase_Document.txt",
                mime="text/plain",
                use_container_width=True,
            )

            try:

                from backend.services.pdf_service import (
                    create_pdf,
                )

                pdf = create_pdf(
                    st.session_state.document,
                    document_type,
                )

                st.download_button(
                    "📕 Download PDF",
                    data=pdf,
                    file_name="LegalEase_Document.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                )

            except Exception as error:

                st.warning(
                    f"PDF export unavailable: {error}"
                )

            try:

                from backend.services.docx_service import (
                    create_docx,
                )

                docx = create_docx(
                    st.session_state.document,
                    document_type,
                )

                st.download_button(
                    "📘 Download DOCX",
                    data=docx,
                    file_name="LegalEase_Document.docx",
                    mime=(
                        "application/vnd.openxmlformats-officedocument."
                        "wordprocessingml.document"
                    ),
                    use_container_width=True,
                )

            except Exception as error:

                st.warning(
                    f"DOCX export unavailable: {error}"
                )

        else:

            st.info(
                "Your document will appear here."
            )


elif page == "🔎 Analyze Document":

    st.markdown(
        """
        <div class="card">

            <div class="card-title">
                🔎 LegalEase Document Analyzer
            </div>

            <p>
            Check important clauses and
            possible review items.
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    document = st.text_area(
        "Document",
        value=st.session_state.document,
        height=450,
    )

    if st.button(
        "🔍 Analyze Document",
        use_container_width=True,
    ):

        if len(document.strip()) < 20:

            st.error(
                "Please enter a longer document."
            )

        else:

            try:

                with st.spinner(
                    "Analyzing document..."
                ):

                    result = call_api(
                        "/api/analyze",
                        {
                            "document": document
                        },
                    )

                st.session_state.analysis = (
                    result
                )

            except Exception as error:

                st.error(
                    "Analysis failed."
                )

                st.code(
                    str(error)
                )

    if st.session_state.analysis:

        analysis = (
            st.session_state.analysis
        )

        score = int(
            analysis[
                "completeness_score"
            ]
        )

        st.markdown(
            f"### 📊 Completeness: {score}%"
        )

        st.progress(
            score / 100
        )

        st.markdown(
            "### 💡 Summary"
        )

        st.info(
            analysis["summary"]
        )

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(
                "### 🔑 Key Clauses"
            )

            for item in analysis[
                "key_clauses"
            ]:

                st.markdown(
                    f"- {item}"
                )

        with col2:

            st.markdown(
                "### ⚠️ Review Items"
            )

            for item in analysis[
                "review_items"
            ]:

                st.warning(
                    item
                )

        st.markdown(
            "### 🌿 Strengths"
        )

        for item in analysis[
            "strengths"
        ]:

            st.success(
                item
            )


elif page == "✨ Rewrite Document":

    st.markdown(
        """
        <div class="card">

            <div class="card-title">
                ✨ AI Rewrite Assistant
            </div>

            <p>
            Ask LegalEase to change the
            presentation of your document.
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    document = st.text_area(
        "Document",
        value=st.session_state.document,
        height=450,
    )

    instruction = st.text_input(
        "Rewrite instruction",
        placeholder=(
            "Make the language clearer and more concise."
        ),
    )

    if st.button(
        "✨ Rewrite",
        use_container_width=True,
    ):

        if not document.strip():

            st.error(
                "Please enter a document."
            )

        elif not instruction.strip():

            st.error(
                "Please enter an instruction."
            )

        else:

            try:

                with st.spinner(
                    "Rewriting document..."
                ):

                    result = call_api(
                        "/api/rewrite",
                        {
                            "document": document,
                            "instruction": instruction,
                        },
                    )

                st.session_state.document = (
                    result["document"]
                )

                st.success(
                    "Rewrite completed."
                )

                show_document(
                    st.session_state.document
                )

            except Exception as error:

                st.error(
                    "Rewrite failed."
                )

                st.code(
                    str(error)
                )


else:

    st.markdown(
        """
        <div class="card">

            <div class="card-title">
                ⚖️ About LegalEase
            </div>

            <p>
            LegalEase is an AI-assisted legal
            document workspace designed to make
            document drafting easier and more
            understandable.
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    features = [
        "🤖 AI-assisted document drafting",
        "🔎 Document analysis",
        "📊 Completeness indicator",
        "✨ AI rewrite assistant",
        "📄 Editable documents",
        "📕 PDF export",
        "📘 DOCX export",
        "🎨 Pastel legal interface",
        "🛡️ Local fallback mode",
    ]

    for feature in features:

        st.markdown(
            f"""
            <div class="card">
                {html.escape(feature)}
            </div>
            """,
            unsafe_allow_html=True,
        )


st.markdown(
    """
    <div class="footer">

        ⚖️ LegalEase

        <br>

        AI-assisted legal document platform

        <br><br>

        Generated documents should be reviewed
        by a qualified legal professional.

    </div>
    """,
    unsafe_allow_html=True,
)