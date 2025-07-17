# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It consists of two key files, `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
  
- **auth.py**: The Python file `auth.py` is responsible for handling user authentication processes. It manages user login, registration, and authentication logic within the project.

## Usage
1. To utilize the validation functions provided in `validator.js`, import the file into your JavaScript code using `import validator from './validator.js'`. You can then call the validation functions as needed to validate user input data.

2. In Python scripts that require user authentication functionalities, import the `auth.py` module using `import auth`. You can then access the authentication methods defined in the file to manage user authentication processes within your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email follows the standard email format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long, alphanumeric, and allows underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication process.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
    - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
    - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
    - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
    - `logout(session_token: str) -> bool`: Ends a user session based on the provided session token.
    - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: Used for hashing passwords.
- `json`: Used for JSON serialization and deserialization.
- `datetime`: Used for working with dates and times.
- `timedelta`: Used for representing a duration of time.
- `typing`: Used for type hints in function definitions.

---
*Auto-generated documentation - Last updated: 2025-07-17 15:43:45*
