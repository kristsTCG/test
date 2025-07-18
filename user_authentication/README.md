# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. It handles tasks such as validating user input and managing user authentication using JavaScript and Python.

## Structure
The folder is organized to separate the validation logic in `validator.js` (JavaScript) and the authentication logic in `auth.py` (Python). Each file serves a specific purpose in the user authentication process.

## Key Files
- `validator.js`: This JavaScript file contains the validation logic for user input. It ensures that user-provided data meets specified criteria before proceeding with authentication processes.
- `auth.py`: The Python file `auth.py` manages user authentication within the project. It handles tasks such as user login, registration, and authentication verification.

## Usage
1. To utilize the validation functionality, refer to `validator.js`. This file contains functions to validate user input data before proceeding with authentication processes.
2. For user authentication tasks such as login, registration, and verification, interact with `auth.py`. This file provides the necessary functions to manage user authentication within the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username allowing only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character complexity.

**Usage:** Import `InputValidator` class from this file to use the provided input validation functions in your authentication logic.

**Dependencies:** No external dependencies required for this file.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the provided user authentication functionalities.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 03:10:52*
