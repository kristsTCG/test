# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. **validator.js**: This JavaScript file contains 1212 characters and is responsible for validating user input data. It ensures that the data provided by users meets the required criteria for authentication.
   
2. **auth.py**: This Python file contains 2198 characters and handles the authentication process for users. It verifies user credentials and grants access based on the authentication rules defined in the project.

## Usage
To work with the code in this folder:
1. Modify the validation rules in `validator.js` to suit the project's requirements.
2. Implement additional authentication logic in `auth.py` as needed.
3. Ensure that both files are integrated correctly with other parts of the project that require user authentication.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username, allowing alphanumeric characters and underscores only.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class where input validation is needed and call the respective validation methods.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user's session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and not expired.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations. Call `register_user` to register a new user, `login` to authenticate and generate a session token, `logout` to end a session, and `is_authenticated` to check session validity.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating expiration time for session tokens.
- `typing`: For type hinting (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-17 17:45:26*
