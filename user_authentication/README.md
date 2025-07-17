# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- `validator.js`: This file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
- `auth.py`: This Python file handles the authentication process for users. It manages user login, registration, and authentication logic.

## Usage
1. To utilize the validation functions in `validator.js`, import the necessary functions into your JavaScript files and call them as needed to validate user input data.
2. For user authentication tasks, import `auth.py` into your Python scripts. Use the provided functions to handle user login, registration, and authentication processes within your application.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3 to 20 characters, alphanumeric, and underscores only.
- `getPasswordStrength(password)`: Calculates the strength level of a given password based on length and character types.

**Usage:** To use this file, import `InputValidator` class in your code and call the respective validation methods as needed.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user's session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations like registration, login, and session handling.

**Dependencies:**
- `hashlib`: Used for hashing passwords.
- `json`: Not used in the provided code but imported.
- `datetime`: Used for date and time operations.
- `timedelta`: Used for calculating session expiration time.
- `typing`: Used for type hinting.

---
*Auto-generated documentation - Last updated: 2025-07-17 19:13:00*
