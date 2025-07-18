# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` for client-side validation written in JavaScript and `auth.py` for server-side authentication written in Python.

## Key Files
1. `validator.js`: This file contains client-side validation logic with 1212 characters. It ensures that user input meets specified criteria before submission.
   
2. `auth.py`: This file contains server-side authentication logic with 2198 characters. It manages user authentication processes, such as login, logout, and session management.

## Usage
1. To utilize the client-side validation functionality, refer to `validator.js` and integrate the validation logic into your front-end forms.
   
2. For server-side authentication tasks, utilize `auth.py` to handle user authentication processes in the backend. Ensure to configure it according to your project's requirements.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of being at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on its length and character composition.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password()`: Method to hash a password using SHA-256.
- `register_user()`: Method to register a new user with a unique username, email, and password.
- `login()`: Method to authenticate a user with a username and password and generate a session token.
- `logout()`: Method to end a user's session by invalidating the session token.
- `is_authenticated()`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization.
- `datetime`: For date and time operations.
- `timedelta`: For calculating expiration time of session tokens.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 08:26:23*
