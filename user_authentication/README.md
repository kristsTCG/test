# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities in the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. **validator.js**: This file contains client-side validation logic for user input. It ensures that user-provided data meets the required criteria before submission.
   
2. **auth.py**: The `auth.py` file contains server-side authentication logic written in Python. It handles user authentication processes, such as login, registration, and session management.

## Usage
1. **validator.js**:
   - To use the validation logic in `validator.js`, include the file in your HTML file using a script tag.
   - Call the validation functions provided in `validator.js` on user input fields to validate user input before form submission.

2. **auth.py**:
   - To utilize the authentication functionalities in `auth.py`, import the necessary functions into your Python project.
   - Use the functions provided in `auth.py` for user registration, login authentication, and managing user sessions.

Ensure that you understand the specific functions and methods provided in each file to effectively implement user authentication in your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the format of a password (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates the format of a username (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** User authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate `UserAuth` class to utilize user authentication functionalities.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization.
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 02:27:39*
