# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It handles tasks such as validating user input and managing user authentication using JavaScript and Python.

## Structure
The folder is organized to separate the validation logic (in `validator.js`) written in JavaScript and the authentication logic (in `auth.py`) written in Python.

## Key Files
- **validator.js**: This file contains the validation logic for user input. It ensures that the data provided by users meets the required criteria before proceeding with authentication.
- **auth.py**: The `auth.py` file is responsible for handling user authentication processes. It manages user login, registration, and authentication using Python.

## Usage
1. **validator.js**:
   - To use the validation functions in `validator.js`, import the necessary functions into your JavaScript files.
   - Call the appropriate validation functions on user input data to ensure it meets the required criteria.

2. **auth.py**:
   - Import the `auth.py` module into your Python scripts to access the authentication functionalities.
   - Use the provided functions in `auth.py` to handle user registration, login, and authentication processes within your project.

Ensure that you follow the documentation within each file to understand the specific functions and methods available for user authentication in your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username allowing alphanumeric characters and underscores only.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the provided validation methods in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token if successful.
  - `logout(session_token: str) -> bool`: Ends a user session based on the provided session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization and deserialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hinting in function signatures.

---
*Auto-generated documentation - Last updated: 2025-07-17 20:51:02*
