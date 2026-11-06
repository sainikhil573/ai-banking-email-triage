
import tempfile
from pathlib import Path
from unittest.mock import patch

from app import database
from app.schemas import BankingEmailClassification


def test_database_integration():
    with tempfile.TemporaryDirectory() as temp_dir:
        test_db = Path(temp_dir) / "test_banking.db"

        with patch.object(database, "DB_PATH", test_db):
            database.initialize_database()
            database.migrate_database()

            classification = BankingEmailClassification(
                category="fraud_complaint",
                priority="High",
                requires_human_review=True
            )

            metrics = {
                "input_tokens": 150,
                "output_tokens": 40,
                "estimated_cost": 0.00035,
                "latency_seconds": 1.25
            }

            record_id = database.save_classification(
                classification, metrics
            )

            records = database.get_classifications(limit=1)

            assert record_id is not None
            assert len(records) == 1

            record = records[0]

            assert record["id"] == record_id
            assert record["category"] == "fraud_complaint"
            assert record["priority"] == "High"
            assert record["requires_human_review"] == 1
            assert record["input_tokens"] == 150
            assert record["output_tokens"] == 40
            assert abs(record["estimated_cost"] - 0.00035) < 1e-9
            assert abs(record["latency_seconds"] - 1.25) < 1e-9

            print("PASS: Classification saved")
            print("PASS: Token metrics stored")
            print("PASS: Estimated cost stored")
            print("PASS: Latency stored")
            print("PASS: Database retrieval verified")
            print("All database integration tests passed!")


if __name__ == "__main__":
    test_database_integration()
