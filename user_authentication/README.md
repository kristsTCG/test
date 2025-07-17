# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. This includes validation of user input and authentication logic.

## Structure
The folder `user_authentication` consists of the following files:
- `validator.js`: A JavaScript file containing functions for validating user input. (1212 characters)
- `auth.py`: A Python file implementing user authentication logic. (2198 characters)

## Key Files
### validator.js
This file is crucial for validating user input to ensure data integrity and security. It contains functions for validating various types of user input such as email addresses, passwords, and usernames.

### auth.py
The `auth.py` file is responsible for handling user authentication processes. It includes functions for user login, registration, password hashing, and token generation.

## Usage
1. To utilize the validation functions in `validator.js`, import the necessary functions into your JavaScript files using `import { functionName } from './validator.js'`.
2. Use the validation functions provided in `validator.js` to validate user input before processing or storing it.
3. In Python scripts, import the authentication functions from `auth.py` using `from auth import function_name`.
4. Utilize the authentication functions in `auth.py` for user registration, login, and other authentication-related tasks in your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the format of a password (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates the format of a username (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the provided validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session management, and authentication.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Register a new user with a unique username, email, and hashed password.
- `login(username: str, password: str) -> Optional[str]`: Authenticate user with username and password, returning a session token if successful.
- `logout(session_token: str) -> bool`: End a user session based on the provided session token.
- `is_authenticated(session_token: str) -> bool`: Check if a session token is valid and active.

**Usage:** To use this file, create an instance of the `UserAuth` class and call its methods for user registration, login, logout, and authentication.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 22:38:35*
