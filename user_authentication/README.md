# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` for client-side input validation written in JavaScript and `auth.py` for server-side authentication logic written in Python.

## Key Files
1. **validator.js**
   - Role: Responsible for client-side input validation.
   - Size: 1212 characters
   - Language: JavaScript

2. **auth.py**
   - Role: Manages server-side authentication processes.
   - Size: 2198 characters
   - Language: Python

## Usage
1. **validator.js**
   - Ensure the file is included in the appropriate HTML file using `<script>` tags.
   - Use the functions provided in `validator.js` to validate user input on the client-side before submitting forms.

2. **auth.py**
   - Integrate the authentication logic from `auth.py` into the server-side codebase.
   - Utilize the functions and methods defined in `auth.py` for user authentication processes, such as login, registration, and session management.

By following the guidelines outlined in the key files, developers can effectively implement user authentication features in the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the specified criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates if the input username meets the specified criteria (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Calculates the strength of the input password based on its length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session management, and authentication.
  - `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Register a new user with a unique username.
  - `login(username: str, password: str) -> Optional[str]`: Authenticate user and return a session token.
  - `logout(session_token: str) -> bool`: End a user session based on the session token.
  - `is_authenticated(session_token: str) -> bool`: Check if a session token is valid.

**Usage:** Instantiate `UserAuth` to manage user authentication operations like registration, login, and session management.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in the provided code snippet).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating expiration time for session tokens.
- `typing.Optional`: For type hinting the return value of the `login` method.

---
*Auto-generated documentation - Last updated: 2025-07-17 17:49:15*
