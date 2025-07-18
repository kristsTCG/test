# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized with two key files:
- `validator.js`: A JavaScript file containing functions for validating user input.
- `auth.py`: A Python file handling user authentication processes.

## Key Files
### validator.js
This file contains functions to validate user input data, ensuring it meets specified criteria before processing.

### auth.py
This Python file manages user authentication processes such as login, logout, and user session management.

## Usage
To utilize the code in this folder:
1. Use the functions defined in `validator.js` to validate user input data before processing.
2. Import and utilize the functions in `auth.py` for user authentication processes within the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on its length and character composition.

**Usage:** Import `InputValidator` class from this file to use its validation functions in user authentication processes.

**Dependencies:** No external dependencies required for this file.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Method to register a new user.
- `login(username: str, password: str) -> Optional[str]`: Method to authenticate a user and return a session token.
- `logout(session_token: str) -> bool`: Method to end a user session.
- `is_authenticated(session_token: str) -> bool`: Method to check if a session is valid.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing functions.
- `json`: For JSON serialization/deserialization.
- `datetime`: For date and time handling.
- `timedelta`: For time duration calculations.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 05:19:06*
