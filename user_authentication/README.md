# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` for client-side input validation in JavaScript and `auth.py` for server-side authentication logic in Python.

## Key Files
1. `validator.js`: This file contains client-side validation logic written in JavaScript. It plays a crucial role in ensuring that user input meets the required criteria before submission.
   
2. `auth.py`: The `auth.py` file contains server-side authentication logic implemented in Python. It manages user authentication processes, such as login, registration, and password handling.

## Usage
To work with the code in this folder:
- Use `validator.js` for client-side input validation by including it in your front-end scripts.
- Utilize `auth.py` for server-side authentication tasks by importing and integrating it into your backend logic.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email matches the standard email format.
- `validatePassword(password)`: Validates if the password meets the criteria of being at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the username is 3-20 characters long, alphanumeric, and allows underscores.
- `getPasswordStrength(password)`: Calculates and returns the strength level of a given password based on length and character types.

**Usage:** This file can be imported as a module to perform input validation tasks related to user authentication.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Import the `UserAuth` class from this file to handle user authentication operations in your Python application.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 03:09:15*
