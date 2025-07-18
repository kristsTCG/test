# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes validator.js for client-side validation and auth.py for server-side authentication logic.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation functions to ensure that user input meets specified criteria before submission.
- **auth.py**: The Python file `auth.py` is responsible for handling server-side authentication processes, such as verifying user credentials and managing user sessions.

## Usage
1. To utilize the client-side validation functionalities, refer to `validator.js` and integrate the validation functions into your front-end forms.
2. For server-side authentication tasks, utilize the functions and logic provided in `auth.py` to authenticate users and manage their sessions securely.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Calculates the strength level of a password.

**Usage:** Import the `InputValidator` class from this file to use its validation and strength assessment methods in user authentication processes.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user's session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to access user authentication functionalities like registration, login, and session management.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 05:17:36*
