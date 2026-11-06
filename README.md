# AI-Powered Banking Email Classification & Triage System

A Python-based Generative AI application that uses Anthropic Claude to classify incoming banking emails, assign priority levels, and identify cases requiring human review.

The application validates structured AI outputs using Pydantic, stores classification results in SQLite, and tracks API usage, estimated costs, and latency.

## Key Features

- AI-powered banking email classification
- Four categories: loan applications, credit card issues, fraud complaints, and general inquiries
- Priority assignment: High, Medium, Low
- Human-review recommendation
- Structured output validation using Pydantic
- SQLite database persistence
- API token usage, estimated cost, and latency tracking
- API exception handling
- Input validation
- Functional, mocked failure, and database integration tests

## Technology Stack

- Python 3.11
- Anthropic Claude API
- Pydantic
- SQLite
- python-dotenv
- unittest.mock

## System Architecture

```text
Banking Email Input
        |
        v
Input Validation
        |
        v
Claude API Classification
        |
        v
Pydantic Schema Validation
        |
        v
Classification + API Metrics
        |
        v
SQLite Database
        |
        v
Stored Results
```

## Project Structure

```text
banking-email-triage/
|
|-- app/
|   |-- __init__.py
|   |-- main.py
|   |-- classifier.py
|   |-- schemas.py
|   |-- database.py
|   |-- config.py
|
|-- tests/
|   |-- __init__.py
|   |-- test_api_timeout.py
|   |-- test_input_validation.py
|   |-- test_classification_scenarios.py
|   |-- test_database_integration.py
|
|-- data/
|-- requirements.txt
|-- .gitignore
|-- README.md
```

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd banking-email-triage
```

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the `banking-email-triage` and add:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

The current application loads this environment file from the parent directory.

Never commit API keys or `.env` files to GitHub.

### 5. Run the application

```bash
python -m app.main
```

The application initializes the database, classifies a sample banking email, stores the result, and displays recent classification records.

## Testing

Run individual tests from the project root:

```bash
python -m tests.test_api_timeout
python -m tests.test_input_validation
python -m tests.test_classification_scenarios
python -m tests.test_database_integration
```

The classification scenario test makes real Claude API calls and may incur API usage charges.

Other tests validate input handling, simulated API failures, and SQLite persistence without requiring live Claude API requests.

## Reliability and Monitoring

The application includes:

- Handling for rate limits, timeouts, connection failures, and API status errors
- Input type, empty-string, and length validation
- Structured output validation
- Explicit database connection cleanup
- Input/output token tracking
- Estimated API cost calculation
- Request latency measurement

API cost calculations use configurable example pricing values and should be verified against current provider pricing before financial reporting.

## Current Limitations

- Demonstration application with a hardcoded sample email
- SQLite storage rather than a managed production database
- Limited classification evaluation dataset
- No authentication or authorization layer
- No sensitive-data redaction or production security controls
- No deployment pipeline or centralized monitoring
- Human-review recommendations are not a substitute for a real banking review process

## Future Enhancements

- REST API using FastAPI
- Larger labeled evaluation dataset
- Automated test suite and CI/CD
- Configuration management and secret storage
- Production logging and observability
- Human-in-the-loop review workflow
- Deployment to a cloud platform

## Engineering Concepts Demonstrated

- Modular Python architecture
- LLM API integration
- Structured outputs and data contracts
- Exception handling and mocking
- Database persistence and schema migration
- Input validation
- API cost and latency monitoring
- Integration and functional testing

## Disclaimer

This is an educational portfolio project. It is not intended for processing real customer banking data or making autonomous financial decisions.