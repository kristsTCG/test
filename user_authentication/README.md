# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It is responsible for validating user input and handling authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` for client-side validation using JavaScript and `auth.py` for server-side authentication using Python.

## Key Files
- **validator.js**: This file contains client-side validation logic written in JavaScript. It ensures that user input meets the required criteria before submitting it for authentication.
  
- **auth.py**: The `auth.py` file is responsible for server-side authentication using Python. It handles user login, registration, and authentication processes securely on the server side.

## Usage
1. **validator.js**:
   - Modify the validation rules in `validator.js` to suit the project's specific requirements.
   - Include `validator.js` in your HTML files using `<script src="path/to/validator.js"></script>`.

2. **auth.py**:
   - Import `auth.py` in your Python project to utilize the authentication functionalities.
   - Implement the necessary API endpoints for user registration, login, and authentication based on the functions provided in `auth.py`.

Ensure that both client-side and server-side authentication processes are in sync to provide a seamless user experience.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
- `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token if successful.
- `logout(session_token: str) -> bool`: Ends a user session based on the provided session token.
- `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and the user is authenticated.

**Usage:** Instantiate `UserAuth` to use the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib` for hashing functions.
- `json` for JSON serialization and deserialization.
- `datetime` for working with dates and times.
- `timedelta` from `datetime` for calculating time differences.
- `typing.Optional` for type hinting.

---
*Auto-generated documentation - Last updated: 2025-07-18 08:15:07*
