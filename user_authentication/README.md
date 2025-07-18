# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It includes a JavaScript file for validation logic and a Python file for handling authentication processes.

## Structure
The folder is organized to centralize all user authentication-related code. It currently consists of two key files: `validator.js` for client-side validation and `auth.py` for server-side authentication.

## Key Files
1. **validator.js**: This JavaScript file contains 1212 characters of code responsible for client-side validation of user input. It ensures that user-provided data meets the required criteria before submission.
   
2. **auth.py**: The Python file `auth.py` with 2198 characters of code manages server-side authentication processes. It handles user login, registration, and authentication against the system.

## Usage
To utilize the user authentication features provided in this folder, follow these steps:
1. Modify the `validator.js` file to customize validation rules as per project requirements.
2. Implement the functions in `auth.py` to integrate user authentication logic into the server-side components.
3. Ensure proper communication between client-side validation and server-side authentication for a seamless user experience.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase letters, lowercase letters, and numbers.
- `validateUsername(username)`: Validates the format of a username, allowing only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
  - `hash_password(password: str) -> str`: Hashes the provided password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user with a username and password, returning a session token if successful.
  - `logout(session_token: str) -> bool`: Ends a user session based on the provided session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations like registration, login, logout, and session validation.

**Dependencies:** 
- `hashlib`: Used for hashing passwords.
- `json`: Not used in this file but imported.
- `datetime`: Used for handling date and time operations.
- `timedelta`: Used for calculating expiration time for session tokens.
- `typing`: Used for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 01:50:10*
