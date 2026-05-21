"""Generated from book-content article."""

import sqlite3


def init_catalog(db_path: str = "catalog.db"):
    conn = sqlite3.connect(db_path)
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS datasets (
        name TEXT NOT NULL,
        version TEXT NOT NULL,
        source_type TEXT,
        license TEXT,
        snapshot_date TEXT,
        row_count INTEGER,
        sha256 TEXT,
        owner TEXT,
        card_json TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (name, version)
    );
    CREATE INDEX IF NOT EXISTS idx_datasets_owner ON datasets(owner);
    CREATE INDEX IF NOT EXISTS idx_datasets_license ON datasets(license);
    """)
    return conn

def register(conn, card: DatasetCard):
    conn.execute("""
    INSERT OR REPLACE INTO datasets
    (name, version, source_type, license, snapshot_date, row_count, sha256, owner, card_json)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (card.name, card.version, card.source_type, card.license,
          card.snapshot_date, card.row_count, card.sha256, card.owner,
          card.to_json()))
    conn.commit()
