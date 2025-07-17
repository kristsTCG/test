# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. These files handle validation and authentication processes for user accounts.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes two key files, `validator.js` and `auth.py`, which are responsible for validating user input and handling authentication logic, respectively.

## Key Files
- **validator.js**: This JavaScript file contains functions for validating user input data, ensuring that it meets specified criteria before proceeding with authentication processes.
- **auth.py**: This Python file manages the authentication process for user accounts, including verifying credentials and granting access to authorized users.

## Usage
1. **validator.js**:
   - To use the validation functions in `validator.js`, import the file into your JavaScript code.
   - Call the appropriate validation functions provided in `validator.js` to validate user input data before processing it further.

2. **auth.py**:
   - Import `auth.py` into your Python code to access the authentication functionalities.
   - Utilize the authentication methods defined in `auth.py` to authenticate users based on their credentials and manage user sessions.

Ensure to follow the specific usage instructions within each file to effectively implement user authentication features in your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character complexity.

**Usage:** To use this file, import `InputValidator` class from `validator.js` and call the desired validation functions or password strength calculation function.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, logout, and session validation.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 16:28:16*
