# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. It includes scripts for validating user inputs and handling user authentication using JavaScript and Python.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files, `validator.js` for client-side input validation and `auth.py` for server-side authentication logic.

## Key Files
1. `validator.js`: This JavaScript file contains functions for validating user inputs on the client-side. It plays a crucial role in ensuring that user-provided data meets the required criteria before submission.
   
2. `auth.py`: The Python file `auth.py` is responsible for handling user authentication on the server-side. It manages user login, registration, and authentication processes securely.

## Usage
To utilize the user authentication features provided in this folder, follow these steps:
1. Use the functions defined in `validator.js` to validate user inputs on the client-side before submitting any forms.
2. Incorporate the server-side authentication logic from `auth.py` to manage user authentication processes securely on the backend.
3. Ensure that both client-side and server-side scripts work together seamlessly to provide a robust user authentication system.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Determines the strength level of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class into your code and call the desired validation methods as needed.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session based on the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations. Call the provided methods to register users, authenticate logins, manage sessions, and check authentication status.

**Dependencies:** 
- `hashlib`: For hashing functions.
- `json`: For JSON serialization.
- `datetime`: For date and time operations.
- `timedelta`: For time duration calculations.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 21:38:33*
