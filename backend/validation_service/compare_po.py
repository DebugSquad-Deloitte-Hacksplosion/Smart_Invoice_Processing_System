from fuzzywuzzy import fuzz
from db_service.fetch_po import fetch_po_details

def validate_invoice(invoice_text):
    """Compare extracted invoice details with PO using fuzzy matching."""
    lines = invoice_text.split("\n")
    po_number = None

    # Extract PO Number from the invoice text
    for line in lines:
        if "PO Number" in line or "PO #" in line:
            po_number = line.split(":")[-1].strip()
            break

    if not po_number:
        return "🚫 PO Number not found in invoice."

    po = fetch_po_details(po_number)
    if not po:
        return "🚫 No matching PO found in database."

    # Compare PO details with invoice text
    validation_score = fuzz.ratio(po[1], invoice_text)
    if validation_score > 80:
        return f"✅ Invoice Validated! Match Score: {validation_score}%"
    else:
        return f"⚠️ Mismatch Detected! Match Score: {validation_score}%"
