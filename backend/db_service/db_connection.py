import os
import pyodbc

# Get credentials from environment variables (Set them before running)
DB_SERVER = os.getenv("AZURE_DB_SERVER")
DB_DATABASE = os.getenv("AZURE_DB_DATABASE")
DB_USERNAME = os.getenv("AZURE_DB_USERNAME")
DB_PASSWORD = os.getenv("AZURE_DB_PASSWORD")

def connect_db():
    """Establish a connection with Azure SQL Server."""
    try:
        conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={DB_SERVER};DATABASE={DB_DATABASE};'
            f'UID={DB_USERNAME};PWD={DB_PASSWORD};'
            f'ENCRYPT=yes;TRUSTSERVERCERTIFICATE=no;CONNECTION TIMEOUT=30;'
        )
        return conn
    except pyodbc.Error as e:
        print(f"⚠️ Error connecting to the database: {e}")
        return None
