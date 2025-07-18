# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes validator.js for client-side validation and auth.py for server-side authentication.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation logic for user inputs. It ensures that user-provided data meets the required criteria before submission.
- **auth.py**: The Python file `auth.py` is responsible for server-side authentication. It handles user login, registration, and authentication processes securely.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to suit the project's requirements.
   - Include `validator.js` in your HTML files using `<script>` tags to enable client-side validation.

2. **auth.py**:
   - Implement additional authentication methods or customize existing ones based on project needs.
   - Integrate `auth.py` with your server-side application logic to manage user authentication securely.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Determines the strength level of a password based on length and character requirements.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication, registration, login, logout, and session validation.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication. Call `register_user` to add a new user, `login` to authenticate and generate a session token, `logout` to end a session, and `is_authenticated` to validate an active session.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-18 06:56:26*
