# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It includes scripts for validating user input and handling authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It consists of two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. `validator.js`: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that the user-provided information meets the required criteria for authentication.
   
2. `auth.py`: The Python script `auth.py` is responsible for managing user authentication processes. It handles tasks such as user login, registration, and authentication checks.

## Usage
To utilize the functionalities provided in this folder, follow these steps:
1. Use the functions defined in `validator.js` to validate user input data before processing it for authentication.
2. Incorporate the authentication logic from `auth.py` into your project to enable secure user authentication processes.

Ensure that you understand the functions and methods defined in these files to effectively implement user authentication in your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on its length and character composition.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication, registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication. Call `register_user` to add new users, `login` to authenticate users and get a session token, `logout` to end a session, and `is_authenticated` to check session validity.

**Dependencies:** 
- `hashlib`: For hashing functions.
- `json`: For JSON serialization.
- `datetime`: For date and time operations.
- `timedelta`: For time duration calculations.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 06:25:20*
