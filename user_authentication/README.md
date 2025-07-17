# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities in the project. It includes validation logic in JavaScript and authentication logic in Python.

## Structure
The folder is organized to handle user authentication tasks. It contains two key files: `validator.js` for input validation and `auth.py` for user authentication.

## Key Files
- **validator.js**: This JavaScript file contains logic for validating user inputs. It plays a crucial role in ensuring that user-provided data meets the required criteria before proceeding with authentication.
- **auth.py**: The Python file `auth.py` handles user authentication processes. It manages user login, registration, and authentication tasks within the project.

## Usage
1. **validator.js**:
   - Ensure that the `validator.js` file is included in the appropriate parts of your project where input validation is required.
   - Use the functions provided in `validator.js` to validate user inputs such as email addresses, passwords, or other relevant data.

2. **auth.py**:
   - Import the `auth.py` module in your Python project to utilize the authentication functionalities.
   - Implement the provided functions in `auth.py` to handle user registration, login, and authentication processes.

Ensure that both files are integrated correctly within your project to maintain secure and efficient user authentication mechanisms.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Returns the strength level of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class where input validation is needed.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and hashed password.
- `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token if successful.
- `logout(session_token: str) -> bool`: Ends a user session based on the provided session token.
- `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and the user is authenticated.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations. Call methods like `register_user`, `login`, `logout`, and `is_authenticated` as needed.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization and deserialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 21:21:40*
