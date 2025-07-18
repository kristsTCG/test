# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities within the project. It handles tasks such as validating user input and managing user authentication using JavaScript and Python.

## Structure
The folder is organized to separate the validation logic in `validator.js` written in JavaScript and the authentication functionality in `auth.py` written in Python.

## Key Files
1. **validator.js**: This file contains the validation logic for user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before proceeding with authentication processes.

2. **auth.py**: The `auth.py` file is responsible for handling user authentication using Python. It manages user login, registration, and authentication processes within the project.

## Usage
1. **validator.js**:
   - To use the validation logic provided in `validator.js`, import the necessary functions into your JavaScript files.
   - Call the appropriate validation functions on user input data to ensure it meets the required criteria before proceeding with authentication processes.

2. **auth.py**:
   - Utilize the functions and classes defined in `auth.py` to handle user authentication tasks in your Python code.
   - Implement user login, registration, and authentication functionalities by calling the relevant methods provided in `auth.py`.

Ensure to follow the documentation and code comments within each file for a better understanding of the implementation details and usage instructions.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric and underscore characters.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on various criteria.

**Usage:** This file can be imported into other JavaScript files using `require` or `import` statements.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations. Call the methods within the class to register users, authenticate logins, manage sessions, and check authentication status.

**Dependencies:** 
- `hashlib` for password hashing.
- `json` for JSON serialization (not used in this file).
- `datetime` for date and time operations.
- `timedelta` for time duration calculations.
- `typing` for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 09:04:32*
