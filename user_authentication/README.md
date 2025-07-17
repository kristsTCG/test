# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This JavaScript file contains code for validating user input and ensuring data integrity during the authentication process. It plays a crucial role in verifying user credentials.
  
- **auth.py**: The Python file `auth.py` is responsible for handling user authentication logic. It manages user login, registration, and session management within the application.

## Usage
1. To utilize the functionalities provided by the `validator.js` file, import it into your JavaScript files using `import validator from './validator.js'`.
   
2. Use the functions defined in `validator.js` to validate user input data before processing it further in the authentication flow.

3. In Python scripts or modules where user authentication is required, import `auth.py` using `import auth`.

4. Utilize the functions and classes defined in `auth.py` to implement user authentication features such as user login, registration, and session handling in your application.

Ensure to follow the documentation and comments within the files for a better understanding of the code structure and usage.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates if the input username meets specific criteria (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and hashed password.
- `login(username: str, password: str) -> Optional[str]`: Authenticates a user with a username and password, generates a session token, and stores the session information.
- `logout(session_token: str) -> bool`: Ends a user session by removing the session token from active sessions.
- `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and not expired.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations. Call the methods to register users, login, logout, and check authentication status.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating expiration time for session tokens.
- `typing.Optional`, `typing.Dict`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 15:06:20*
