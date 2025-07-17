# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities within the project. It includes validation logic in JavaScript and authentication logic in Python.

## Structure
The folder is organized to handle user authentication tasks. The key components include a JavaScript file for data validation and a Python file for user authentication.

## Key Files
- **validator.js**: This JavaScript file contains 1212 characters of code responsible for validating user input data.
- **auth.py**: This Python file contains 2198 characters of code for handling user authentication processes.

## Usage
1. To utilize the validation logic, refer to `validator.js` and integrate the validation functions into your user input forms.
2. For user authentication tasks, refer to `auth.py` and incorporate the authentication methods into your user management system.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numeric characters.
- `validateUsername(username)`: Validates the format of a username, allowing only alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the provided validation functions in your authentication logic.

**Dependencies:** No external dependencies are required for this file.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token if successful.
  - `logout(session_token: str) -> bool`: Ends a user session based on the provided session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and the user is authenticated.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:** 
- `hashlib`: For hashing functions.
- `json`: For JSON serialization and deserialization.
- `datetime`: For date and time operations.
- `timedelta`: For time duration calculations.
- `typing.Optional`, `typing.Dict`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 14:20:53*
