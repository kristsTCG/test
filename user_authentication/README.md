# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder consists of two key files: `validator.js` written in JavaScript and `auth.py` written in Python. These files handle user input validation and authentication logic respectively.

## Key Files
1. `validator.js`: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria before proceeding with authentication processes.

2. `auth.py`: The Python file `auth.py` is responsible for handling user authentication within the project. It manages user login, registration, and authentication processes to ensure secure access to the system.

## Usage
1. To utilize the validation functions provided in `validator.js`, import the necessary functions into your JavaScript files and call them as needed to validate user input data.

2. For user authentication functionalities, interact with the `auth.py` file in Python. Use the defined functions to handle user registration, login, and authentication processes within the project. Ensure to follow the established authentication flow for secure user access.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of the input password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Register a new user with a unique username, email, and password.
- `login(username: str, password: str) -> Optional[str]`: Authenticate a user and return a session token.
- `logout(session_token: str) -> bool`: End a user's session based on the provided session token.
- `is_authenticated(session_token: str) -> bool`: Check if a session token is valid and the user is authenticated.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON encoding and decoding.
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 03:00:45*
