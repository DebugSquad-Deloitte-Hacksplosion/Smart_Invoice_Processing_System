import os
import streamlit as st
import time
from email_service.fetch_email import fetch_invoice_email
from ocr_service.extract_text import extract_invoice_text
from validation_service.compare_po import validate_invoice

def main():
    # Page configuration
    st.set_page_config(
        page_title="Invoice Processing System",
        page_icon="📑",
        layout="centered"
    )

    # Custom CSS
    st.markdown("""
        <style>
        .stButton>button {
            width: 100%;
            height: 3em;
            font-size: 1.1em;
            margin-top: 1em;
        }
        .success-message {
            padding: 1em;
            border-radius: 0.5em;
            background-color: #d4edda;
            border: 1px solid #c3e6cb;
            color: #155724;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown("<h1 style='text-align: center; margin-bottom: 2em;'>📑 Invoice Processing System</h1>", unsafe_allow_html=True)

    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### Step 1: Fetch")
    with col2:
        st.markdown("### Step 2: Extract")
    with col3:
        st.markdown("### Step 3: Validate")

    
    if 'pdf_path' not in st.session_state:
        st.session_state.pdf_path = None
    if 'invoice_text' not in st.session_state:
        st.session_state.invoice_text = None
    if 'processing' not in st.session_state:
        st.session_state.processing = False

    # Main process container
    with st.container():
        # Fetch Invoice Section
        if not st.session_state.pdf_path:
            if st.button("🔄 Fetch Invoice from Email", key="fetch_button"):
                with st.spinner("Fetching invoice from email..."):
                    st.session_state.processing = True
                    pdf_path = fetch_invoice_email()
                    if pdf_path:
                        st.session_state.pdf_path = pdf_path
                        st.success(f"✅ Invoice successfully saved!")
                        st.markdown(f"📁 Location: `{pdf_path}`")
                    else:
                        st.error("❌ No new invoice found in email.")
                    st.session_state.processing = False

        # Extract Text Section
        if st.session_state.pdf_path and not st.session_state.invoice_text:
            if st.button("📝 Extract Text from Invoice", key="extract_button"):
                with st.spinner("Extracting text from invoice..."):
                    st.session_state.processing = True
                    invoice_text = extract_invoice_text(st.session_state.pdf_path)
                    st.session_state.invoice_text = invoice_text
                    st.session_state.processing = False

        # Display extracted text if available
        if st.session_state.invoice_text:
            st.markdown("### 📄 Extracted Text")
            st.text_area(
                "Invoice Content",
                value=st.session_state.invoice_text,
                height=200,
                key="text_area"
            )

            # Validation Section
            if st.button("✅ Validate Invoice", key="validate_button", type="primary"):
                with st.spinner("Validating invoice..."):
                    validation_result = validate_invoice(st.session_state.invoice_text)
                    
                    # Display validation results in an expander
                    with st.expander("View Validation Results", expanded=True):
                        st.json(validation_result)

        # Reset button at the bottom
        if st.session_state.pdf_path or st.session_state.invoice_text:
            if st.button("🔄 Process New Invoice", key="reset_button"):
                st.session_state.pdf_path = None
                st.session_state.invoice_text = None
                st.rerun()

    # Footer
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; color: #666;'>Invoice Processing System v1.0</p>", 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()