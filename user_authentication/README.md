# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
### validator.js
- Role: Responsible for validating user input data.
- Size: 1212 characters
- Language: JavaScript

### auth.py
- Role: Manages user authentication processes.
- Size: 2198 characters
- Language: Python

## Usage
1. To utilize the validation functionality, refer to `validator.js` for methods and rules for validating user input.
2. For user authentication tasks, interact with `auth.py` to handle authentication processes such as login, registration, and password management.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long, alphanumeric, and allows underscores.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in other parts of the application.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user registration, login, and session handling.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Register a new user with a unique username.
- `login(username: str, password: str) -> Optional[str]`: Authenticate user and return a session token.
- `logout(session_token: str) -> bool`: End a user session.
- `is_authenticated(session_token: str) -> bool`: Check if a session token is valid.

**Usage:** Instantiate `UserAuth` to manage user authentication. Call `register_user` to add new users, `login` to authenticate users and get a session token, `logout` to end a session, and `is_authenticated` to check session validity.

**Dependencies:** `hashlib`, `json`, `datetime`, `timedelta`, `Optional`, `Dict`

---
*Auto-generated documentation - Last updated: 2025-07-18 09:00:11*
