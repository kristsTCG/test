# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript for input validation and `auth.py` written in Python for authentication processes.

## Key Files
- **validator.js**: This file contains functions to validate user input, ensuring data integrity and security.
- **auth.py**: Responsible for handling user authentication processes, such as login, logout, and session management.

## Usage
1. To utilize the input validation functionalities, refer to `validator.js` and incorporate the validation functions in your code.
2. For user authentication tasks, import `auth.py` and utilize the provided functions for secure user authentication processes.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates that a password meets specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates that a username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on its length and character types.

**Usage:** Import this file as `InputValidator` and use its static methods to validate user input for authentication purposes.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session by providing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: Used for hashing passwords.
- `json`: Not used in this file but imported.
- `datetime`: Used for handling date and time operations.
- `timedelta`: Used for calculating expiration time for session tokens.
- `typing`: Used for type hinting in function definitions.

---
*Auto-generated documentation - Last updated: 2025-07-18 02:04:56*
