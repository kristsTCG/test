# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This functionality is responsible for validating user input and managing user authentication using both JavaScript and Python.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` for client-side validation using JavaScript and `auth.py` for server-side authentication using Python.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation logic for user input. It ensures that user-provided data meets specified criteria before submission.
  
- **auth.py**: The Python file `auth.py` is responsible for server-side authentication processes. It handles user authentication, login, and authorization within the application.

## Usage
To work with the code in this folder:
1. Use `validator.js` to implement client-side validation for user input forms.
2. Utilize `auth.py` to manage server-side user authentication processes, such as login and authorization.
3. Ensure to maintain consistency between client-side and server-side validation to enhance security and user experience.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of being at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character complexity.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and generates a session token for active sessions.
  - `logout(session_token: str) -> bool`: Ends a user session by removing the session token from active sessions.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and active.

**Usage:** This file can be imported into other Python scripts to implement user authentication features.

**Dependencies:**
- `hashlib`: For hashing password using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 18:13:03*
