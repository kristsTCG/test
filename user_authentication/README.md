# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities in the project. It includes validation logic in JavaScript and authentication logic in Python.

## Structure
The folder is organized to handle user authentication tasks. It contains two key files, `validator.js` for input validation and `auth.py` for user authentication.

## Key Files
- **validator.js**: This file contains JavaScript code (1212 characters) responsible for validating user input data.
- **auth.py**: This Python file (2198 characters) handles user authentication processes such as login, registration, and password management.

## Usage
1. Use `validator.js` to validate user input data by importing and calling the validation functions where necessary.
2. Utilize `auth.py` for user authentication tasks like user login, registration, and password management. Ensure to follow the defined functions and methods for authentication processes.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on its length and character composition.

**Usage:** Import the `InputValidator` class from this file to use the validation methods in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file provides a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
  - `logout(session_token: str) -> bool`: Ends a user session based on the session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Instantiate `UserAuth` to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing functions.
- `json`: For JSON serialization and deserialization.
- `datetime`: For date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hinting support.

---
*Auto-generated documentation - Last updated: 2025-07-18 01:57:20*
