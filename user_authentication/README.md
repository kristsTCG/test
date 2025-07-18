# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes a JavaScript file for validation (`validator.js`) and a Python file for authentication (`auth.py`).

## Key Files
- `validator.js`: This JavaScript file contains functions for validating user input. It plays a crucial role in ensuring that user data meets the required criteria before proceeding with authentication processes.
- `auth.py`: The Python file `auth.py` is responsible for handling user authentication tasks. It manages user login, registration, and authentication processes within the project.

## Usage
1. To utilize the validation functions provided in `validator.js`, import the file into your JavaScript code and call the necessary functions to validate user input.
2. For user authentication tasks, import `auth.py` into your Python code and utilize the functions defined within the file to manage user login, registration, and authentication processes.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user's session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and still active.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your Python application.

**Dependencies:**
- `hashlib`: Used for hashing passwords.
- `json`: Not used in this file but imported.
- `datetime`: Used for date and time operations.
- `timedelta`: Used for calculating expiration time for session tokens.
- `typing`: Used for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 03:19:46*
