# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files, `validator.js` written in JavaScript for input validation and `auth.py` written in Python for handling user authentication.

## Key Files
1. `validator.js`: This JavaScript file contains functions for validating user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before proceeding with authentication processes.

2. `auth.py`: The Python file `auth.py` is responsible for managing user authentication within the project. It handles tasks such as user login, registration, and authentication verification.

## Usage
To utilize the functionalities provided in this folder, follow these steps:
1. Use the functions defined in `validator.js` to validate user input before processing it further.
2. Incorporate the authentication logic from `auth.py` to handle user login, registration, and authentication verification within the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Determines the strength level of a password based on length and character types.

**Usage:** This file can be imported into other JavaScript files using `require` or `import` statements to access the input validation functionalities provided by the `InputValidator` class.

**Dependencies:** This file does not have any external dependencies and can be used independently for input validation tasks related to user authentication.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** To use this file, create an instance of `UserAuth` and call its methods for user registration, login, logout, and session validation.

**Dependencies:** This file imports `hashlib`, `json`, `datetime`, `timedelta`, and `Optional` from `typing`.

---
*Auto-generated documentation - Last updated: 2025-07-17 22:39:24*
