# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files, `validator.js` and `auth.py`, which are responsible for validating user input and handling authentication in JavaScript and Python, respectively.

## Key Files
- **validator.js**: This JavaScript file contains functions for validating user input, ensuring that data entered by users meets specified criteria before proceeding with authentication processes.
- **auth.py**: The Python file `auth.py` handles user authentication logic, including verifying user credentials and managing user sessions securely.

## Usage
1. To use the validation functions in `validator.js`, import the file into your JavaScript code and call the appropriate validation functions as needed.
2. For user authentication tasks in Python, import the `auth.py` file and utilize the functions provided to authenticate users securely.
3. Ensure to review and customize the validation criteria and authentication logic according to the project requirements before deploying the code.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the format of a password (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates the format of a username (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Determines the strength level of a password based on length and character requirements.

**Usage:** Import `InputValidator` class from this file to use the provided validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication operations.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Method to register a new user.
- `login(username: str, password: str) -> Optional[str]`: Method to authenticate a user and return a session token.
- `logout(session_token: str) -> bool`: Method to end a user session.
- `is_authenticated(session_token: str) -> bool`: Method to check if a session token is valid.

**Usage:** Instantiate `UserAuth` class to utilize user authentication functionalities.

**Dependencies:**
- `hashlib`: For hashing functions.
- `json`: For JSON serialization/deserialization.
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 18:25:20*
