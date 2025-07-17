# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes the following key components:
- `validator.js`: A JavaScript file containing functions for validating user input data.
- `auth.py`: A Python file responsible for handling user authentication processes.

## Key Files
### validator.js
- Role: Provides functions for validating user input data.
- Size: 1212 characters
- Language: JavaScript

### auth.py
- Role: Manages user authentication processes such as login, registration, and password reset.
- Size: 2198 characters
- Language: Python

## Usage
1. To utilize the validation functions in `validator.js`, import the necessary functions into your JavaScript files.
2. Use the functions provided in `auth.py` to handle user authentication tasks such as user login, registration, and password reset.
3. Ensure to follow the documentation within each file for specific usage instructions and parameters.

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

**Purpose:** This file provides a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: Used for hashing passwords.
- `json`: Not currently used but imported.
- `datetime`: Used for working with date and time.
- `timedelta`: Used for calculating time differences.
- `typing`: Used for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 21:20:02*
