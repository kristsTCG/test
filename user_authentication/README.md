# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This file contains functions for validating user input. It plays a crucial role in ensuring that user data meets the required criteria before processing.
  
- **auth.py**: The `auth.py` file is responsible for handling user authentication logic. It manages user login, registration, and authentication processes within the application.

## Usage
1. To utilize the validation functions provided in `validator.js`, import the file into your JavaScript code and call the necessary functions to validate user input.

2. For user authentication functionalities, import `auth.py` into your Python code. Utilize the functions within this file to manage user login, registration, and authentication processes.

3. Ensure that you understand the specific functions and methods available in each file to effectively implement user authentication features in your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the format of a password (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates the format of a username (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session based on the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication processes.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating expiration time for session tokens.
- `typing`: For type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-17 16:24:27*
