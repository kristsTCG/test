# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It includes scripts for validating user input and handling authentication using JavaScript and Python.

## Structure
The folder is organized to handle user authentication tasks efficiently. It consists of two key files: `validator.js` for input validation in JavaScript and `auth.py` for authentication logic in Python.

## Key Files
- **validator.js**: This JavaScript file contains functions for validating user input, ensuring data integrity and security.
- **auth.py**: The Python script `auth.py` manages user authentication processes, such as login, logout, and user session management.

## Usage
1. **validator.js**:
   - To use the validation functions in `validator.js`, import the file into your JavaScript code.
   - Call the appropriate validation functions with user input data to ensure data integrity.

2. **auth.py**:
   - Import `auth.py` into your Python project to access the authentication functionalities.
   - Utilize the provided functions for user login, logout, and session management as needed.

Ensure to follow best practices for user authentication and data validation when working with the code in this folder.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on various criteria.

**Usage:** To use this file, import `InputValidator` class in your code and call the desired validation functions or password strength assessment function.

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

**Dependencies:** `hashlib`, `json`, `datetime`, `timedelta`, `Optional`, `Dict`.

---
*Auto-generated documentation - Last updated: 2025-07-17 16:20:41*
