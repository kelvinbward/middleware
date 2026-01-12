# Testing Guide

This project uses `pytest` for automated testing.

## Prerequisites

Ensure you have the virtual environment set up and dependencies installed:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running Tests

Run the test suite from the project root:

```bash
python -m pytest tests/
```

## mocking Strategy

- **DB Dependency**: The `get_latest_resume_from_db` function is mocked to avoid external database connections during testing.
- **Environment**: Critical environment variables like `ADMIN_API_KEY` are mocked using `unittest.mock.patch` within the test functions.
- **File I/O**: File writing operations (for export tests) are mocked using `mock_open`.
