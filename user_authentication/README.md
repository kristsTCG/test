# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files, `validator.js` for client-side validation written in JavaScript and `auth.py` for server-side authentication logic written in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic to ensure that user input meets specified criteria before submitting it to the server for authentication.
- **auth.py**: The `auth.py` file is responsible for handling server-side authentication processes. It manages user login, registration, and authentication using Python.

## Usage
1. **validator.js**:
   - Modify the validation rules in `validator.js` to suit the specific requirements of the project.
   - Include `validator.js` in your HTML files using `<script>` tags to enable client-side validation.

2. **auth.py**:
   - Implement additional authentication features as needed by extending the functionality in `auth.py`.
   - Integrate `auth.py` with your backend server to handle user authentication requests.

Ensure that both client-side and server-side authentication processes are in sync to provide a secure and seamless user authentication experience.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of a password and returns a descriptive level.

**Usage:** To use this file, import `InputValidator` class where input validation is needed and call the appropriate validation functions or password strength function.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and hashed password.
- `login(username: str, password: str) -> Optional[str]`: Authenticates a user and generates a session token for active sessions.
- `logout(session_token: str) -> bool`: Ends a user session by removing the session token from active sessions.
- `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and has not expired.

**Usage:** This file can be imported into other Python scripts to handle user authentication tasks.

**Dependencies:** 
- `hashlib`: for hashing functions.
- `json`: for JSON serialization/deserialization.
- `datetime`: for working with dates and times.
- `timedelta`: for calculating time differences.
- `typing`: for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 01:27:25*
