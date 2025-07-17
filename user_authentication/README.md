# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities within the project. It includes validation logic in JavaScript and authentication logic in Python.

## Structure
The folder is organized to handle user authentication tasks. It contains two key files: `validator.js` for input validation and `auth.py` for user authentication.

## Key Files
1. `validator.js`: This JavaScript file contains logic for validating user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before proceeding with authentication.
   
2. `auth.py`: The Python file `auth.py` is responsible for handling user authentication processes. It manages user login, registration, and authentication tasks within the project.

## Usage
To utilize the code in this folder effectively:
- Review the `validator.js` file to understand the input validation logic and make any necessary adjustments to fit your project's requirements.
- Explore the `auth.py` file to understand how user authentication is implemented and customize it as needed for your project's authentication flow.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on its length and character composition.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** User authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates user and returns a session token.
  - `logout(session_token: str) -> bool`: Ends a user session.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session is valid.

**Usage:** Instantiate `UserAuth` to utilize user authentication functionalities.

**Dependencies:** `hashlib`, `json`, `datetime`, `timedelta`, `typing`.

---
*Auto-generated documentation - Last updated: 2025-07-17 19:23:36*
