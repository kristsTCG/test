# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
- **auth.py**: The `auth.py` file contains authentication logic written in Python. It manages user authentication processes such as login, registration, and session management.

## Usage
To utilize the functionality provided in this folder:
1. Review the `validator.js` file to understand the validation rules applied to user input.
2. Explore the `auth.py` file to understand the authentication logic implemented in Python.
3. Integrate these files into your project to handle user authentication securely and efficiently.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates if a password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if a username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of a password based on its length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Register a new user with a unique username, email, and password.
- `login(username: str, password: str) -> Optional[str]`: Authenticate user credentials and return a session token.
- `logout(session_token: str) -> bool`: End a user session by invalidating the session token.
- `is_authenticated(session_token: str) -> bool`: Check if a session token is valid and active.

**Usage:** To use this file, create an instance of `UserAuth` and call its methods for user registration, login, session management, and authentication.

**Dependencies:** 
- `hashlib`: Used for hashing passwords.
- `json`: Imported but not used in the provided code.
- `datetime`: Used for handling timestamps and session expiration.
- `timedelta`: Used for calculating session expiration time.
- `typing.Optional`: Used for type hinting in method signatures.
- `typing.Dict`: Used for type hinting in method signatures.

---
*Auto-generated documentation - Last updated: 2025-07-17 23:07:19*
