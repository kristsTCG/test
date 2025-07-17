# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication logic.

## Structure
The folder consists of two key files:
- `validator.js`: A JavaScript file containing functions for validating user input.
- `auth.py`: A Python file responsible for handling user authentication processes.

## Key Files
### validator.js
- Role: This file contains functions to validate user input data, ensuring it meets the required criteria before processing.
- Size: 1212 characters

### auth.py
- Role: This Python file manages user authentication processes, such as login, registration, and password management.
- Size: 2198 characters

## Usage
1. To utilize the validation functions in `validator.js`, import the necessary functions into your JavaScript files and call them as needed to validate user input.
2. For user authentication processes, interact with the functions defined in `auth.py` by importing and using them within your Python codebase. This includes handling user login, registration, and password-related operations.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters, alphanumeric, and underscores only.
- `getPasswordStrength(password)`: Determines the strength of the input password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token if successful.
  - `logout(session_token: str) -> bool`: Ends a user session based on the session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: Used for hashing passwords.
- `json`: Not used in the provided code but imported.
- `datetime`: Used for working with dates and times.
- `timedelta`: Used for time-based calculations.
- `typing`: Used for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 14:08:59*
