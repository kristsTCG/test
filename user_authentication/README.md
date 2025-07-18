# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This file contains functions for validating user input, ensuring data integrity, and preventing malicious input.
- **auth.py**: This file handles user authentication processes such as login, logout, and user session management.

## Usage
1. To use the validation functions in `validator.js`, import the file into your JavaScript code and call the appropriate functions to validate user input.
2. For user authentication tasks, utilize the functions provided in `auth.py`. Import the file into your Python code and call the necessary functions for login, logout, and session management.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username allowing alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation methods in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication, registration, login, logout, and session validation.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session using a session token.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your Python application.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing.Optional`: For type hinting.
- `typing.Dict`: For type hinting.

---
*Auto-generated documentation - Last updated: 2025-07-18 01:36:03*
