# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It includes a JavaScript file for validation and a Python file for authentication.

## Structure
The folder is organized to handle user authentication tasks. It consists of two key files: `validator.js` for input validation and `auth.py` for user authentication.

## Key Files
1. **validator.js**: This JavaScript file contains functions for validating user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before proceeding with authentication processes.
   
2. **auth.py**: The Python file `auth.py` is responsible for handling user authentication logic. It manages user login, registration, and authentication processes within the project.

## Usage
To utilize the functionalities provided in this folder:
- Use the functions defined in `validator.js` to validate user input data before authentication.
- Incorporate the authentication logic from `auth.py` to manage user login and registration processes in the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates if the input username meets specific criteria (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Assesses the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** User authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates user and returns session token.
  - `logout(session_token: str) -> bool`: Ends user session.
  - `is_authenticated(session_token: str) -> bool`: Checks if session is valid.

**Usage:** Instantiate `UserAuth` to manage user authentication operations.

**Dependencies:** `hashlib`, `json`, `datetime`, `timedelta`, `typing`.

---
*Auto-generated documentation - Last updated: 2025-07-17 23:03:00*
