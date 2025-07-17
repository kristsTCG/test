# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript for input validation and `auth.py` written in Python for authentication logic.

## Key Files
1. `validator.js`: This JavaScript file is crucial for validating user input. It contains 1212 characters of code dedicated to ensuring that user-provided data meets specified criteria.
   
2. `auth.py`: The Python file `auth.py` plays a vital role in handling user authentication processes. With 2198 characters of code, it manages user login, registration, and authentication within the system.

## Usage
To utilize the functionalities provided in this folder, follow these steps:
1. Modify the validation criteria in `validator.js` as per the project requirements.
2. Implement the authentication logic in `auth.py` to manage user login and registration processes.
3. Ensure that both files are integrated seamlessly with other components of the project that require user authentication functionalities.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates if the input username meets specific criteria (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Determines the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication, registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session by providing the session token.
- `is_authenticated`: Method to check if a session token is valid and the user is authenticated.

**Usage:** Instantiate the `UserAuth` class to use the provided authentication functionalities.

**Dependencies:** 
- `hashlib` for hashing functions.
- `json` for JSON serialization and deserialization.
- `datetime` for date and time operations.
- `timedelta` for calculating time differences.
- `typing` for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 21:48:01*
