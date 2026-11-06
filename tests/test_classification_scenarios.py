
from app.classifier import classify_email


test_cases = [
    {
        "email": "I want to apply for a home loan.",
        "expected_category": "loan_application"
    },
    {
        "email": "My credit card payment was declined.",
        "expected_category": "credit_card_issue"
    },
    {
        "email": "Someone made unauthorized transactions on my account.",
        "expected_category": "fraud_complaint"
    },
    {
        "email": "What are your bank's working hours?",
        "expected_category": "general_inquiry"
    }
]


def test_classification_scenarios():
    passed = 0

    for index, test_case in enumerate(test_cases, start=1):
        print(f"\nTesting scenario {index}...")

        result, metrics = classify_email(test_case["email"])

        actual = result.category
        expected = test_case["expected_category"]

        print("Expected:", expected)
        print("Actual:", actual)

        if actual == expected:
            print("PASS")
            passed += 1
        else:
            print("FAIL")

    print(f"\nResults: {passed}/{len(test_cases)} passed")

    assert passed == len(test_cases), (
        "One or more classification scenarios failed"
    )


if __name__ == "__main__":
    test_classification_scenarios()
