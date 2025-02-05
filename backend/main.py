from email_service.fetch_email import fetch_invoice_email
from ocr_service.extract_text import extract_invoice_text
from validation_service.compare_po import validate_invoice
import os

def main():
    print("\n🚀 Starting Invoice Processing...")
    
    pdf_path = fetch_invoice_email()
    if not pdf_path:
        print("🚫 No new invoice found.")
        return

    if not os.path.exists(pdf_path):
        print("🚫 PDF file not found.")
        return

    invoice_text = extract_invoice_text(pdf_path)
    if not invoice_text:
        print("🚫 Text extraction failed.")
        return

    result = validate_invoice(invoice_text)
    print(result)

if __name__ == "__main__":
    main()