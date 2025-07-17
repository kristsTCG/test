# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- `validator.js`: This file contains JavaScript code for validating user input. It plays a crucial role in ensuring that user data meets the required criteria before authentication.
- `auth.py`: The Python file `auth.py` is responsible for handling user authentication logic. It manages user login, registration, and authentication processes within the project.

## Usage
To work with the code in this folder:
1. Review `validator.js` to understand the validation rules applied to user input.
2. Explore `auth.py` to grasp the authentication logic and processes implemented in Python.
3. Make necessary modifications or enhancements to the validation and authentication mechanisms as per project requirements.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength level of a password based on various criteria.

**Usage:** To use this file, import `InputValidator` class from `validator.js` and call the desired validation methods as needed.

**Dependencies:** No external dependencies required for this file.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token if successful.
  - `logout(session_token: str) -> bool`: Ends a user session based on the provided session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and active.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your Python application.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization and deserialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing.Optional`: For type hinting optional return values.
- `typing.Dict`: For type hinting dictionary structures.

---
*Auto-generated documentation - Last updated: 2025-07-17 14:17:22*
