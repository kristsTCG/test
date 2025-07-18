# user_authentication

## Overview
The user_authentication folder contains files related to user authentication functionality in the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains validator.js for client-side input validation and auth.py for server-side authentication.

## Key Files
1. **validator.js**: This JavaScript file contains client-side validation logic to ensure that user input meets specified criteria before submission.
   
2. **auth.py**: This Python file is responsible for server-side authentication processes, such as verifying user credentials and managing user sessions.

## Usage
1. **validator.js**: To use the client-side validation logic, include the validator.js file in your HTML file using a script tag. You can then call the validation functions defined within this file to validate user input before submitting forms.

2. **auth.py**: To utilize the server-side authentication functionalities, import the auth.py file in your Python project. You can then use the functions provided in this file to authenticate users, manage sessions, and handle user authentication-related tasks.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength level of a password based on various criteria.

**Usage:** Import `InputValidator` class from this file to use the validation functions in other parts of the application.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user's session.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Import `UserAuth` class from this file to handle user authentication in your Python application.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-18 02:44:57*
