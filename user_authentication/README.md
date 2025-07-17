# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication features efficiently. It includes two key files, `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user data meets the required criteria before proceeding with authentication processes.
  
- **auth.py**: The Python file `auth.py` is responsible for handling user authentication logic. It manages user login, registration, and authentication processes within the system.

## Usage
To work with the code in this folder:
1. Review `validator.js` to understand the validation rules and functions used for user input data.
2. Explore `auth.py` to grasp the authentication logic and processes implemented for user login and registration.
3. Integrate these files into the project's authentication system as needed.
4. Ensure to maintain the integrity and security of user authentication processes by following best practices outlined in the code files.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the provided validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user's session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** This file can be imported into other Python scripts to handle user authentication processes.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-17 18:42:05*
