# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` written in JavaScript for input validation and `auth.py` written in Python for authentication logic.

## Key Files
- **validator.js**: This file contains functions to validate user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
- **auth.py**: The `auth.py` file is responsible for handling user authentication processes. It contains functions for user login, registration, and authentication checks.

## Usage
1. **validator.js**:
   - To use the validation functions in `validator.js`, import the file into your JavaScript code.
   - Call the appropriate validation functions with user input data to ensure it meets the required criteria.

2. **auth.py**:
   - Import `auth.py` into your Python code to access the authentication functions.
   - Utilize the functions provided in `auth.py` for user login, registration, and authentication checks within your application.

Ensure to follow the documentation within each file for specific function usage and parameters.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length and character requirements.
- `validateUsername(username)`: Validates a username for length and allowed characters.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character complexity.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
  - `logout(session_token: str) -> bool`: Ends a user session.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Instantiate `UserAuth` to utilize the user authentication functionalities provided by the class.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization.
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 03:41:55*
