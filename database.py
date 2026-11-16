import sqlite3
from datetime import datetime


class Database:

    def __init__(self, path):

        self.conn = sqlite3.connect(path)

        self.create_tables()

    def create_tables(self):

        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS listings (
            listing_id TEXT PRIMARY KEY,
            source TEXT,
            price REAL,
            first_seen TEXT,
            last_seen TEXT
        )
        """)

        self.conn.commit()

    def get_previous_price(self, listing_id):

        row = self.conn.execute(
            """
            SELECT price
            FROM listings
            WHERE listing_id = ?
            """,
            (listing_id,)
        ).fetchone()

        if row:
            return row[0]

        return None

    def save_listing(self, listing):

        now = datetime.utcnow().isoformat()

        self.conn.execute(
            """
            INSERT OR REPLACE INTO listings
            (
                listing_id,
                source,
                price,
                first_seen,
                last_seen
            )
            VALUES
            (
                ?,
                ?,
                ?,
                COALESCE(
                    (
                        SELECT first_seen
                        FROM listings
                        WHERE listing_id=?
                    ),
                    ?
                ),
                ?
            )
            """,
            (
                listing.listing_id,
                listing.source,
                listing.price,
                listing.listing_id,
                now,
                now
            )
        )

        self.conn.commit()