# Pydantic models file

# This file defines valid input and output structures.

# Step 1 — Define the classification structure
# What does this code do? - It defines the "data contract" for our AI classifier.

# What is data contract?
# A data contract "defines the structure and rules" that data must follow when passing between different parts of an application.


from typing import Literal
from pydantic import BaseModel, ConfigDict


class BankingEmailClassification(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
        strict=True
    )

    category: Literal[
        "loan_application",
        "credit_card_issue",
        "fraud_complaint",
        "general_inquiry"
    ]

    priority: Literal[
        "High",
        "Medium",
        "Low"
    ]

    requires_human_review: bool
# The model rejects unexpected fields and invalid values.
