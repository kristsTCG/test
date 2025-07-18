# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It handles tasks such as validating user input and managing user authentication using JavaScript and Python.

## Structure
The folder is organized to encapsulate all user authentication logic. It contains two key files: `validator.js` for client-side validation in JavaScript and `auth.py` for server-side authentication in Python.

## Key Files
- `validator.js`: This JavaScript file contains client-side validation logic for user input. It ensures that user-provided data meets specified criteria before submission.
- `auth.py`: The Python file `auth.py` is responsible for server-side authentication processes. It manages user authentication, login, and authorization within the system.

## Usage
1. To utilize the client-side validation functionality, refer to `validator.js`. Modify the validation rules as needed to suit the project requirements.
2. For server-side authentication tasks, interact with `auth.py`. Implement additional authentication logic or integrate it with existing authentication systems as necessary.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates password complexity requirements (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates username format (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class in your code and call the validation functions as needed.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash passwords using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 06:56:50*
