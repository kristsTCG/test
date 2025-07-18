# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. These files handle user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes two key files: `validator.js` and `auth.py`.

## Key Files
- `validator.js`: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
- `auth.py`: This Python file manages the authentication process for users. It handles user login, registration, and authentication using secure methods.

## Usage
1. To utilize the validation functions provided in `validator.js`, import the file into your JavaScript code and call the necessary functions to validate user input data.
2. For user authentication tasks, import `auth.py` into your Python code. Use the functions within this file to handle user login, registration, and authentication processes securely.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates a password based on specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates a username for length (3-20 characters) and allowed characters (alphanumeric and underscores).
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in other parts of the application.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
  - `logout(session_token: str) -> bool`: Ends a user session.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session is valid.

**Usage:** Instantiate `UserAuth` to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: Used for hashing passwords.
- `json`: Used for JSON operations.
- `datetime`: Used for date and time operations.
- `timedelta`: Used for time calculations.
- `typing`: Used for type hinting.

---
*Auto-generated documentation - Last updated: 2025-07-18 06:04:58*
