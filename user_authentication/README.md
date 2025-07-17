# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. `validator.js`: This JavaScript file contains code for validating user input. It plays a crucial role in ensuring that user data meets specified criteria before proceeding with authentication processes.
   
2. `auth.py`: The Python file `auth.py` is responsible for handling user authentication logic. It manages user login, registration, and other authentication-related tasks within the project.

## Usage
To utilize the functionality provided by the `user_authentication` folder, developers can refer to the `validator.js` file for input validation requirements and integrate the authentication logic from `auth.py` into the project's user management system. Ensure to follow the guidelines and functions defined in these files for secure and efficient user authentication processes.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with specific length and character restrictions.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on various criteria.

**Usage:** To use this file, import `InputValidator` class in your code and call the desired validation functions or password strength calculation function.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, logout, and session authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and has not expired.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations in your application.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints in function signatures.

---
*Auto-generated documentation - Last updated: 2025-07-17 14:14:50*
