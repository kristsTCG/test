# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` for client-side input validation in JavaScript and `auth.py` for server-side authentication logic in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic to ensure that user input meets specified criteria before submission.
- **auth.py**: The `auth.py` file handles server-side authentication tasks such as verifying user credentials and managing user sessions.

## Usage
1. **validator.js**:
   - Modify the validation rules in `validator.js` to suit the project's requirements.
   - Include `validator.js` in your HTML file using `<script src="path/to/validator.js"></script>`.

2. **auth.py**:
   - Implement additional authentication logic as needed in `auth.py`.
   - Integrate `auth.py` with your server-side code to handle user authentication processes.

Ensure that both files are properly integrated into your project to enable secure and efficient user authentication.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates if a password meets specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates if a username meets specific criteria (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Assesses the strength of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that handles user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token if successful.
  - `logout(session_token: str) -> bool`: Ends a user session based on the provided session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and the user is authenticated.

**Usage:** Instantiate the `UserAuth` class to utilize the provided user authentication functionalities.

**Dependencies:** 
- `hashlib`: Used for hashing passwords.
- `json`: Not used in the provided code but imported.
- `datetime`: Used for handling date and time operations.
- `timedelta`: Used for calculating expiration time for sessions.
- `typing`: Used for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 05:34:17*
