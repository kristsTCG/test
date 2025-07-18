# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user inputs and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes a JavaScript file for validation (`validator.js`) and a Python file for authentication (`auth.py`).

## Key Files
- `validator.js`: This JavaScript file contains functions for validating user inputs, ensuring data integrity and security.
- `auth.py`: The Python file handles user authentication processes, such as login, registration, and password management.

## Usage
1. To use the validation functions in `validator.js`, import the file into your JavaScript code and call the appropriate functions to validate user inputs.
2. For user authentication tasks, import `auth.py` into your Python code and utilize the functions provided for login, registration, and password management.
3. Ensure to handle errors and exceptions appropriately when using these files to maintain the security and integrity of user authentication processes.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates an email address using a regular expression.
- `validatePassword(password)`: Validates a password based on specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates a username for length (3-20 characters) and character restrictions (alphanumeric and underscores only).
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** This file can be imported using `require` or `import` statements to access the `InputValidator` class and its validation methods.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file provides a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
  - `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Method to register a new user.
  - `login(username: str, password: str) -> Optional[str]`: Method to authenticate a user and return a session token.
  - `logout(session_token: str) -> bool`: Method to end a user session.
  - `is_authenticated(session_token: str) -> bool`: Method to check if a session is valid.

**Usage:** Instantiate `UserAuth` to use the provided authentication functionalities.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization/deserialization.
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 06:36:38*
