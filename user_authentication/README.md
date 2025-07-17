# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. **validator.js**: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
   
2. **auth.py**: The Python file `auth.py` is responsible for handling user authentication processes. It manages user login, registration, and authentication logic within the system.

## Usage
To utilize the functionalities provided in this folder:
- Use the `validator.js` file to validate user input data before processing it further.
- Incorporate the `auth.py` file to manage user authentication processes such as login, registration, and authentication within the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the format of a password, requiring at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates the format of a username, requiring 3-20 characters that are alphanumeric and underscores only.
- `getPasswordStrength(password)`: Calculates the strength of a password based on its length and character composition.

**Usage:** Import the `InputValidator` class from this file to use its validation functions in user authentication processes.

**Dependencies:** None

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session based on the session token provided.
- `is_authenticated`: Method to check if a session token is valid and the user is authenticated.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided.

**Dependencies:** 
- `hashlib` for hashing passwords.
- `json` for JSON serialization (not used in the provided code).
- `datetime` for handling date and time operations.
- `timedelta` for calculating time differences.
- `typing` for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 21:26:49*
