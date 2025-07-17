# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication logic.

## Structure
The folder consists of two key files: `validator.js` written in JavaScript and `auth.py` written in Python. These files handle user input validation and authentication processes respectively.

## Key Files
1. `validator.js`: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria before proceeding with authentication.
   
2. `auth.py`: The Python file `auth.py` is responsible for handling user authentication processes. It contains functions for verifying user credentials and managing user sessions.

## Usage
To utilize the functionality provided in this folder:
- Use the functions defined in `validator.js` to validate user input data before authentication.
- Incorporate the authentication logic from `auth.py` to authenticate users and manage their sessions within the application.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username restricting it to alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character complexity, returning a descriptive level.

**Usage:** Import the `InputValidator` class from this file to access the validation methods.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints in function definitions.

---
*Auto-generated documentation - Last updated: 2025-07-17 14:17:46*
