# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. **validator.js**
   - Language: JavaScript
   - Size: 1212 characters
   - Role: Responsible for validating user input data to ensure it meets the required criteria for authentication.

2. **auth.py**
   - Language: Python
   - Size: 2198 characters
   - Role: Manages the authentication process for users, including login, registration, and session management.

## Usage
1. To utilize the validation capabilities, refer to the `validator.js` file and integrate the validation functions into your user input forms.
   
2. For user authentication functionalities, interact with the `auth.py` file to handle user registration, login, and session management within the project.

Ensure to maintain the integrity of user data and follow security best practices when working with the code in this folder.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with specific length and character requirements.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on various criteria.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
- `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token for active sessions.
- `logout(session_token: str) -> bool`: Ends a user session by removing the session token from active sessions.
- `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and not expired.

**Usage:** Instantiate `UserAuth` to manage user authentication operations like registration, login, and session handling.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization and deserialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 20:38:15*
