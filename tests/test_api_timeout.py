
from unittest.mock import patch

from anthropic import APITimeoutError

from app.classifier import classify_email, client


def test_timeout():
    with patch.object(
        client.messages,
        "parse",
        side_effect=APITimeoutError(request=None)
    ):
        try:
            classify_email("Test banking email")

        except APITimeoutError:
            print("PASS: Timeout propagated correctly.")

        else:
            raise AssertionError(
                "FAIL: Expected a timeout exception."
            )


if __name__ == "__main__":
    test_timeout()
