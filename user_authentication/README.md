# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It includes scripts for validating user input and handling authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python. These files work together to ensure secure user authentication within the application.

## Key Files
1. **validator.js**: This JavaScript file is 1212 characters long and is responsible for validating user input related to authentication. It ensures that user data meets the required criteria before proceeding with authentication processes.

2. **auth.py**: This Python file is 2198 characters long and handles the authentication logic within the application. It manages user login, registration, and authentication processes securely.

## Usage
To work with the code in this folder:
- Review `validator.js` to understand the validation rules for user input.
- Explore `auth.py` to understand the authentication logic and processes implemented in Python.
- Ensure that both files are integrated correctly within the project to maintain secure user authentication functionalities.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length and character requirements.
- `validateUsername(username)`: Validates the format of a username allowing alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character complexity.

**Usage:** Import `InputValidator` class from this file to use the provided validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Register a new user with a unique username, email, and password.
- `login(username: str, password: str) -> Optional[str]`: Authenticate user credentials and return a session token.
- `logout(session_token: str) -> bool`: End a user's session by invalidating the session token.
- `is_authenticated(session_token: str) -> bool`: Check if a session token is valid and not expired.

**Usage:** Instantiate `UserAuth` to manage user authentication operations. Call `register_user` to add new users, `login` to authenticate users and get a session token, `logout` to end a session, and `is_authenticated` to check session validity.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing.Optional`: For type hinting of optional return values.
- `typing.Dict`: For type hinting of dictionary structures.

---
*Auto-generated documentation - Last updated: 2025-07-18 00:21:42*
