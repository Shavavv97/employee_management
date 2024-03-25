# Employee Management System

## Overview
This is a simple Employee Management System built using Flask, a Python web framework. The system allows users to create, retrieve, and manage employee data using a CSV file.

## Getting Started

1.- Clone the repository

```bash
git clone https://github.com/Shavavv97/employee_management.git
```

2.- Create a virtual environment

```bash
python -m venv env
```

3.- Activate the virtual environment

```bash
source env/bin/activate
```

4.- Install the required packages

```bash
pip install -r requirements.txt
```

5.- Run the application

```bash
python app.py
```

## API Endpoints

### Get Employees

*GET /api/*

Retrieves a list of all employees in the system.

**Response 200 OK** - A JSON response with a list of employees

### Get Employee
*GET /api/<field>/<value>*

Retrieves an employee by providing a field name and a value.

**Response 200 OK** - A JSON response with the employee

**Response 404 Not Found** - If the employee is not found

### Create Employee

*POST /api/*

Creates a new employee in the system.

**Request**
The request body should be in JSON format, with the following structure:

```bash
{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "phone1": "555-555-5555",
    "address": "123 Main St",
    "city": "Springfield",
    "state": "IL",
    "zip": "12345",
    "company_name": "ABC Corporation",
    "department": "Marketing"
}
```

**Response 201 Created** - A JSON response with a success message

## Testing
The project includes a test suite using Python's built-in unittest module.

Activate the virtual environment
```
source env/bin/activate
```

Run the tests

```
python -m unittest
```

## License

[MIT](https://choosealicense.com/licenses/mit/)