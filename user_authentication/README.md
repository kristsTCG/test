# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication features efficiently. It includes validator.js for client-side validation and auth.py for server-side authentication.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation logic for user input. It ensures that user-provided data meets specified criteria before submission.
  
- **auth.py**: The Python file `auth.py` is responsible for server-side authentication processes. It manages user login, registration, and authentication against stored credentials.

## Usage
1. **validator.js**:
   - Modify validation rules as needed to suit project requirements.
   - Include `validator.js` in your HTML files using `<script>` tags.
   - Call validation functions on user input events to enforce validation.

2. **auth.py**:
   - Import `auth.py` in your server-side scripts to utilize authentication functionalities.
   - Implement user registration and login routes using the functions provided in `auth.py`.
   - Ensure proper error handling and secure storage of user credentials.

By following the guidelines above, you can effectively utilize the user authentication features provided in the `user_authentication` folder.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates an email address based on a regular expression pattern.
- `validatePassword(password)`: Validates a password based on specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates a username based on specific criteria (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Method to register a new user.
- `login(username: str, password: str) -> Optional[str]`: Method to authenticate a user and return a session token.
- `logout(session_token: str) -> bool`: Method to end a user session.
- `is_authenticated(session_token: str) -> bool`: Method to check if a session token is valid.

**Usage:** Instantiate `UserAuth` to use the provided authentication functionalities.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 14:51:06*
