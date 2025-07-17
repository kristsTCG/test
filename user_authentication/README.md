# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files, `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- `validator.js`: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria before proceeding with authentication processes.
  
- `auth.py`: The Python file `auth.py` is responsible for handling user authentication logic. It manages user login, registration, and authentication processes within the project.

## Usage
To utilize the functionalities provided in this folder:
1. Review the `validator.js` file to understand the validation rules applied to user input.
2. Explore the `auth.py` file to understand how user authentication processes are implemented in the project.
3. Integrate these files into your project as needed for user authentication functionalities.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Assesses the strength of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class in your code and call the validation functions as needed.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, logout, and session validation.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
- `login(username: str, password: str) -> Optional[str]`: Authenticates a user and generates a session token for active sessions.
- `logout(session_token: str) -> bool`: Ends a user session by removing the session token from active sessions.
- `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and not expired.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:** `hashlib`, `json`, `datetime`, `timedelta`, `typing`

---
*Auto-generated documentation - Last updated: 2025-07-17 17:28:16*
