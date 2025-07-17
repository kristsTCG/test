# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files, `validator.js` for client-side validation written in JavaScript and `auth.py` for server-side authentication written in Python.

## Key Files
1. `validator.js`: This file contains client-side validation logic for user input. It ensures that user-provided data meets the required criteria before submitting it to the server.
   
2. `auth.py`: The `auth.py` file handles server-side authentication processes. It manages user authentication, login, and logout functionalities using Python.

## Usage
1. To utilize the client-side validation provided by `validator.js`, include the script in your HTML file using `<script src="path/to/validator.js"></script>`. Then, call the validation functions as needed in your frontend code.

2. For server-side authentication using `auth.py`, import the necessary functions or classes into your Python project. Use the provided authentication methods to secure user access and manage user sessions effectively.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates if a password meets specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates if a username meets specific criteria (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Determines the strength level of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user session.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** To use this file, create an instance of `UserAuth` and call its methods for user registration, login, logout, and session validation.

**Dependencies:** 
- `hashlib` for hashing functions.
- `json` for JSON serialization.
- `datetime` for date and time operations.
- `timedelta` for time duration calculations.
- `typing` for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 19:24:49*
