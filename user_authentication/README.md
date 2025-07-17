# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. These files handle user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. `validator.js`: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
   
2. `auth.py`: The Python file `auth.py` is responsible for handling user authentication processes. It manages user login, registration, and authentication tasks within the system.

## Usage
To work with the code in this folder:
- Review `validator.js` to understand the validation logic and criteria for user input data.
- Explore `auth.py` to familiarize yourself with the user authentication processes implemented in Python.
- Integrate these files into the project's authentication system as needed, ensuring proper validation and authentication of user data.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters long and consists of alphanumeric characters and underscores only.
- `getPasswordStrength(password)`: Determines the strength of the input password based on length and character types.

**Usage:** This file can be imported in other JavaScript files using `require` or `import` statements to access the input validation functions.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Register a new user with a unique username.
- `login(username: str, password: str) -> Optional[str]`: Authenticate a user and return a session token.
- `logout(session_token: str) -> bool`: End a user session by removing the session token.
- `is_authenticated(session_token: str) -> bool`: Check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations like registration, login, logout, and session validation.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For managing dates and times.
- `timedelta`: For calculating expiration time for session tokens.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 14:37:19*
