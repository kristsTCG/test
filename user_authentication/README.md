# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` for client-side input validation written in JavaScript and `auth.py` for server-side authentication logic written in Python.

## Key Files
1. **validator.js**: This file is crucial for validating user input on the client-side. It contains functions to ensure that user-provided data meets specified criteria before submission.
   
2. **auth.py**: This file handles server-side authentication processes. It includes functions for user login, registration, and session management. The authentication logic is implemented in Python to ensure secure user authentication.

## Usage
1. To utilize the client-side input validation provided by `validator.js`, include the necessary script in your HTML file and call the validation functions as needed.
   
2. For server-side authentication tasks, import and use the functions defined in `auth.py` within your Python application. Ensure that proper authentication checks are in place to secure user data and access to the system.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates if the provided email address is in a valid format.
- `validatePassword(password)`: Validates if the provided password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the provided username is 3-20 characters long and consists of alphanumeric characters and underscores only.
- `getPasswordStrength(password)`: Determines the strength of the provided password based on length and character types.

**Usage:** This file can be imported using `require` or `import` statements to access the `InputValidator` class and its validation methods.

**Dependencies:** No external dependencies are required for this file.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user session.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 19:20:41*
