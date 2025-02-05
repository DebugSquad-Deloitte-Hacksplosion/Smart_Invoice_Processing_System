from fuzzywuzzy import fuzz
from db_service.db_connection import connect_db

def validate_invoice(invoice_text):
    if not invoice_text:
        return "🚫 No text could be extracted from invoice."

    lines = invoice_text.split("\n")
    po_number = None

    for line in lines:
        if any(term in line.upper() for term in ["PO NUMBER", "PO #", "PURCHASE ORDER"]):
            po_number = ''.join(filter(str.isalnum, line.split(":")[-1]))
            break

    if not po_number:
        return "🚫 PO Number not found in invoice."

    po = fetch_po_details(po_number)
    if not po:
        return "🚫 No matching PO found in database."

    validation_score = fuzz.ratio(str(po[1]), invoice_text)
    threshold = 80

    if validation_score > threshold:
        return f"✅ Invoice Validated! Match Score: {validation_score}%"
    else:
        return f"⚠️ Mismatch Detected! Match Score: {validation_score}%"
