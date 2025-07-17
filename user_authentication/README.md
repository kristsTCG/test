# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
  
- **auth.py**: The Python file `auth.py` is responsible for handling user authentication processes. It manages user login, registration, and authentication logic within the project.

## Usage
To work with the code in this folder:
1. Review the `validator.js` file to understand the validation rules applied to user input data.
2. Explore the `auth.py` file to familiarize yourself with the user authentication logic implemented in Python.
3. Integrate these files into your project to enable user authentication functionalities.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates an email address using a regular expression.
- `validatePassword(password)`: Validates a password based on specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates a username for length (3-20 characters) and allowed characters (alphanumeric and underscores).
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user session.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** You can create an instance of `UserAuth` to handle user authentication operations like registration, login, logout, and session validation.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON operations.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 21:10:16*
