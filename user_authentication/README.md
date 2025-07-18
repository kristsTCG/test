# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This functionality is crucial for managing user access and security.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes validator.js for client-side validation written in JavaScript and auth.py for server-side authentication logic written in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic with 1212 characters. It ensures that user input meets specified criteria before sending it to the server for authentication.
  
- **auth.py**: With 2198 characters, this Python file handles server-side authentication processes. It manages user login, registration, and authentication against stored credentials.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to suit the project's requirements.
   - Include this file in your HTML templates using `<script>` tags to enable client-side validation.

2. **auth.py**:
   - Integrate the authentication logic into your server-side codebase.
   - Utilize the functions provided in this file for user login, registration, and authentication processes.

Ensure that both client-side and server-side components work together seamlessly to provide a secure and user-friendly authentication experience.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username allowing alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on length and character requirements.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by deleting the session token.
- `is_authenticated`: Method to check if a session token is valid and not expired.

**Usage:** To use this file, create an instance of the `UserAuth` class and call its methods for user registration, login, logout, and session validation.

**Dependencies:** 
- `hashlib`: Used for password hashing.
- `json`: Not used in this file but imported.
- `datetime`: Used for date and time operations.
- `timedelta`: Used for calculating session expiration time.
- `typing`: Imported for type hinting purposes.

---
*Auto-generated documentation - Last updated: 2025-07-18 01:52:58*
