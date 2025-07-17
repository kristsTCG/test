# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder `user_authentication` contains two key files:
- `validator.js`: A JavaScript file with 1212 characters, responsible for validating user input data.
- `auth.py`: A Python file with 2198 characters, handling user authentication processes.

## Key Files
### validator.js
- **Role**: Validates user input data to ensure it meets specified criteria.
- **Size**: 1212 characters
- **Usage**: Used to validate user input before processing it further in the authentication flow.

### auth.py
- **Role**: Manages user authentication processes such as login, logout, and session management.
- **Size**: 2198 characters
- **Usage**: Contains the core logic for user authentication within the project.

## Usage
1. To utilize the validation functionality, refer to `validator.js` and integrate the validation logic into your user input handling code.
2. For user authentication processes, refer to `auth.py` and use the provided functions for login, logout, and session management within your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric and underscore characters.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user's session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to use the provided authentication functionalities.

**Dependencies:**
- `hashlib`: Used for hashing passwords.
- `json`: Not used in the provided code but imported.
- `datetime`: Used for handling date and time operations.
- `timedelta`: Used for calculating expiration time for session tokens.
- `typing`: Used for type hinting in function definitions.

---
*Auto-generated documentation - Last updated: 2025-07-17 22:47:17*
