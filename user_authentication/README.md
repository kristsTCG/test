# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This functionality is responsible for validating user input and handling authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes validator.js for client-side input validation and auth.py for server-side authentication logic.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation logic for user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before submission.
  
- **auth.py**: The Python file `auth.py` is responsible for server-side authentication processes. It manages user authentication, login, and authorization within the application.

## Usage
1. **validator.js**:
   - To use the client-side validation logic, include `validator.js` in your HTML file using a script tag.
   - Call the validation functions provided in `validator.js` to validate user input fields before form submission.
  
2. **auth.py**:
   - Import `auth.py` into your Python project to leverage the authentication functionalities.
   - Utilize the functions defined in `auth.py` for user login, authentication, and authorization processes.

Ensure that you follow the guidelines and best practices defined in each file for secure and efficient user authentication within your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Determines the strength level of a password based on length and character types.

**Usage:** This file can be imported as a module to perform input validation for user authentication in a JavaScript application.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password()`: Method to hash a password using SHA-256.
- `register_user()`: Method to register a new user with a unique username, email, and password.
- `login()`: Method to authenticate a user with a username and password and generate a session token.
- `logout()`: Method to end a user session by invalidating the session token.
- `is_authenticated()`: Method to check if a session token is valid and active.

**Usage:** To use this file, instantiate the `UserAuth` class and call its methods for user registration, login, logout, and session validation.

**Dependencies:** 
- `hashlib` for password hashing.
- `json` for JSON serialization (not used in this file).
- `datetime` for handling date and time operations.
- `timedelta` for calculating time differences.
- `typing` for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 23:37:36*
