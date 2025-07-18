# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- `validator.js`: This file contains functions to validate user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
- `auth.py`: This file handles the authentication logic using Python. It manages user login, registration, and authentication processes.

## Usage
1. To utilize the validation functions provided in `validator.js`, import the file into your JavaScript code and call the necessary functions to validate user input.
2. For authentication tasks, import `auth.py` into your Python project. Use the functions within this file to manage user authentication processes such as login and registration.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username allowing alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Calculates the strength of a password based on various criteria and returns a descriptive level.

**Usage:** This file can be imported using `require` or `import` statements in other JavaScript files to access the input validation utilities provided by the `InputValidator` class.

**Dependencies:** This file does not have any external dependencies and can be used independently for input validation tasks related to user authentication.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and not expired.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-18 08:01:40*
