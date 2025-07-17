# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. **validator.js**: This file contains client-side validation logic for user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before submission.
   
2. **auth.py**: This Python file handles server-side authentication processes. It is responsible for verifying user credentials, generating tokens, and managing user sessions.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to match the project's requirements.
   - Include the script in your HTML files using `<script src="path/to/validator.js"></script>`.

2. **auth.py**:
   - Implement additional authentication methods or customize the existing logic to suit the project's security needs.
   - Integrate the authentication functionality into your project by importing and using the necessary functions from `auth.py`.

Ensure that both client-side and server-side authentication processes are in sync to provide a secure and seamless user experience.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates that a password meets specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates that a username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on its length and character composition.

**Usage:** This file can be imported into other JavaScript files using `require` or `import` statements to perform input validation for user authentication.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, logout, and session validation.
- `hash_password`: Method to hash passwords using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Import `auth.py` and create an instance of `UserAuth` to utilize the user authentication functionalities.

**Dependencies:**
- `hashlib`: Used for hashing passwords.
- `json`: Not used in the provided code but imported.
- `datetime`: Used for handling date and time operations.
- `timedelta`: Used for calculating expiration time for session tokens.
- `typing`: Used for type hints in function definitions.

---
*Auto-generated documentation - Last updated: 2025-07-17 16:22:18*
