# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It handles validation of user input and authentication processes.

## Structure
The folder is organized to separate the validation logic in `validator.js` written in JavaScript and the authentication logic in `auth.py` written in Python.

## Key Files
- **validator.js**: This file contains the validation logic for user input. It ensures that user-provided data meets the required criteria before proceeding with authentication processes.
  
- **auth.py**: The `auth.py` file is responsible for handling user authentication. It manages user login, registration, and authentication processes within the system.

## Usage
1. **validator.js**: To use the validation logic provided in `validator.js`, import the file in your JavaScript code and utilize the functions defined within it to validate user input before authentication.

2. **auth.py**: Import `auth.py` in your Python code to access the authentication functionalities. Use the methods defined in this file to handle user registration, login, and authentication processes within your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3 to 20 characters long, containing only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the provided validation methods in your authentication logic.

**Dependencies:** None

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
  - `logout(session_token: str) -> bool`: Ends a user session based on the session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization and deserialization.
- `datetime`: For working with date and time objects.
- `timedelta`: For representing a duration of time.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 02:11:39*
