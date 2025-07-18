# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript for input validation and `auth.py` written in Python for authentication processes.

## Key Files
1. **validator.js**: This file is responsible for validating user input data. It contains functions to ensure that user-provided data meets the required criteria and is safe for processing.
   
2. **auth.py**: This Python file handles user authentication tasks such as login, registration, and session management. It implements the logic for verifying user credentials and managing user sessions securely.

## Usage
1. **validator.js**:
   - To use the validation functions in `validator.js`, import the file into your JavaScript code.
   - Call the appropriate validation functions with user input data as parameters to validate the input.
   - Handle the validation results accordingly in your application logic.

2. **auth.py**:
   - Import `auth.py` into your Python code to access the authentication functionalities.
   - Utilize the provided functions for user registration, login, and session management.
   - Ensure to securely integrate the authentication logic into your application to protect user data.

Ensure to follow best practices for user authentication and data validation when working with the code in this folder.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username allowing alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class in your code and call the validation functions as needed.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your Python application.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in the provided code snippet).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 02:51:03*
