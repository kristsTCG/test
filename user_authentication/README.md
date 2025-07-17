# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python. These files handle user input validation and authentication logic respectively.

## Key Files
- `validator.js`: This JavaScript file contains functions for validating user input such as email addresses, passwords, and other user credentials.
- `auth.py`: The Python file `auth.py` is responsible for handling user authentication processes, such as login, logout, and user session management.

## Usage
To work with the code in this folder, you can utilize the functions defined in `validator.js` for validating user input before processing it further. In `auth.py`, you can integrate the authentication logic into your application to ensure secure user authentication processes. Make sure to follow the documentation within each file for proper usage and integration.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the provided validation methods in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** User authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Register a new user with username, email, and password.
- `login(username: str, password: str) -> Optional[str]`: Authenticate user and return a session token.
- `logout(session_token: str) -> bool`: End user session based on the session token.
- `is_authenticated(session_token: str) -> bool`: Check if a session token is valid.

**Usage:** Instantiate `UserAuth` to manage user authentication operations. Call `register_user` to add a new user, `login` to authenticate and generate a session token, `logout` to end a session, and `is_authenticated` to check session validity.

**Dependencies:** `hashlib`, `json`, `datetime`, `timedelta`, `typing`.

---
*Auto-generated documentation - Last updated: 2025-07-17 14:28:04*
