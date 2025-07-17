# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized with two key files: `validator.js` written in JavaScript and `auth.py` written in Python. These files handle user input validation and authentication processes respectively.

## Key Files
- `validator.js`: This file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria before authentication.
- `auth.py`: This Python file implements the authentication logic for verifying user credentials and managing user sessions. It is essential for securing user access to the system.

## Usage
1. To utilize the validation functions in `validator.js`, import the file into your JavaScript code and call the appropriate validation functions as needed.
2. For authentication processes, import `auth.py` into your Python code and use the provided functions to authenticate users and manage their sessions securely.

Ensure that you follow the defined validation rules and authentication procedures to maintain the security and integrity of user accounts within the system.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the format of a password (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates the format of a username (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication process.

**Dependencies:** None.

## auth.py

**Purpose:** User authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Register a new user with username, email, and password.
- `login(username: str, password: str) -> Optional[str]`: Authenticate user and return a session token.
- `logout(session_token: str) -> bool`: End a user session.
- `is_authenticated(session_token: str) -> bool`: Check if a session token is valid.

**Usage:** Instantiate `UserAuth` to manage user authentication. Call `register_user` to add a new user, `login` to authenticate and get a session token, `logout` to end a session, and `is_authenticated` to check session validity.

**Dependencies:** hashlib, json, datetime, timedelta, typing.

---
*Auto-generated documentation - Last updated: 2025-07-17 21:47:13*
