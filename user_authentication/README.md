# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files, `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. `validator.js`: This JavaScript file contains functions for validating user input. It plays a crucial role in ensuring that user data meets the required criteria before proceeding with authentication processes.
   
2. `auth.py`: The Python file `auth.py` is responsible for handling authentication logic. It manages user authentication, login, and session management within the project.

## Usage
To work with the code in this folder, follow these steps:
1. Review the `validator.js` file to understand the validation functions available.
2. Utilize the functions in `validator.js` to validate user input before authentication.
3. Refer to `auth.py` for authentication logic implementation and session management.
4. Ensure to integrate these files appropriately within the project's user authentication flow.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length and character requirements.
- `validateUsername(username)`: Validates the format of a username allowing only alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character complexity.

**Usage:** To use this file, import `InputValidator` class where input validation is needed and call the respective validation functions.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session creation, and session validation.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session based on the session token.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: for hashing passwords.
- `json`: for JSON serialization (not used in the provided code snippet).
- `datetime`: for working with dates and times.
- `timedelta`: for calculating time differences.
- `typing`: for type hints (not used in the provided code snippet).

---
*Auto-generated documentation - Last updated: 2025-07-18 03:48:12*
