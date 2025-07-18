# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This JavaScript file contains 1212 characters and is responsible for validating user input data. It ensures that user data meets the required criteria before proceeding with authentication processes.
  
- **auth.py**: This Python file consists of 2198 characters and handles the authentication logic for users. It verifies user credentials and grants access based on the authentication process.

## Usage
To utilize the user authentication functionalities in this folder:
1. Review the `validator.js` file to understand the validation criteria for user input data.
2. Explore the `auth.py` file to comprehend the authentication logic and processes.
3. Integrate these files into your project to implement user authentication features effectively.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates that a password meets complexity requirements (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates that a username is 3-20 characters long, alphanumeric, and contains underscores only.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** This file can be imported as a module in other JavaScript files using `require` or ES6 `import` statements.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password()`: Method to hash a password using SHA-256.
- `register_user()`: Registers a new user with a unique username, email, and hashed password.
- `login()`: Authenticates a user with a username and password, generates a session token, and tracks the last login time.
- `logout()`: Ends a user session by removing the session token from active sessions.
- `is_authenticated()`: Checks if a session token is valid and has not expired.

**Usage:** Instantiate `UserAuth` to use the provided authentication functionalities.

**Dependencies:**
- `hashlib`: Used for hashing passwords.
- `json`: Not used in this file but imported.
- `datetime`: Used for handling dates and times.
- `timedelta`: Used for calculating session expiration time.
- `typing`: Used for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 04:45:07*
