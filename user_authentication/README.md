# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` written in JavaScript for input validation and `auth.py` written in Python for authentication logic.

## Key Files
- **validator.js**: This file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria before proceeding with authentication processes.
  
- **auth.py**: The `auth.py` file is responsible for handling user authentication logic. It manages user login, registration, and authentication processes within the system.

## Usage
1. To utilize the input validation functionality, refer to the `validator.js` file. Modify or extend the validation rules as needed to suit the project requirements.
   
2. For user authentication tasks such as login and registration, interact with the `auth.py` file. Implement the necessary authentication processes based on the project specifications.

3. Ensure to maintain the integrity and security of user authentication data by following best practices and security guidelines while working with the code in this folder.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** User authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Register a new user with username, email, and password.
- `login(username: str, password: str) -> Optional[str]`: Authenticate user and return session token.
- `logout(session_token: str) -> bool`: End user session.
- `is_authenticated(session_token: str) -> bool`: Check if session token is valid.

**Usage:** Import `auth.py` and create an instance of `UserAuth` to perform user registration, login, logout, and session validation.

**Dependencies:** `hashlib`, `json`, `datetime`, `timedelta`, `typing`.

---
*Auto-generated documentation - Last updated: 2025-07-17 18:02:54*
