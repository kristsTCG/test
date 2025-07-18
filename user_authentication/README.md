# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
- **auth.py**: The Python file `auth.py` is responsible for handling the authentication logic. It manages user authentication processes such as login, logout, and session management.

## Usage
1. To utilize the validation functions provided in `validator.js`, import the file into your JavaScript code and call the necessary functions to validate user input data.
2. For authentication processes, import `auth.py` into your Python code. Use the functions within this file to manage user authentication tasks such as login and session handling.

Ensure that you follow the guidelines and conventions set within these files to maintain a secure and efficient user authentication system in your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of being at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is between 3 to 20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in other parts of the application.

**Dependencies:** None.

## auth.py

**Purpose:** User authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class for managing user authentication.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates user and returns a session token.
  - `logout(session_token: str) -> bool`: Ends a user session.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session is valid.

**Usage:** Instantiate `UserAuth` to manage user authentication, registration, login, logout, and session validation.

**Dependencies:** `hashlib`, `json`, `datetime`, `timedelta`, `Optional`, `Dict`.

---
*Auto-generated documentation - Last updated: 2025-07-18 02:41:57*
