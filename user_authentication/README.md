# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. It includes scripts for validating user input and handling user authentication using JavaScript and Python.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` for client-side input validation and `auth.py` for server-side authentication logic.

## Key Files
1. **validator.js**: This JavaScript file contains 1212 characters of code responsible for validating user input on the client-side. It ensures that user-provided data meets the required criteria before submission.
   
2. **auth.py**: The `auth.py` file, written in Python and consisting of 2198 characters, manages server-side authentication processes. It handles user login, registration, and authentication tasks securely.

## Usage
To utilize the functionality provided by the `user_authentication` folder, follow these steps:
1. Include `validator.js` in your HTML file to enable client-side input validation.
2. Use `auth.py` in your server-side code to implement user authentication features such as login, registration, and authentication.
3. Ensure that the code in both files is integrated correctly with your project's existing authentication system for seamless user authentication processes.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric and underscore characters.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on various criteria.

**Usage:** To use this file, import `InputValidator` class where input validation is needed.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, logout, and session authentication.
- `hash_password`: Method to hash passwords using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user's session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to access user authentication functionalities.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hinting in function definitions.

---
*Auto-generated documentation - Last updated: 2025-07-17 23:27:45*
