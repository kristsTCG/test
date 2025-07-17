# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` for client-side input validation written in JavaScript and `auth.py` for server-side authentication logic written in Python.

## Key Files
1. **validator.js**
   - Role: Handles client-side input validation for user authentication forms.
   - Path: `user_authentication/validator.js`
   - Size: 1212 characters

2. **auth.py**
   - Role: Manages server-side authentication processes such as user login, registration, and session management.
   - Path: `user_authentication/auth.py`
   - Size: 2198 characters

## Usage
1. **validator.js**
   - To use the client-side input validation functionality:
     - Include `validator.js` in your HTML file using `<script src="path/to/validator.js"></script>`.
     - Call the validation functions provided in `validator.js` on form submission events.

2. **auth.py**
   - To utilize the server-side authentication logic:
     - Import `auth.py` in your Python project using `from user_authentication import auth`.
     - Use the functions defined in `auth.py` for user login, registration, and session management.

Ensure to follow the documentation within each file for specific usage instructions and customization options.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long, alphanumeric, and contains underscores only.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user session.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization.
- `datetime`: For handling dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 20:16:41*
