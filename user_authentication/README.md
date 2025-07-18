# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It consists of two key files: `validator.js` written in JavaScript for input validation and `auth.py` written in Python for authentication processes.

## Key Files
1. `validator.js`: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria before proceeding with authentication processes.
   
2. `auth.py`: The Python file `auth.py` is responsible for handling user authentication logic. It manages user login, registration, and authentication processes within the project.

## Usage
To utilize the functionalities provided in this folder:
- Use the functions defined in `validator.js` to validate user input data before processing.
- Incorporate the authentication logic from `auth.py` to manage user authentication processes in the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength level of a password based on various criteria.

**Usage:** Import the `InputValidator` class from this file to use the provided validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file provides a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication, registration, login, logout, and session validation.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication. Call `register_user` to add a new user, `login` to authenticate and generate a session token, `logout` to end a session, and `is_authenticated` to check session validity.

**Dependencies:** 
- `hashlib` for hashing functions.
- `json` for JSON serialization.
- `datetime` for date and time operations.
- `timedelta` for time differences.
- `typing` for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 07:51:56*
