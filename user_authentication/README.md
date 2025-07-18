# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It handles tasks such as validating user input and managing user authentication using JavaScript and Python scripts.

## Structure
The folder is organized to separate the validation logic (validator.js) written in JavaScript and the authentication logic (auth.py) written in Python.

## Key Files
- **validator.js**: This JavaScript file contains the validation logic for user input. It ensures that the data entered by the user meets the required criteria before proceeding with authentication.
- **auth.py**: The Python script `auth.py` is responsible for managing user authentication processes. It handles tasks such as user login, registration, and authentication verification.

## Usage
1. **validator.js**:
   - To use the validation logic in `validator.js`, import the file into your JavaScript code.
   - Call the appropriate validation functions provided in `validator.js` to validate user input before proceeding with authentication.

2. **auth.py**:
   - Import `auth.py` into your Python code to access the authentication functionalities.
   - Utilize the functions defined in `auth.py` to handle user authentication processes such as login, registration, and authentication verification.

Ensure that you understand the specific functions and methods provided in each file to effectively implement user authentication within your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Determines the strength level of a password based on length and character types.

**Usage:** This file can be imported as a module to perform input validation tasks in user authentication processes.

**Dependencies:** No external dependencies are required for this file.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user session.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** To use this file, create an instance of `UserAuth` and call its methods for user registration, login, logout, and session validation.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 06:00:14*
