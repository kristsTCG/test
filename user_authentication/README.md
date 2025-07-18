# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It is responsible for validating user inputs and handling user authentication processes.

## Structure
The folder is organized to handle user authentication logic using both JavaScript and Python. The key components include a JavaScript file for validation (`validator.js`) and a Python file for authentication (`auth.py`).

## Key Files
- `validator.js`: This JavaScript file contains functions for validating user inputs, ensuring data integrity before authentication processes.
- `auth.py`: The Python file `auth.py` is crucial for handling user authentication processes, such as verifying user credentials and managing user sessions.

## Usage
1. To utilize the validation functions, refer to `validator.js` and integrate the validation logic into your user input forms.
2. For user authentication processes, utilize the functions and methods defined in `auth.py` to authenticate users and manage their sessions securely.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength and format of a password (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates the format of a username (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Method to register a new user.
- `login(username: str, password: str) -> Optional[str]`: Method to authenticate a user and return a session token.
- `logout(session_token: str) -> bool`: Method to end a user session.
- `is_authenticated(session_token: str) -> bool`: Method to check if a session token is valid.

**Usage:** Instantiate `UserAuth` to use the provided authentication functionalities.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing.Optional`: For type hinting.

---
*Auto-generated documentation - Last updated: 2025-07-18 01:02:54*
