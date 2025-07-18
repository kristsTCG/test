# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. This folder handles validation and authentication processes for user accounts.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes two key files: `validator.js` for client-side validation written in JavaScript and `auth.py` for server-side authentication written in Python.

## Key Files
1. `validator.js`: This file contains client-side validation logic for user input. It ensures that user-provided data meets specific criteria before submitting it to the server for authentication.
   
2. `auth.py`: The `auth.py` file handles server-side authentication processes. It verifies user credentials, generates authentication tokens, and manages user sessions securely on the server side.

## Usage
To utilize the user authentication functionalities in this folder:
1. Modify the validation criteria in `validator.js` to suit the project's requirements.
2. Implement the necessary server-side authentication logic in `auth.py` to authenticate users securely.
3. Ensure that both client-side and server-side scripts work together seamlessly to provide a robust user authentication system.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of being at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of a password based on its length and character composition.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username.
- `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
- `logout(session_token: str) -> bool`: Ends a user session based on the session token.
- `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and not expired.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your application.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For working with JSON data.
- `datetime`: For managing dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints in function signatures.

---
*Auto-generated documentation - Last updated: 2025-07-18 03:54:30*
