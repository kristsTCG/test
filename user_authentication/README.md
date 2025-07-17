# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This module handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication features. It includes validator.js for client-side validation in JavaScript and auth.py for server-side authentication in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic written in JavaScript. It plays a crucial role in ensuring that user input meets specified criteria before submission.
- **auth.py**: The auth.py file is responsible for server-side authentication using Python. It manages user authentication processes, such as login, logout, and session management.

## Usage
1. To utilize client-side validation, refer to the `validator.js` file and integrate the validation logic into your front-end forms.
2. For server-side authentication functionalities, utilize the `auth.py` file by importing and using the defined authentication methods in your backend code.
3. Ensure to maintain the integrity of user authentication processes by following the guidelines and logic implemented in these files.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric and underscore characters.
- `getPasswordStrength(password)`: Calculates the strength of a password and returns a corresponding level.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file provides a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session management, and authentication.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Method to register a new user.
- `login(username: str, password: str) -> Optional[str]`: Method to authenticate a user and return a session token.
- `logout(session_token: str) -> bool`: Method to end a user session.
- `is_authenticated(session_token: str) -> bool`: Method to check if a session token is valid.

**Usage:** Instantiate `UserAuth` class to manage user authentication. Call `register_user` to register a new user, `login` to authenticate and get a session token, `logout` to end a session, and `is_authenticated` to check session validity.

**Dependencies:** `hashlib`, `json`, `datetime`, `timedelta`, `Optional`, `Dict` from `typing` module.

---
*Auto-generated documentation - Last updated: 2025-07-17 15:08:12*
