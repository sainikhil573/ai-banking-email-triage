
from app.classifier import classify_email


def test_invalid_email(email):
    try:
        classify_email(email)
    except (ValueError, TypeError) as error:
        print(f"PASS: {error}")
    else:
        raise AssertionError("Invalid input was accepted")


if __name__ == "__main__":
    test_invalid_email("")
    test_invalid_email("   ")
    test_invalid_email(123)
    test_invalid_email("A" * 10_001)

    print("All input validation tests passed!")
