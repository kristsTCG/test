# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This module handles user validation and authentication processes.

## Structure
The folder is organized to separate validation logic in `validator.js` written in JavaScript and authentication logic in `auth.py` written in Python.

## Key Files
- `validator.js`: This file contains the logic for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria before proceeding with authentication.
  
- `auth.py`: This file is responsible for handling user authentication processes. It manages user login, registration, and authentication using Python.

## Usage
1. To work with the validation logic, refer to `validator.js` and understand the validation rules implemented.
2. For user authentication tasks, utilize `auth.py` to manage user login, registration, and authentication processes.
3. Ensure to integrate these files with other components of the project that require user authentication functionalities.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength level of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user registration, login, and session management.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Register a new user with a unique username, email, and hashed password.
- `login(username: str, password: str) -> Optional[str]`: Authenticate a user and return a session token.
- `logout(session_token: str) -> bool`: End a user session based on the session token.
- `is_authenticated(session_token: str) -> bool`: Check if a session token is valid and active.

**Usage:** Instantiate `UserAuth` to use the provided user authentication functionalities.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 23:00:38*
