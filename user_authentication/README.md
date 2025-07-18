# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes validator.js for client-side input validation and auth.py for server-side authentication logic.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation functions to ensure that user input meets specified criteria before submission.
- **auth.py**: This Python file handles server-side authentication processes, such as verifying user credentials and managing user sessions.

## Usage
1. **validator.js**:
   - Import the validator.js file into your HTML document using `<script src="path/to/validator.js"></script>`.
   - Utilize the validation functions provided in validator.js to validate user input fields before form submission.

2. **auth.py**:
   - Import the auth.py file into your Python project using `import auth`.
   - Implement the authentication logic provided in auth.py to authenticate users, manage user sessions, and handle login/logout functionalities.

Ensure to customize the validation criteria and authentication processes according to your project requirements.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates an email address using a regular expression.
- `validatePassword(password)`: Validates a password based on specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates a username based on length and character restrictions.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use its validation methods in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user's session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your Python application.

**Dependencies:**
- `hashlib`: Used for hashing passwords.
- `json`: Used for JSON serialization (not used in the provided code).
- `datetime`: Used for working with dates and times.
- `timedelta`: Used for calculating time differences.
- `typing`: Used for type hints (not used in the provided code).

---
*Auto-generated documentation - Last updated: 2025-07-18 02:49:36*
