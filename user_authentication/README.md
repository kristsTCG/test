# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. These files handle user validation and authentication processes.

## Structure
The folder is organized to separate the validation logic in `validator.js` written in JavaScript and the authentication logic in `auth.py` written in Python.

## Key Files
- `validator.js`: This file contains the user validation logic, ensuring that user input meets specified criteria before proceeding with authentication.
- `auth.py`: This file handles the authentication process, verifying user credentials and granting access based on the authentication rules.

## Usage
1. To work with the user validation logic, refer to `validator.js` and customize the validation criteria as needed.
2. For authentication processes, utilize `auth.py` to integrate user authentication into the project flow.
3. Ensure that both files are properly integrated and called within the project to enable secure user authentication.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates an email address using a regular expression.
- `validatePassword(password)`: Validates a password based on specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates a username for length (3-20 characters) and allowed characters (alphanumeric and underscores).
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your application.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints in function definitions.

---
*Auto-generated documentation - Last updated: 2025-07-17 19:07:54*
