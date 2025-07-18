# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This module handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication features efficiently. It includes validator.js for client-side validation and auth.py for server-side authentication.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation logic for user inputs. It ensures that user-provided data meets specified criteria before submission.
- **auth.py**: The Python file `auth.py` is responsible for server-side authentication processes. It manages user login, registration, and authentication using secure methods.

## Usage
1. To utilize the client-side validation functionality, refer to `validator.js` and integrate the validation logic into your front-end forms.
2. For server-side authentication, utilize the functions and methods defined in `auth.py` to handle user authentication processes securely.
3. Ensure to maintain the integrity and security of user data by following best practices outlined in the authentication files.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength level of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file provides a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session management, and authentication.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Method to register a new user with a unique username, email, and password.
- `login(username: str, password: str) -> Optional[str]`: Method to authenticate a user and generate a session token for active sessions.
- `logout(session_token: str) -> bool`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated(session_token: str) -> bool`: Method to check if a session token is valid and still active.

**Usage:** Instantiate `UserAuth` class to utilize user authentication functionalities like registration, login, logout, and session validation.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 09:02:38*
