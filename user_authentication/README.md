# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. This includes validation of user input and authentication logic.

## Structure
The folder `user_authentication` contains two key files:
- `validator.js`: A JavaScript file with 1212 characters that handles user input validation.
- `auth.py`: A Python file with 2198 characters that manages user authentication processes.

## Key Files
### validator.js
- **Role**: Handles user input validation.
- **Character count**: 1212
- **Usage**: Validates user input to ensure data integrity and security.

### auth.py
- **Role**: Manages user authentication processes.
- **Character count**: 2198
- **Usage**: Implements authentication logic such as login, logout, and user session management.

## Usage
1. Ensure that the necessary dependencies for both JavaScript and Python are installed.
2. Use `validator.js` for validating user input before processing it further.
3. Utilize `auth.py` for implementing user authentication functionalities in the project.
4. Refer to the specific functions within each file for detailed usage instructions.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication, registration, login, and session handling.
- `hash_password`: Method to hash passwords using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with username and password, generating a session token.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate `UserAuth` to manage user authentication operations like registration, login, logout, and session validation.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For time-based calculations.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 00:15:59*
