# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. These files handle user validation and authentication processes.

## Structure
The folder is organized to include two key files: `validator.js` written in JavaScript and `auth.py` written in Python. These files are responsible for validating user input and managing user authentication, respectively.

## Key Files
1. **validator.js**
   - Role: Handles user input validation.
   - Language: JavaScript
   - Size: 1212 characters

2. **auth.py**
   - Role: Manages user authentication processes.
   - Language: Python
   - Size: 2198 characters

## Usage
1. **validator.js**
   - To use the `validator.js` file, import it into your JavaScript code using `import validator from './validator.js';`.
   - Utilize the functions within `validator.js` to validate user input before proceeding with authentication processes.

2. **auth.py**
   - To work with `auth.py`, ensure you have Python installed on your system.
   - Import `auth.py` into your Python code using `import auth`.
   - Use the functions provided in `auth.py` to authenticate users within your application.

Ensure to follow the documentation within each file for specific usage instructions and function details.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric and underscores within a specific length range.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class where input validation is required.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and hashed password.
- `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token if successful.
- `logout(session_token: str) -> bool`: Ends a user session based on the provided session token.
- `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and not expired.

**Usage:** Instantiate the `UserAuth` class to use the provided user authentication functionalities.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization and deserialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 20:33:00*
