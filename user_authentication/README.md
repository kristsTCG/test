# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized with two key files: `validator.js` written in JavaScript and `auth.py` written in Python. These files handle user input validation and authentication logic respectively.

## Key Files
- `validator.js`: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria before proceeding with authentication.
- `auth.py`: The Python file `auth.py` is responsible for handling user authentication processes. It manages user login, registration, and authentication mechanisms within the project.

## Usage
To work with the code in this folder:
1. Review `validator.js` for input validation functions and ensure they are integrated into the user input forms.
2. Utilize `auth.py` for implementing user authentication features such as login, registration, and authentication checks.
3. Ensure that the authentication logic in `auth.py` aligns with the project's security requirements and user experience guidelines.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates a password based on specified criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates a username for length (3-20 characters) and alphanumeric with underscores only.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user session.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations like registration, login, and session handling.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization.
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 22:59:54*
