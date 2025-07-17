# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. These files handle validation of user input and authentication processes.

## Structure
The folder contains two key files:
- `validator.js` (JavaScript): Responsible for validating user input data.
- `auth.py` (Python): Handles user authentication processes.

## Key Files
### validator.js
- Role: Validates user input data.
- Size: 1212 characters
- Language: JavaScript

### auth.py
- Role: Manages user authentication processes.
- Size: 2198 characters
- Language: Python

## Usage
1. To utilize the validation functionality, refer to `validator.js` and integrate the validation logic into your user input forms.
2. For user authentication processes, utilize `auth.py` and call the necessary functions to authenticate users within the system.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password, returning a session token.
- `logout`: Method to end a user's session based on the session token.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations. Call methods like `register_user`, `login`, `logout`, and `is_authenticated` as needed.

**Dependencies:** 
- `hashlib`: Used for hashing passwords.
- `json`: Not used in this file but imported.
- `datetime`: Used for handling timestamps and session expiration.
- `timedelta`: Used for calculating session expiration time.
- `typing`: Used for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 14:57:27*
