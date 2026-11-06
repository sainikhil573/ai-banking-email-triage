# Application entry point file

# This file connects everything.

from app.classifier import classify_email
from app.database import (
    initialize_database,
    migrate_database,
    save_classification,
    get_classifications
)
from anthropic import APIError


def main():
    initialize_database()
    migrate_database()

    email = """
        Hello,

        I noticed three unauthorized transactions
        on my credit card totaling $1,200.

        I did not make these purchases.
        Please investigate immediately.
    """

    print("Processing customer email...")

    try:
        result, metrics = classify_email(email)

    except APIError as error:
        print(f"Classification failed: {type(error).__name__}")
        return

    print("\nClassification Result")
    print("---------------------")
    print("Category:", result.category)
    print("Priority:", result.priority)
    print("Human Review:", result.requires_human_review)

    record_id = save_classification(result, metrics)

    print("\nClassification saved successfully!")
    print("Database Record ID:", record_id)

    print("\nRecent Classification History")
    print("-----------------------------")

    records = get_classifications(limit=5)

    for record in records:
        print(
            f"\nRecord ID: {record['id']}"
            f"\nCategory: {record['category']}"
            f"\nPriority: {record['priority']}"
            f"\nHuman Review: {bool(record['requires_human_review'])}"
            f"\nInput Tokens: {record['input_tokens']}"
            f"\nOutput Tokens: {record['output_tokens']}"
            f"\nEstimated Cost: ${record['estimated_cost']:.6f}"
            f"\nAPI Latency: {record['latency_seconds']:.2f} seconds"
            if record["estimated_cost"] is not None
            and record["latency_seconds"] is not None
            else (
                f"\nRecord ID: {record['id']}"
                f"\nCategory: {record['category']}"
                f"\nPriority: {record['priority']}"
                f"\nMetrics: Not recorded (older record)"
            )
        )


if __name__ == "__main__":
    main()
