# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This module is responsible for validating user input and handling authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes validator.js for client-side input validation and auth.py for server-side authentication logic.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation logic for user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before submission.
  
- **auth.py**: The Python file `auth.py` is responsible for server-side authentication processes. It manages user authentication, login, and authorization within the system.

## Usage
1. **validator.js**:
   - To use the client-side validation logic provided in `validator.js`, include this file in your HTML document using `<script src="path/to/validator.js"></script>`.
   - Utilize the functions defined in `validator.js` to validate user input fields before submitting forms.

2. **auth.py**:
   - Import `auth.py` in your Python project to access the authentication functionalities.
   - Use the methods defined in `auth.py` to authenticate users, handle login processes, and manage user authorization within the system.

Ensure that you follow the guidelines and best practices outlined in each file for secure and efficient user authentication in your project.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates if a password meets specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates if a username meets specific criteria (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user session.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate `UserAuth` to utilize user authentication functionalities like registration, login, logout, and session validation.

**Dependencies:** 
- `hashlib` for hashing passwords.
- `json` for JSON serialization (not used in this file).
- `datetime` for date and time operations.
- `timedelta` for calculating time differences.
- `typing` for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 08:05:58*
