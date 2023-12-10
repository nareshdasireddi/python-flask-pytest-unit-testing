# Flask REST APIs with Pytest Unit Testing

This repository provides a simple example of building RESTful APIs using Flask and conducting unit testing with Pytest. This project follows best practices for structuring a Flask application and includes sample tests using Pytest.

## Getting Started

### Prerequisites

Make sure you have Python and pip installed on your machine. Additionally, you may want to set up a virtual environment to isolate dependencies.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS and Linux
source venv/bin/activate
```

## Run Server
```
python app.py
```

## Run Test cases
```bash
# Run all files and folder which are having name test
pytest 

# Run specific file
pytest -s test/test_app.py
```

## 