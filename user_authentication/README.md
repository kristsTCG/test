# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. **validator.js**
   - Language: JavaScript
   - Size: 1212 characters
   - Role: Responsible for validating user input data for authentication purposes.

2. **auth.py**
   - Language: Python
   - Size: 2198 characters
   - Role: Manages the authentication process for users, including login, registration, and access control.

## Usage
1. **validator.js**
   - To utilize the `validator.js` file, import it into your JavaScript files using `import validator from './validator.js';`.
   - Use the provided validation functions to validate user input data before processing it for authentication.

2. **auth.py**
   - To use `auth.py`, import it into your Python files using `import auth`.
   - Utilize the functions within `auth.py` to handle user authentication tasks such as user login, registration, and managing user access permissions.

Ensure that you follow the defined structure and utilize the functions provided in these files for seamless user authentication within your project.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication. It provides methods to validate email addresses, passwords, and usernames, as well as determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is between 3 to 20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of the input password based on length and character types.

**Usage:** This file can be imported into other JavaScript files using `require` or `import` statements, depending on the project setup.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file provides a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
  - `logout(session_token: str) -> bool`: Ends a user session based on the provided session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to use the provided user authentication functionalities.

**Dependencies:**
- `hashlib`: for hashing passwords using SHA-256.
- `json`: for handling JSON data.
- `datetime`: for working with dates and times.
- `timedelta`: for calculating time differences.
- `typing`: for type hints in function definitions.

---
*Auto-generated documentation - Last updated: 2025-07-17 15:21:12*
