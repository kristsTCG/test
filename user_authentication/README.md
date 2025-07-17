# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities within the project. It includes validation logic in JavaScript and authentication logic in Python.

## Structure
The folder is organized to handle user authentication tasks. The key components include a JavaScript file for validation and a Python file for authentication.

## Key Files
- `validator.js`: This JavaScript file contains validation logic for user inputs. It plays a crucial role in ensuring that user-provided data meets the required criteria.
- `auth.py`: The Python file `auth.py` is responsible for handling user authentication processes. It manages user login, registration, and authentication tasks.

## Usage
To utilize the code in this folder:
1. Use the functions defined in `validator.js` to validate user inputs before processing them.
2. Import and utilize the functions in `auth.py` to handle user authentication tasks such as login and registration.

Ensure that you understand the functions and methods provided in each file to effectively implement user authentication features in the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, username validation, and password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** This file can be imported as a module in other JavaScript files to perform input validation for user authentication.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
  - `logout(session_token: str) -> bool`: Ends a user session based on the provided session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: for hashing passwords using SHA-256.
- `json`: for JSON serialization and deserialization.
- `datetime`: for working with dates and times.
- `timedelta`: for calculating time differences.
- `typing`: for type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 14:38:34*
