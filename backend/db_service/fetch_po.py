from .db_connection import connect_db

def fetch_po_details(po_number):
    """Fetch PO details from the Azure SQL database."""
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM PurchaseOrders WHERE PO_Number = ?", (po_number,))
        po = cursor.fetchone()
        conn.close()
        return po
    except Exception as e:
        print(f"⚠️ Database Error: {e}")
        return None
