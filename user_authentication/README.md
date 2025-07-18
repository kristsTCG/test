# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes the following key components:
- `validator.js`: A JavaScript file containing functions for user input validation.
- `auth.py`: A Python file responsible for user authentication logic.

## Key Files
### validator.js
- **Role**: Handles user input validation.
- **Character Count**: 1212
- **Usage**: Ensures that user input meets specified criteria before proceeding with authentication processes.

### auth.py
- **Role**: Manages user authentication processes.
- **Character Count**: 2198
- **Usage**: Implements authentication logic such as verifying user credentials and granting access based on authentication status.

## Usage
1. Utilize `validator.js` for validating user input before authentication.
2. Implement `auth.py` to manage user authentication processes within the project.
3. Ensure to understand the roles of each file to effectively handle user authentication tasks.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric and underscores, 3-20 characters long.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the provided validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and not expired.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hinting (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-18 01:45:05*
