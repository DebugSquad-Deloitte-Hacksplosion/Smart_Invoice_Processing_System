from email_service.fetch_email import fetch_invoice_email
from ocr_service.extract_text import extract_invoice_text
from validation_service.compare_po import validate_invoice



def main():
    print("\n🚀 Starting Invoice Processing...")
    pdf_path = fetch_invoice_email()
    if not pdf_path:
        print("🚫 No new invoice found.")
        return

    invoice_text = extract_invoice_text(pdf_path)
    validation_result = validate_invoice(invoice_text)
    print(validation_result)

if __name__ == "__main__":
    main()
