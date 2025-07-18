# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript for input validation and `auth.py` written in Python for authentication processes.

## Key Files
1. `validator.js`: This JavaScript file contains functions for validating user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before proceeding with authentication processes.
   
2. `auth.py`: The Python file `auth.py` is responsible for handling user authentication tasks. It manages user login, registration, and authentication processes within the application.

## Usage
To utilize the functionalities provided in this folder:
- Use the functions defined in `validator.js` to validate user input before processing authentication.
- Incorporate the authentication logic from `auth.py` to handle user login, registration, and authentication processes in your application.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates a password based on specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates a username for length (3-20 characters) and alphanumeric characters with underscores only.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Register a new user with a unique username.
- `login(username: str, password: str) -> Optional[str]`: Authenticate a user and return a session token.
- `logout(session_token: str) -> bool`: End a user's session.
- `is_authenticated(session_token: str) -> bool`: Check if a session token is valid.

**Usage:** Instantiate `UserAuth` to manage user authentication. Call `register_user` to add a new user, `login` to authenticate and get a session token, `logout` to end a session, and `is_authenticated` to verify a session token.

**Dependencies:** `hashlib`, `json`, `datetime` from `datetime`, `timedelta` from `datetime`, `Optional` and `Dict` from `typing`.

---
*Auto-generated documentation - Last updated: 2025-07-18 05:52:03*
