# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files, `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
  
- **auth.py**: The Python file `auth.py` is responsible for handling user authentication processes. It manages user login, registration, and authentication logic within the project.

## Usage
To utilize the functionality provided in this folder:
1. Use the functions defined in `validator.js` to validate user input data before processing it further.
2. Incorporate the authentication logic from `auth.py` to manage user authentication tasks such as login and registration.

Ensure that you understand the functions and methods defined in these files to effectively implement user authentication features in the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric and underscores within a specific length range.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** User authentication system with login and registration functionality.

**Key Components:**
- `UserAuth` class: Manages user registration, login, and session handling.
- `hash_password` method: Hashes a password using SHA-256.
- `register_user` method: Registers a new user with a unique username, email, and password.
- `login` method: Authenticates a user and generates a session token for active sessions.
- `logout` method: Ends a user session by removing the session token from active sessions.
- `is_authenticated` method: Checks if a session token is valid and not expired.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib` for password hashing.
- `json` for JSON serialization.
- `datetime` for date and time handling.
- `timedelta` for time duration calculations.
- `typing` for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 22:31:16*
