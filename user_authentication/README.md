# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. `validator.js`: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
   
2. `auth.py`: The Python file `auth.py` is responsible for handling the authentication process. It includes functions for user login, registration, and authentication logic.

## Usage
To utilize the functionalities provided in this folder:
1. Use the functions defined in `validator.js` to validate user input data before processing it for authentication.
2. Import and utilize the functions from `auth.py` to handle user authentication tasks such as login, registration, and authentication logic within your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username, allowing alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types, returning a descriptive level.

**Usage:** Import the `InputValidator` class from this file to access the validation methods.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:** 
- `hashlib` for hashing passwords.
- `json` for JSON serialization.
- `datetime` and `timedelta` from the `datetime` module for handling timestamps.
- `typing` for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 22:28:38*
