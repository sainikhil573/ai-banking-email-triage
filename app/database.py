# SQLite operations file

# This file handles saving and retrieving records.

import sqlite3
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parents[1]

# Database file location
DB_PATH = BASE_DIR / "data" / "banking.db"


def initialize_database():

    DB_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    connection = sqlite3.connect(DB_PATH)

    try:

        cursor = connection.execute("""
            CREATE TABLE IF NOT EXISTS email_classifications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL,
                priority TEXT NOT NULL,
                requires_human_review INTEGER NOT NULL,
                created_at TEXT NOT NULL
                    DEFAULT CURRENT_TIMESTAMP
            )
        """)
        connection.commit()
        print("Database initialized successfully!")
    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def save_classification(classification, metrics):
    connection = sqlite3.connect(DB_PATH)

    try:
        cursor = connection.execute(
            """
            INSERT INTO email_classifications
            (
                category,
                priority,
                requires_human_review,
                input_tokens,
                output_tokens,
                estimated_cost,
                latency_seconds
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                classification.category,
                classification.priority,
                int(classification.requires_human_review),
                metrics["input_tokens"],
                metrics["output_tokens"],
                metrics["estimated_cost"],
                metrics["latency_seconds"]
            )
        )

        record_id = cursor.lastrowid
        connection.commit()

        return record_id

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def migrate_database():
    new_columns = {
        "input_tokens": "INTEGER",
        "output_tokens": "INTEGER",
        "estimated_cost": "REAL",
        "latency_seconds": "REAL"
    }

    connection = sqlite3.connect(DB_PATH)

    try:

        cursor = connection.execute(
            """
                PRAGMA table_info(email_classifications)
            """
        )

        existing_columns = {
            row[1] for row in cursor.fetchall()
        }

        if not existing_columns:
            raise RuntimeError(
                "Table not found. Initialize the database first."
            )

        for column, data_type in new_columns.items():
            if column not in existing_columns:
                connection.execute(
                    f"ALTER TABLE email_classifications "
                    f"ADD COLUMN {column} {data_type}"
                )
        connection.commit()
        print("Database migration completed!")

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def get_classifications(limit=10):
    connection = sqlite3.connect(DB_PATH)

    try:
        connection.row_factory = sqlite3.Row

        cursor = connection.execute(
            """
                SELECT
                    id,
                    category,
                    priority,
                    requires_human_review,
                    input_tokens,
                    output_tokens,
                    estimated_cost,
                    latency_seconds,
                    created_at
                FROM email_classifications
                ORDER BY id DESC
                LIMIT ?
            """,
            (limit,)
        )

        records = cursor.fetchall()

        return [dict(record) for record in records]

    finally:
        connection.close()


if __name__ == "__main__":
    initialize_database()
