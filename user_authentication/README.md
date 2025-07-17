# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities within the project. It includes files for validating user input and handling authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` for client-side validation in JavaScript and `auth.py` for server-side authentication in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic for user input. It helps ensure that user-provided data meets specified criteria before submission.
  
- **auth.py**: The `auth.py` file handles server-side authentication processes. It manages user authentication, verification, and access control within the application.

## Usage
1. **validator.js**:
   - To use the client-side validation logic, include `validator.js` in your HTML file using a script tag.
   - Call the appropriate validation functions provided in `validator.js` to validate user input fields before form submission.

2. **auth.py**:
   - Import `auth.py` in your Python application to access the authentication functionalities.
   - Utilize the functions defined in `auth.py` to authenticate users, verify credentials, and manage user access permissions.

Ensure to follow the specific usage instructions and guidelines provided within each file for seamless integration and proper functioning of the user authentication features.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username allowing alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Assesses the strength of a password based on various criteria and returns a strength level.

**Usage:** To use this file, import `InputValidator` class in your code and call the desired validation functions or password strength assessment function.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** User authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user authentication operations.
    - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
    - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user.
    - `login(username: str, password: str) -> Optional[str]`: Authenticates user and returns a session token.
    - `logout(session_token: str) -> bool`: Ends a user session.
    - `is_authenticated(session_token: str) -> bool`: Checks if a session is valid.

**Usage:** Instantiate `UserAuth` to use the provided authentication functionalities.

**Dependencies:**
- `hashlib`: For hashing functions.
- `json`: For JSON serialization.
- `datetime`: For date and time operations.
- `timedelta`: For time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 16:41:21*
