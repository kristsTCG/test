# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` for client-side input validation in JavaScript and `auth.py` for server-side authentication logic in Python.

## Key Files
1. **validator.js**
   - Role: Responsible for validating user input on the client-side.
   - Size: 1212 characters
   - Language: JavaScript

2. **auth.py**
   - Role: Manages server-side authentication processes.
   - Size: 2198 characters
   - Language: Python

## Usage
To utilize the user authentication functionalities provided in this folder:
1. Use `validator.js` for client-side input validation by including it in your HTML files and calling its validation functions.
2. Incorporate `auth.py` into your server-side code to handle user authentication processes such as login, registration, and session management. Make sure to configure it according to your project's requirements.

Ensure proper integration and testing of these components to maintain secure user authentication within your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the specified criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates if the input username meets the specified criteria (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Determines the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and generates a session token.
  - `logout(session_token: str) -> bool`: Ends a user session based on the session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Instantiate `UserAuth` to utilize the user authentication functionalities provided in the class.

**Dependencies:**
- `hashlib`: For hashing functions.
- `json`: For JSON serialization and deserialization.
- `datetime`: For working with dates and times.
- `timedelta`: For representing time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 01:06:50*
