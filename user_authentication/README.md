# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. `validator.js`: This JavaScript file is 1212 characters long and is responsible for validating user input data. It ensures that the data provided by users meets the required criteria before proceeding with authentication processes.

2. `auth.py`: This Python file, spanning 2198 characters, handles the authentication logic for users. It manages user login, registration, and authentication processes within the system.

## Usage
To utilize the functionalities provided in this folder:
- Use `validator.js` to validate user input data before authentication.
- Incorporate `auth.py` to implement user authentication processes such as login, registration, and authentication logic within the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates that a password meets specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates that a username is 3-20 characters long, alphanumeric, and allows underscores.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character requirements.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
  - `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and hashed password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token for active sessions.
  - `logout(session_token: str) -> bool`: Ends a user session by removing the session token from active sessions.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and active.

**Usage:** To use this file, create an instance of the `UserAuth` class and call its methods for user registration, login, session management, and authentication.

**Dependencies:** The file imports `hashlib`, `json`, `datetime`, `timedelta`, and `Optional` from `typing`.

---
*Auto-generated documentation - Last updated: 2025-07-18 07:26:55*
