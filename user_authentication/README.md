# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It handles validation and authentication of user credentials.

## Structure
The folder is organized to manage user authentication processes efficiently. It includes validator.js for client-side validation and auth.py for server-side authentication.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation logic for user input. It ensures that user-provided data meets specified criteria before submission.
- **auth.py**: The Python file `auth.py` is responsible for server-side authentication. It manages user login, registration, and authentication processes.

## Usage
1. **validator.js**:
   - Modify validation rules as needed for user input fields.
   - Include `validator.js` in your HTML files using `<script>` tags.
   - Call validation functions on form submission events.

2. **auth.py**:
   - Configure database connections and user authentication settings.
   - Import `auth.py` in your main application file to handle user authentication.
   - Use the provided functions for user login, registration, and authentication processes.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Assesses the strength of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class and call the desired validation functions or password strength assessment function.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
  - `logout(session_token: str) -> bool`: Ends a user session.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session is valid.

**Usage:** Instantiate `UserAuth` to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 21:53:12*
