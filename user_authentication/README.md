# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. `validator.js`: This file contains functions for validating user input. It plays a crucial role in ensuring that user data meets specified criteria before proceeding with authentication processes.
   
2. `auth.py`: This Python file handles the authentication logic for users. It manages user login, registration, and authentication processes within the application.

## Usage
To work with the code in this folder:
1. Review the `validator.js` file to understand the validation rules applied to user input.
2. Explore the `auth.py` file to understand how user authentication is implemented in the project.
3. Modify the validation rules in `validator.js` as needed to customize input validation.
4. Use the functions in `auth.py` to integrate user authentication features into other parts of the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters, alphanumeric, and underscores only.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** User authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user authentication operations.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Register a new user with username, email, and password.
- `login(username: str, password: str) -> Optional[str]`: Authenticate user and return session token.
- `logout(session_token: str) -> bool`: End user session.
- `is_authenticated(session_token: str) -> bool`: Check if session token is valid.

**Usage:** Import `auth.py` and create an instance of `UserAuth` to utilize user authentication functionalities.

**Dependencies:**
- `hashlib`: for hashing functions.
- `json`: for JSON serialization/deserialization.
- `datetime`: for date and time operations.
- `timedelta`: for time differences calculations.
- `typing`: for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 18:32:52*
