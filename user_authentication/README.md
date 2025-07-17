# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It includes a JavaScript file for validation and a Python file for authentication.

## Structure
The folder is organized to handle user authentication tasks. The `validator.js` file handles input validation, while the `auth.py` file manages user authentication processes.

## Key Files
- **validator.js**: This JavaScript file contains functions for validating user inputs. It plays a crucial role in ensuring data integrity and security.
- **auth.py**: The Python file `auth.py` is responsible for handling user authentication tasks such as login, logout, and user session management.

## Usage
1. To utilize the validation functions in `validator.js`, import the necessary functions into your JavaScript files using `import { functionName } from './validator.js'`.
2. In Python scripts that require user authentication functionalities, import `auth.py` using `import auth`.
3. Use the functions provided in `validator.js` for input validation and the functions in `auth.py` for user authentication processes within your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the format of a password (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates the format of a username (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the provided validation methods.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session based on the session token.
- `is_authenticated`: Method to check if a session token is valid and the user is authenticated.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations like registration, login, session handling, and authentication.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 15:21:34*
