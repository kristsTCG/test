# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. These files handle user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes validator.js for client-side validation in JavaScript and auth.py for server-side authentication in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic for user inputs. It helps ensure that user-provided data meets specified criteria before submission.
  
- **auth.py**: This file is responsible for server-side authentication processes. It manages user authentication, login, and session handling on the server side.

## Usage
1. **validator.js**: To utilize the client-side validation provided by `validator.js`, include this file in your HTML file using a `<script>` tag. You can then call the validation functions defined in this file to validate user inputs before form submission.

2. **auth.py**: To implement server-side authentication using `auth.py`, ensure that this file is imported or included in your server-side codebase. Use the functions defined in `auth.py` to authenticate users, handle login requests, and manage user sessions securely.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the specified criteria.
- `validateUsername(username)`: Validates if the input username meets the specified criteria.
- `getPasswordStrength(password)`: Calculates the strength level of a given password based on length and character types.

**Usage:** To use this file, import `InputValidator` class where needed and call the validation functions or password strength function as required.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is still valid.

**Usage:** Instantiate `UserAuth` to use the provided authentication functionalities.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For JSON operations.
- `datetime`: For handling date and time.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 01:44:42*
