# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user data meets the required criteria before authentication.
  
- **auth.py**: The Python file `auth.py` is responsible for handling user authentication processes. It manages user login, registration, and authentication using secure methods.

## Usage
To work with the code in this folder:
1. Utilize the functions in `validator.js` to validate user input data before authentication.
2. Use the functionalities provided in `auth.py` for user login, registration, and authentication processes.
3. Ensure to integrate these files with other parts of the project that require user authentication functionalities.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** This file can be imported into other JavaScript files using `require` or `import` statements, depending on the module system being used.

**Dependencies:** No external dependencies are required for this file.

## auth.py

**Purpose:**  
User authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user authentication.
  - `hash_password(password: str) -> str`: Hashes password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates user and returns session token.
  - `logout(session_token: str) -> bool`: Ends user session.
  - `is_authenticated(session_token: str) -> bool`: Checks if session is valid.

**Usage:**  
Instantiate `UserAuth` to manage user authentication, registration, login, logout, and session validation.

**Dependencies:**  
- `hashlib`: For hashing functions.
- `json`: For JSON serialization.
- `datetime`: For date and time operations.
- `timedelta`: For time duration calculations.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 22:03:28*
