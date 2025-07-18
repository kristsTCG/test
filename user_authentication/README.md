# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It includes scripts for validating user input and handling authentication logic.

## Structure
The folder is organized to handle user authentication processes efficiently. It contains two key files: `validator.js` for client-side input validation in JavaScript and `auth.py` for server-side authentication logic in Python.

## Key Files
1. `validator.js`: This JavaScript file is crucial for validating user input on the client-side. It ensures that user-provided data meets the required criteria before submission.
   
2. `auth.py`: The Python script `auth.py` plays a significant role in managing user authentication on the server-side. It handles user login, registration, and authentication processes securely.

## Usage
1. To utilize the client-side input validation, refer to `validator.js` in your front-end code. You can customize the validation rules to suit your project requirements.

2. For server-side authentication functionalities, interact with `auth.py` in your back-end code. Implement the provided authentication logic to secure user access and manage user accounts effectively.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Determines the strength level of a password based on length and character types.

**Usage:** This file can be imported and used in other JavaScript files by requiring it as `const InputValidator = require('./validator.js');`.

**Dependencies:** No external dependencies are required for this file.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password, generating a session token.
- `logout`: Method to end a user's session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations. Call methods like `register_user`, `login`, `logout`, and `is_authenticated` as needed.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-18 02:01:41*
