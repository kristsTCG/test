# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. It handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes two key files: `validator.js` for client-side validation in JavaScript and `auth.py` for server-side authentication in Python.

## Key Files
1. **validator.js**: This JavaScript file contains 1212 characters and is responsible for client-side validation of user input. It ensures that user data meets specified criteria before submission.
   
2. **auth.py**: With 2198 characters, `auth.py` is a Python file that manages server-side authentication processes. It handles user login, registration, and authentication against the database.

## Usage
1. **validator.js**:
   - To use the client-side validation functionality, include `validator.js` in your HTML file using a script tag.
   - Call the appropriate validation functions defined in `validator.js` on user input fields to validate user data before form submission.

2. **auth.py**:
   - Import `auth.py` in your Python project to utilize the authentication functionalities.
   - Use the provided functions in `auth.py` to handle user registration, login, and authentication processes within your application.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates a password based on specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates a username for length (3-20 characters) and alphanumeric with underscores only.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in other parts of the application.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and hashed password.
- `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token for active sessions.
- `logout(session_token: str) -> bool`: Ends a user session by removing the session token from active sessions.
- `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and not expired.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:** 
- `hashlib` for hashing functions.
- `json` for JSON serialization (not used in this file).
- `datetime` for date and time operations.
- `timedelta` for time differences.
- `typing.Optional` for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 14:19:52*
