# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It handles tasks such as validating user input and managing user authentication using JavaScript and Python scripts.

## Structure
The folder is organized to separate the validation logic (validator.js) written in JavaScript and the authentication logic (auth.py) written in Python.

## Key Files
- **validator.js**: This JavaScript file contains the validation logic for user input. It ensures that user-provided data meets the required criteria before proceeding with authentication.
  
- **auth.py**: The Python script `auth.py` is responsible for handling user authentication processes. It manages user login, registration, and authentication using secure methods.

## Usage
1. **validator.js**:
   - To use the validation functions in `validator.js`, import the necessary functions into your JavaScript files.
   - Call the validation functions with user input data to ensure it meets the required criteria before proceeding with authentication.

2. **auth.py**:
   - Import the `auth.py` module into your Python scripts to access the authentication functionalities.
   - Use the provided functions in `auth.py` to handle user registration, login, and authentication processes securely.

Ensure that you follow the guidelines and best practices defined in the respective files for proper user authentication within the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Register a new user with a unique username, email, and password.
- `login(username: str, password: str) -> Optional[str]`: Authenticate a user and return a session token if successful.
- `logout(session_token: str) -> bool`: End a user session based on the session token.
- `is_authenticated(session_token: str) -> bool`: Check if a session token is valid and active.

**Usage:** Instantiate `UserAuth` to manage user authentication processes. Call `register_user` to add new users, `login` to authenticate users and get session tokens, `logout` to end user sessions, and `is_authenticated` to verify session validity.

**Dependencies:** 
- `hashlib` for password hashing.
- `json` for JSON serialization (not used in this file).
- `datetime` for handling date and time operations.
- `timedelta` for time-based calculations.
- `typing.Optional` and `typing.Dict` for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 15:00:26*
