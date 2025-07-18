# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes validator.js for client-side input validation and auth.py for server-side authentication logic.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation functions to ensure that user input meets specified criteria before submitting to the server.
- **auth.py**: This Python file handles server-side authentication processes, such as verifying user credentials and generating access tokens.

## Usage
1. **validator.js**:
   - Modify the validation functions as needed to enforce specific input requirements.
   - Include the script in your HTML files using `<script src="path/to/validator.js"></script>`.

2. **auth.py**:
   - Customize the authentication logic to integrate with your user database or authentication service.
   - Import and use the functions in your server-side code to authenticate users securely.

Ensure that both client-side and server-side authentication processes are in sync to provide a seamless user experience and maintain security standards.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of the input password based on length and character types.

**Usage:** This file can be imported using `require` or `import` statements to access the input validation functions.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, logout, and session authentication.
    - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
    - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
    - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
    - `logout(session_token: str) -> bool`: Ends a user session based on the session token.
    - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your Python application.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints in function definitions.

---
*Auto-generated documentation - Last updated: 2025-07-18 06:44:28*
