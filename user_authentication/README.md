# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user inputs and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript for client-side validation and `auth.py` written in Python for server-side authentication.

## Key Files
1. **validator.js**: This file is responsible for client-side validation of user inputs. It contains functions to validate user data before submitting it to the server.
   
2. **auth.py**: The `auth.py` file handles server-side authentication processes. It includes functions for user login, registration, and authentication checks.

## Usage
1. **validator.js**: To use the client-side validation functionality, include `validator.js` in your HTML file using a script tag. You can then call the validation functions provided within this file to validate user inputs before form submission.

2. **auth.py**: For server-side authentication tasks, import `auth.py` into your Python project. You can then utilize the functions within this file to handle user authentication processes such as login, registration, and authentication checks.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength evaluation.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username, allowing alphanumeric characters and underscores only.
- `getPasswordStrength(password)`: Evaluates the strength of a password based on length and character complexity.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, logout, and session authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in the provided code snippet).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints (not used in the provided code snippet).

---
*Auto-generated documentation - Last updated: 2025-07-18 02:39:52*
