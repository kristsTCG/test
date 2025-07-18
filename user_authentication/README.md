# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. These files handle user validation and authentication processes.

## Structure
The folder is organized to manage user authentication features efficiently. It includes two key files, `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- `validator.js`: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets specified criteria for authentication.
  
- `auth.py`: The Python file `auth.py` is responsible for handling user authentication processes. It includes functions for user login, registration, and authentication.

## Usage
To utilize the code in this folder:
1. Use the functions defined in `validator.js` to validate user input data before processing it for authentication.
2. Incorporate the functions from `auth.py` to manage user authentication processes such as login, registration, and authentication within the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength evaluation.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username allowing alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Evaluates the strength of a password based on length and character complexity.

**Usage:** Import `InputValidator` class from this file to use the provided validation methods in your authentication logic.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
  - `logout(session_token: str) -> bool`: Ends a user session.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session is valid.

**Usage:** Instantiate `UserAuth` to use the provided authentication functionalities.

**Dependencies:**
- `hashlib`: For hashing functions.
- `json`: For JSON handling.
- `datetime`: For date and time operations.
- `timedelta`: For time duration calculations.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 08:39:14*
