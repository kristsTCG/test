# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. `validator.js`: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
   
2. `auth.py`: The Python file `auth.py` is responsible for handling the authentication process. It manages user login, registration, and authentication logic within the project.

## Usage
1. To utilize the validation functions provided in `validator.js`, import the file into your JavaScript code and call the necessary functions to validate user input data.

2. For user authentication functionalities such as login and registration, interact with the `auth.py` file in your Python code. Utilize the defined functions to authenticate users and manage user sessions securely.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username, allowing only alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on length and character requirements.

**Usage:** Import the `InputValidator` class from this file to use its validation methods in user authentication processes.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
  - `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Method to register a new user.
  - `login(username: str, password: str) -> Optional[str]`: Method to authenticate a user and return a session token.
  - `logout(session_token: str) -> bool`: Method to end a user session.
  - `is_authenticated(session_token: str) -> bool`: Method to check if a session is valid.

**Usage:** Instantiate `UserAuth` class to use the provided user authentication functionalities.

**Dependencies:**
- `hashlib`: For hashing functions.
- `json`: For JSON operations.
- `datetime`: For handling date and time.
- `timedelta`: For time-related calculations.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 19:32:18*
