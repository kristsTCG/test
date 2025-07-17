# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It includes a JavaScript file for validation and a Python file for handling authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It consists of two key files: `validator.js` for client-side validation and `auth.py` for server-side authentication.

## Key Files
1. **validator.js**: This JavaScript file contains client-side validation logic for user inputs. It ensures that user-provided data meets the required criteria before submission.
   
2. **auth.py**: The Python file `auth.py` is responsible for server-side authentication processes. It manages user login, registration, and authentication against the database.

## Usage
1. **validator.js**: To use the validation logic provided in `validator.js`, include the file in your HTML or JavaScript code using a script tag. Call the validation functions as needed to validate user inputs before form submission.

2. **auth.py**: Utilize the functions defined in `auth.py` to handle user authentication tasks on the server-side. Import the necessary functions into your Python codebase and integrate them with your application's user management system.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates an email address using a regular expression.
- `validatePassword(password)`: Validates a password based on length and character requirements.
- `validateUsername(username)`: Validates a username for length and character restrictions.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character complexity.

**Usage:** To use this file, import `InputValidator` class in your code and call the validation functions as needed.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file provides a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash passwords using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user's session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication processes. Call `register_user` to add new users, `login` to authenticate users and generate session tokens, `logout` to end user sessions, and `is_authenticated` to verify active sessions.

**Dependencies:** 
- `hashlib`: for hashing passwords.
- `json`: for JSON serialization and deserialization.
- `datetime`: for working with dates and times.
- `timedelta`: for calculating time differences.
- `typing`: for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 17:02:26*
