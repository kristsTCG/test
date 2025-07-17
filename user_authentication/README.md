# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` for client-side input validation in JavaScript and `auth.py` for server-side authentication logic in Python.

## Key Files
- **validator.js**: This file contains client-side validation functions to ensure that user input meets specified criteria before submission.
- **auth.py**: The `auth.py` file is responsible for server-side authentication processes, such as verifying user credentials and managing user sessions.

## Usage
1. **validator.js**:
   - To use the validation functions in `validator.js`, include the file in your HTML document using a script tag.
   - Call the validation functions as needed within your client-side JavaScript code to validate user input.

2. **auth.py**:
   - Import the `auth.py` file in your Python project to access the authentication functionalities.
   - Utilize the functions provided in `auth.py` to authenticate users, handle login/logout processes, and manage user sessions.

Ensure that proper error handling and security measures are implemented when working with user authentication functionalities in this folder.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric and underscore characters.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on various criteria.

**Usage:** This file can be imported as a module in other JavaScript files to perform input validation tasks.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user registration, login, session handling, and authentication.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
- `login(username: str, password: str) -> Optional[str]`: Authenticates a user and generates a session token for active sessions.
- `logout(session_token: str) -> bool`: Ends a user session by removing the session token from active sessions.
- `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and active.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your application.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating expiration time for session tokens.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 14:02:34*
