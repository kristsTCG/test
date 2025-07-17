# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` for client-side input validation in JavaScript and `auth.py` for server-side authentication logic in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic written in JavaScript. It ensures that user input meets specified criteria before submission.
- **auth.py**: The `auth.py` file contains server-side authentication logic written in Python. It handles user authentication processes such as login, registration, and session management.

## Usage
1. **validator.js**:
   - Modify the validation criteria as needed by updating the functions in this file.
   - Include `validator.js` in your HTML files using `<script src="path/to/validator.js"></script>`.

2. **auth.py**:
   - Implement additional authentication features by extending the existing logic in this file.
   - Integrate `auth.py` with your backend application to handle user authentication processes effectively.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric and underscore characters.
- `getPasswordStrength(password)`: Determines the strength of a password and returns a descriptive level.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication operations.
  - `hash_password(password: str) -> str`: Hashes the password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates the user with the provided username and password, returning a session token if successful.
  - `logout(session_token: str) -> bool`: Ends the user session associated with the provided session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if the session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: Used for hashing passwords.
- `json`: Used for JSON serialization and deserialization.
- `datetime`: Used for working with dates and times.
- `timedelta`: Used for representing a duration of time.
- `typing`: Used for type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 21:03:22*
