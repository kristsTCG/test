# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It is responsible for validating user input and handling authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes a JavaScript file for validation logic and a Python file for authentication functionalities.

## Key Files
- **validator.js**: This JavaScript file contains 1212 characters and is responsible for validating user input data for authentication. It plays a crucial role in ensuring that user-provided information meets the required criteria.
  
- **auth.py**: This Python file contains 2198 characters and is essential for handling user authentication processes. It manages user login, registration, and other authentication-related tasks within the project.

## Usage
To utilize the user authentication functionalities in this folder, follow these steps:
1. Use the `validator.js` file to validate user input data before processing it for authentication.
2. Utilize the `auth.py` file to handle user authentication tasks such as login, registration, and authentication processes.
3. Ensure that both files are integrated correctly within the project to enable seamless user authentication functionalities.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** User authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
  - `logout(session_token: str) -> bool`: Ends a user session.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Import the `UserAuth` class to handle user authentication operations.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For JSON operations.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 18:14:59*
