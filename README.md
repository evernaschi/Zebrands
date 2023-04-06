# Zebrands

Zebrands is a project that provides an API to manage a catalog of products. It is built using Python and FastAPI.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker

### Running the Application

1. Clone the repository:

```
git clone https://github.com/evernaschi/Zebrands.git
```

2. Go to the project directory:
```
cd Zebrands
```

3. Modify the `.env` file with the correct environment variables
4. Build the Docker containers:

```
docker-compose build
```
5. Start the application:
```
docker-compose up -d
```

6. Navigate to `http://localhost:8080/docs` in your web browser to view the API documentation.

### Running the Tests

```
docker-compose exec backend pytest
```

## Deployed App
The app has been deployed on Fly.io and can be accessed at https://zebrands.fly.dev/docs

Use the following example credentials to log in as an administrator:


- Username: admin@example.com
- Password: admin123

## Structure

The Zebrands directory contains the main application code:

- api: Contains the API endpoints.
- core: Contains security and basic configurations.
- crud: Contains CRUD methods.
- db: Creates the database engine and initializes the SQLAlchemy's declarative base.
- models: Contains Database models.
- schemas: Contains Pydantic schemas for the database models.
- tests: Contains the test files.
- main.py: The entry point of the application.
- prestart.sh: Script that runs before starting the app.


## Authors

- **Eric Vernaschi** - [evernaschi](https://github.com/evernaschi)
