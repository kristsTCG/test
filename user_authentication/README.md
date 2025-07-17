# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication features efficiently. It includes the following key components:
- `validator.js`: A JavaScript file containing functions for validating user input data.
- `auth.py`: A Python file responsible for handling user authentication logic.

## Key Files
### validator.js
- Role: Provides functions for validating user input data.
- Size: 1212 characters

### auth.py
- Role: Manages user authentication processes.
- Size: 2198 characters

## Usage
To utilize the user authentication features in this folder:
1. Use the functions provided in `validator.js` to validate user input data.
2. Implement the authentication logic defined in `auth.py` for user authentication processes.

Ensure to integrate these files into the project's authentication system for seamless user validation and authentication.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates an email address using a regular expression.
- `validatePassword(password)`: Validates a password based on specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates a username for length (3-20 characters) and alphanumeric/underscore characters only.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your application.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating expiration time for session tokens.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 15:37:58*
