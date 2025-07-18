# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript for input validation and `auth.py` written in Python for authentication logic.

## Key Files
1. `validator.js`: This JavaScript file is crucial for validating user input data. It plays a significant role in ensuring that user-provided information meets the required criteria before proceeding with authentication processes.
   
2. `auth.py`: The Python file `auth.py` is responsible for handling user authentication within the project. It contains the necessary logic to authenticate users based on the provided credentials.

## Usage
To utilize the functionality provided in this folder, follow these steps:
1. Use `validator.js` to validate user input data before processing authentication.
2. Implement the authentication logic defined in `auth.py` to authenticate users within the project.
3. Ensure that both files are integrated correctly with other parts of the project that require user authentication functionality.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the format of a password (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates the format of a username (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use its validation and password strength functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** To use this file, create an instance of `UserAuth` and call its methods for user registration, login, logout, and authentication.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 02:08:17*
