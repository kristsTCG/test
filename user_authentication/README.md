# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It consists of two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
  
- **auth.py**: The Python file `auth.py` is responsible for handling user authentication processes. It manages user login, registration, and authentication logic within the system.

## Usage
To utilize the code in this folder effectively, follow these steps:
1. Review the `validator.js` file to understand the validation rules and functions available.
2. Explore the `auth.py` file to familiarize yourself with the authentication logic implemented in Python.
3. Integrate these files into your project to enable user authentication functionalities.
4. Ensure to call the appropriate functions from `validator.js` and `auth.py` as needed in your project's authentication flow.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
  - `hash_password(password: str) -> str`: Hashes the password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
  - `logout(session_token: str) -> bool`: Ends a user session based on the session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization and deserialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 06:10:50*
