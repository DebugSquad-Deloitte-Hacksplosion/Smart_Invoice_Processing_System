import imaplib
import email
from email.header import decode_header
import os

# Email Configuration
EMAIL_USER = "manojkprdev@gmail.com"
EMAIL_PASS = "oigvttknbrhxjfkc" 
IMAP_SERVER = "imap.gmail.com"  # For Outlook, use 'outlook.office365.com'
INVOICE_FOLDER = "./invoices" 
os.makedirs(INVOICE_FOLDER, exist_ok=True)

def fetch_invoice_email():
    """Fetch the latest invoice email and save the PDF attachment."""
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_USER, EMAIL_PASS)
        mail.select("inbox")

        _, search_data = mail.search(None, "ALL")
        email_ids = search_data[0].split()

        for email_id in email_ids[::-1]:  # Start from the latest email
            _, msg_data = mail.fetch(email_id, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    for part in msg.walk():
                        if part.get_content_type() == "application/pdf":
                            filename = part.get_filename()
                            if filename:
                                filepath = os.path.join(INVOICE_FOLDER, filename)
                                with open(filepath, "wb") as f:
                                    f.write(part.get_payload(decode=True))
                                return filepath
        return None
    except Exception as e:
        print(f"⚠️ Email Fetching Error: {e}")
        return None
