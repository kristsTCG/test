# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It includes a JavaScript file for validation and a Python file for authentication.

## Structure
The folder is organized to handle user authentication tasks. The key components include a validator script in JavaScript for input validation and an authentication script in Python for user authentication.

## Key Files
- **validator.js**: This JavaScript file contains 1212 characters and is responsible for validating user inputs to ensure data integrity and security.
- **auth.py**: This Python file contains 2198 characters and handles user authentication processes such as login, registration, and password management.

## Usage
1. To utilize the input validation functionality, refer to the `validator.js` file and integrate the validation logic into your frontend forms or backend APIs.
2. For user authentication tasks, utilize the `auth.py` file by importing the necessary functions and methods to authenticate users during login or registration processes.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters, alphanumeric, and underscores only.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For managing dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-18 04:44:21*
