# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities within the project. It includes validation logic in JavaScript and authentication logic in Python.

## Structure
The folder is organized to handle user authentication processes. It includes two key files: `validator.js` for input validation and `auth.py` for user authentication.

## Key Files
1. `validator.js`: This JavaScript file contains logic for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
   
2. `auth.py`: This Python file handles user authentication processes. It includes functions for user login, registration, and authentication checks. 

## Usage
To work with the code in this folder:
- Use `validator.js` for validating user input data before processing authentication requests.
- Utilize `auth.py` for implementing user authentication functionalities such as login, registration, and authentication checks.
- Ensure to follow the specific functions and methods defined in each file for seamless integration with the user authentication system.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates an email address using a regular expression.
- `validatePassword(password)`: Validates a password based on specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates a username for length (3-20 characters) and alphanumeric characters with underscores only.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class in your code and call its methods as needed.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user's session.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to use the provided authentication functionality.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 21:31:22*
