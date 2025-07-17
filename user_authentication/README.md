# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This module is responsible for validating user input and handling authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes the following key components:
- `validator.js`: A JavaScript file containing functions for validating user input data.
- `auth.py`: A Python file that manages user authentication processes such as login, registration, and password management.

## Key Files
### validator.js
- **Role**: Responsible for validating user input data to ensure it meets the required criteria.
- **Character Count**: 1212 characters

### auth.py
- **Role**: Manages user authentication functionalities such as login, registration, and password management.
- **Character Count**: 2198 characters

## Usage
1. **validator.js**:
   - Import the `validator.js` file into your JavaScript code.
   - Utilize the functions provided in `validator.js` to validate user input data before processing.

2. **auth.py**:
   - Import the `auth.py` module into your Python code.
   - Use the functions within `auth.py` to handle user authentication processes like login, registration, and password management.

Ensure to follow the documentation within each file for specific usage instructions and function details.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates if the input username meets specific criteria (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
- `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
- `logout(session_token: str) -> bool`: Ends a user session based on the session token.
- `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** This file can be imported into other Python scripts to handle user authentication tasks.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization and deserialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hinting in function definitions.

---
*Auto-generated documentation - Last updated: 2025-07-17 20:13:25*
