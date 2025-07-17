# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized with two key files: `validator.js` written in JavaScript and `auth.py` written in Python. These files handle user input validation and authentication logic respectively.

## Key Files
- **validator.js**: This file contains functions for validating user input, ensuring that data entered by users meets specified criteria.
- **auth.py**: Responsible for handling user authentication processes, such as verifying user credentials and managing user sessions.

## Usage
To utilize the functionality provided by this folder:
1. Use the functions defined in `validator.js` to validate user input before processing it.
2. Incorporate the authentication logic from `auth.py` to authenticate users and manage their sessions within the application.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of being at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is between 3 to 20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on its length and character composition.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
  - `logout(session_token: str) -> bool`: Ends a user session.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session is valid.

**Usage:** Instantiate `UserAuth` to utilize user authentication functionalities.

**Dependencies:** 
- `hashlib` for hashing functions.
- `json` for JSON serialization.
- `datetime` and `timedelta` from `datetime` module for handling timestamps.
- `typing.Optional` and `typing.Dict` for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 23:09:49*
