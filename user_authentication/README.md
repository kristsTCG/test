# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks. It includes two key files, `validator.js` for client-side input validation written in JavaScript, and `auth.py` for server-side authentication logic written in Python.

## Key Files
- `validator.js`: This file contains client-side validation logic to ensure that user input meets specified criteria before submission.
- `auth.py`: The `auth.py` file handles server-side authentication processes, such as verifying user credentials and generating access tokens.

## Usage
1. To utilize the client-side validation functionality, refer to `validator.js` and integrate the validation logic into your front-end code.
2. For server-side authentication tasks, utilize the functions and methods defined in `auth.py` to authenticate users and manage access control within your application.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long, alphanumeric, and contains underscores only.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** Import this file as a module and use the provided validation functions as needed in user authentication processes.

**Dependencies:** None

## auth.py

**Purpose:** User authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user session.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For JSON operations.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 02:04:12*
