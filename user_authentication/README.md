# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes the following key components:
- `validator.js`: A JavaScript file containing functions for validating user input and data.
- `auth.py`: A Python file responsible for handling user authentication processes.

## Key Files
### validator.js
- Role: Provides functions for validating user input and data.
- Size: 1212 characters

### auth.py
- Role: Manages user authentication processes.
- Size: 2198 characters

## Usage
1. To utilize the validation functions in `validator.js`, import the file in your JavaScript code and call the necessary functions to validate user input.
2. For user authentication processes, import `auth.py` in your Python code and utilize the functions provided to authenticate users securely.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username for user authentication.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the provided validation methods in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, logout, and session authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations. Call methods like `register_user`, `login`, `logout`, and `is_authenticated` as needed.

**Dependencies:** 
- `hashlib` for password hashing.
- `json` for JSON operations.
- `datetime` for working with dates and times.
- `timedelta` for calculating time differences.
- `typing` for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 08:21:58*
