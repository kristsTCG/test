# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. **validator.js**: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
   
2. **auth.py**: The Python file `auth.py` is responsible for handling user authentication processes. It includes functions for user login, registration, and authentication logic.

## Usage
To utilize the functionalities provided in this folder:
1. Review the `validator.js` file to understand the validation rules and functions available for user input.
2. Explore the `auth.py` file to implement user authentication processes such as login, registration, and authentication logic.
3. Ensure to integrate these files into the project's authentication system as needed.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of the input password based on length and character types.

**Usage:** This file can be imported into other JavaScript files using `require` or `import` statements to utilize the input validation functions provided.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** User authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Register a new user with username, email, and password.
- `login(username: str, password: str) -> Optional[str]`: Authenticate user and return session token.
- `logout(session_token: str) -> bool`: End user session.
- `is_authenticated(session_token: str) -> bool`: Check if session token is valid.

**Usage:** Instantiate `UserAuth` class to perform user registration, login, logout, and session validation.

**Dependencies:**
- `hashlib`: For hashing functions.
- `json`: For JSON serialization/deserialization.
- `datetime`: For date and time operations.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 23:20:59*
