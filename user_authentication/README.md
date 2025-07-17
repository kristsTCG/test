# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes a JavaScript file for validation (`validator.js`) and a Python file for authentication (`auth.py`).

## Key Files
- **validator.js**: This JavaScript file contains functions for validating user input, ensuring data integrity and security.
- **auth.py**: The Python file `auth.py` is responsible for handling user authentication processes, such as login, registration, and session management.

## Usage
To utilize the functionality within this folder:
1. Use the functions defined in `validator.js` to validate user input before processing it further.
2. Incorporate the authentication logic from `auth.py` to manage user login, registration, and session handling in the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3 to 20 characters long, alphanumeric, and underscores only.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No notable dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
  - `hash_password(password: str) -> str`: Hashes the input password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user with a username and password, returning a session token if successful.
  - `logout(session_token: str) -> bool`: Ends a user session using the provided session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: Used for hashing passwords.
- `json`: Not used in the provided code but imported.
- `datetime`: Used for handling date and time operations.
- `timedelta`: Used for defining time intervals.
- `typing`: Used for type hinting.

---
*Auto-generated documentation - Last updated: 2025-07-17 14:01:25*
