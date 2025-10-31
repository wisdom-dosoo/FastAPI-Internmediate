# FastAPI Advance

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

A comprehensive backend development project built with Python and FastAPI. This repository serves as a tutorial and example for advanced concepts in building RESTful APIs using FastAPI, including routing, response handling, Pydantic models, routers, status codes, tags, and integration with modern Python libraries.

## Features

- **Modular Routing**: Organized endpoints using FastAPI routers for better code structure.
- **Pydantic Models**: Data validation and serialization with Pydantic BaseModel.
- **HTTP Methods**: Support for GET, POST, and DELETE operations.
- **Status Codes**: Custom status code handling for different response scenarios.
- **Tags**: Endpoint categorization using tags for better API documentation.
- **Auto-generated API Documentation**: Interactive API docs at `/docs` (Swagger UI) and `/redoc`.
- **Fast and Asynchronous**: Built on FastAPI for high-performance API development.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/BROOKS69/FastAPI-advance.git
   cd FastAPI-advance
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the FastAPI server**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the application**:
   - **Base URL**: `http://127.0.0.1:8000`
   - **API Docs**: `http://127.0.0.1:8000/docs` (Swagger UI)
   - **ReDoc**: `http://127.0.0.1:8000/redoc`

## API Endpoints

### Main Application Routes

- **GET** `/home` - Returns a welcome message for the home page.
- **GET** `/blog/all` - Retrieves all blogs from user request.
- **DELETE** `/about` - Provides information about the application (About Page).
- **GET** `/blog/{id}` - Retrieves a specific blog by ID.
- **POST** `/create/blog` - Creates a new blog.

### GET Operations Router (`/get_op`)

- **GET** `/get_op/{item_id}` - Retrieves an item by ID.
- **GET** `/get_op/all` - Retrieves all items.
- **GET** `/get_op/search/` - Searches for items based on query parameters.
- **GET** `/get_op/` - Root endpoint for GET operations.

### POST Operations Router (`/post_op`)

- **POST** `/post_op/` - Creates a new post.
- **POST** `/post_op/{post_id}` - Retrieves a post by ID (Note: Typically, POST is for creation; this might be an example endpoint).

### Additional Example Files

The repository includes standalone example files demonstrating advanced FastAPI features:
- `predefined_path.py`: Using enums for predefined path parameters.
- `status_code.py`: Custom status code handling.
- `tags.py`: Endpoint tagging for organization.

These files are not integrated into the main application but serve as educational examples.

## Dependencies

- **FastAPI**: Modern, fast web framework for building APIs with Python 3.7+.
- **Uvicorn**: ASGI web server implementation for Python.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for Python.

## Project Structure

```
FastAPI-advance/
├── main.py                 # Main FastAPI application
├── routers/
│   ├── get_op.py           # GET operations router
│   └── post_op.py          # POST operations router
├── predefined_path.py      # Example: Predefined path parameters
├── status_code.py          # Example: Status code handling
├── tags.py                 # Example: Endpoint tagging
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── LICENSE                 # MIT License
└── .gitignore              # Git ignore file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
