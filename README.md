# FastAPI Advance

A comprehensive backend development course project built with Python and FastAPI. This repository demonstrates advanced concepts in building RESTful APIs using FastAPI, including routing, response handling, and integration with modern Python libraries.

## Features

- **Home Endpoint**: `/home` - Returns a welcome message for the home page.
- **About Endpoint**: `/about` - Provides information about the application.
- **Auto-generated API Documentation**: FastAPI automatically generates interactive API docs at `/docs` and `/redoc`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/BROOKS69/FastAPI-advance.git
   cd FastAPI-advance
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

2. Access the application:
   - Home: `http://127.0.0.1:8000/home`
   - About: `http://127.0.0.1:8000/about`
   - API Docs: `http://127.0.0.1:8000/docs` (Swagger UI)
   - ReDoc: `http://127.0.0.1:8000/redoc`

## Dependencies

- **FastAPI**: Modern, fast web framework for building APIs with Python 3.7+.
- **Uvicorn**: ASGI web server implementation for Python.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for Python.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
