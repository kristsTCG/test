# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It handles tasks such as validating user input and managing user authentication using JavaScript and Python scripts.

## Structure
The folder is organized to support user authentication features. It consists of two key files: `validator.js` for client-side validation written in JavaScript and `auth.py` for server-side authentication written in Python.

## Key Files
1. `validator.js`: This JavaScript file contains client-side validation logic for user input. It ensures that user-provided data meets specified criteria before submission.
   
2. `auth.py`: The Python script `auth.py` is responsible for server-side authentication processes. It manages user authentication, such as verifying credentials and granting access to authorized users.

## Usage
To utilize the functionalities provided in the `user_authentication` folder:
1. Modify the validation criteria in `validator.js` to suit the project's requirements.
2. Integrate the server-side authentication logic from `auth.py` into the backend system for user authentication.
3. Ensure that both client-side and server-side scripts work harmoniously to provide a secure and reliable user authentication mechanism.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength and format of a password (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates the format of a username (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the provided validation functions in other parts of the application.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user registration, login, and session management.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** To use this file, create an instance of `UserAuth` and call its methods for user registration, login, logout, and session validation.

**Dependencies:** 
- `hashlib` for hashing functions.
- `json` for JSON serialization.
- `datetime` for date and time operations.
- `timedelta` for time duration calculations.
- `typing` for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 14:04:14*
