# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication within the project. This functionality is responsible for validating user input and managing user authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes validator.js for client-side validation written in JavaScript and auth.py for server-side authentication logic written in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic to ensure that user input meets specified criteria before submitting it to the server.
- **auth.py**: The auth.py file contains server-side authentication code to authenticate users based on their credentials and manage user sessions.

## Usage
1. To utilize the client-side validation functionality, refer to the `validator.js` file and integrate the validation logic into your front-end code.
2. For server-side authentication processes, review the `auth.py` file to understand how user authentication is handled on the server side.
3. Make sure to configure the necessary endpoints and integrate the authentication logic with your application's user management system.

By following the instructions in the key files, you can effectively implement user authentication features in your project using the code provided in this folder.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates an email address using a regular expression.
- `validatePassword(password)`: Validates a password based on specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates a username for length (3-20 characters) and alphanumeric characters with underscores only.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication, registration, login, logout, and session validation.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session using the session token.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations like registration, login, logout, and session validation.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization and deserialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 18:09:56*
