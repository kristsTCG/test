# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` for client-side input validation in JavaScript and `auth.py` for server-side authentication logic in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic written in JavaScript. It ensures that user input meets specified criteria before submitting it for authentication.
  
- **auth.py**: The `auth.py` file contains server-side authentication logic written in Python. It handles user authentication processes, such as verifying credentials and generating access tokens.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed by updating the functions in this file.
   - Include `validator.js` in your HTML files using `<script src="path/to/validator.js"></script>`.

2. **auth.py**:
   - Implement additional authentication logic by extending the existing functions in this file.
   - Integrate `auth.py` with your backend server to enable user authentication.

Ensure that both files work together seamlessly to provide a secure and reliable user authentication system.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength evaluation.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the required criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates if the input username meets the criteria (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Evaluates the strength of a password based on length and character types.

**Usage:** This file can be imported into other JavaScript files using `require` or `import` statements to access the input validation functions provided by the `InputValidator` class.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and hashed password.
- `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token for active sessions.
- `logout(session_token: str) -> bool`: Ends a user session by removing the session token from active sessions.
- `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and active.

**Usage:** To use this file, create an instance of `UserAuth` and call its methods for user registration, login, logout, and authentication.

**Dependencies:** 
- `hashlib`: for hashing passwords using SHA-256.
- `json`: for JSON serialization and deserialization.
- `datetime`: for working with dates and times.
- `timedelta`: for calculating time differences.
- `typing`: for type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 00:29:02*
