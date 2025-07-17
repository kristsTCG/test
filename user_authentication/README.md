# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities within the project. It includes files responsible for validating user input and handling user authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. The key components include a JavaScript file for validation logic (`validator.js`) and a Python file for authentication (`auth.py`).

## Key Files
- `validator.js`: This JavaScript file contains validation logic for user input. It ensures that the data provided by users meets the required criteria before proceeding with authentication processes.
- `auth.py`: The Python file `auth.py` is responsible for handling user authentication tasks. It manages user login, registration, and authentication processes within the project.

## Usage
To utilize the code in this folder effectively:
1. Review the `validator.js` file to understand the validation rules applied to user input.
2. Examine the `auth.py` file to understand how user authentication processes are managed within the project.
3. Integrate the validation logic from `validator.js` into your user input forms to ensure data consistency.
4. Utilize the functions and methods defined in `auth.py` to handle user authentication tasks securely and efficiently.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the specified criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates if the input username meets the specified criteria (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user session.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 18:05:10*
