# scripts/fetch_data.py

from Bio import Entrez, SeqIO
import sqlite3
import os
from config import NCBI_EMAIL, NCBI_DATABASE, NCBI_QUERY, MAX_RECORDS

# Setup Entrez
Entrez.email = NCBI_EMAIL

# Database setup
DB_PATH = '../db/sequences.db'
TABLE_NAME = 'genomes'

def create_db():
    if not os.path.exists('../db'):
        os.makedirs('../db')
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id TEXT PRIMARY KEY,
            sequence TEXT,
            organism TEXT,
            collection_date TEXT,
            location TEXT
        )
    ''')
    conn.commit()
    conn.close()

def fetch_sequences():
    # Query NCBI
    handle = Entrez.esearch(db=NCBI_DATABASE, term=NCBI_QUERY, retmax=MAX_RECORDS)
    record = Entrez.read(handle)
    handle.close()
    ids = record["IdList"]

    # Fetch each sequence
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for seq_id in ids:
        print(f"Fetching sequence: {seq_id}")
        handle = Entrez.efetch(db=NCBI_DATABASE, id=seq_id, rettype="gb", retmode="text")
        record = SeqIO.read(handle, "genbank")
        handle.close()

        # Extract relevant metadata
        seq = str(record.seq)
        organism = record.annotations.get("organism", "Unknown")
        collection_date = "Unknown"
        location = "Unknown"

        for feature in record.features:
            if feature.type == "source":
                collection_date = feature.qualifiers.get("collection_date", ["Unknown"])[0]
                location = feature.qualifiers.get("country", ["Unknown"])[0]

        # Insert into database
        cursor.execute(f'''
            INSERT OR IGNORE INTO {TABLE_NAME} (id, sequence, organism, collection_date, location) 
            VALUES (?, ?, ?, ?, ?)
        ''', (seq_id, seq, organism, collection_date, location))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
    fetch_sequences()
