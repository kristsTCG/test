# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized with two key files: `validator.js` written in JavaScript and `auth.py` written in Python. These files handle user input validation and authentication processes respectively.

## Key Files
1. **validator.js**: This file contains the logic for validating user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before proceeding with authentication.
   
2. **auth.py**: The `auth.py` file is responsible for handling user authentication processes. It contains the necessary functions and methods to authenticate users securely within the system.

## Usage
To work with the code in this folder:
- Review `validator.js` to understand the validation rules and criteria for user input.
- Explore `auth.py` to understand the authentication logic and methods used for user authentication.
- Make necessary modifications or enhancements to suit the project's specific authentication requirements.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of the input password based on length and character types.

**Usage:** This file can be imported as a module in other JavaScript files using `const InputValidator = require('./validator.js');`.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, logout, and session validation.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user's session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and not expired.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating expiration time for session tokens.
- `typing.Optional`, `typing.Dict`: For type hinting.

---
*Auto-generated documentation - Last updated: 2025-07-18 05:41:23*
