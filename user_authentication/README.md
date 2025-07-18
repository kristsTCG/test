# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It includes scripts for validating user input and handling authentication processes.

## Structure
The folder is organized to manage user authentication logic efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This JavaScript file (1212 characters) is responsible for validating user input data for authentication processes. It ensures that the data provided by users meets the required criteria for authentication.
  
- **auth.py**: This Python file (2198 characters) handles the authentication processes for users. It includes functions for user login, registration, and authentication checks.

## Usage
To utilize the code in this folder:
1. Review the `validator.js` file for input validation logic.
2. Explore the `auth.py` file to understand the authentication processes.
3. Modify the files as needed to customize user authentication functionalities for the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the required criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates if the input username meets the criteria (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Determines the strength of the input password based on length and character types.

**Usage:** This file can be imported into other JavaScript files using `require` or `import` statements to perform input validation for user authentication.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session creation, and session validation.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user's session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and not expired.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 04:12:26*
