# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to separate the validation and authentication functionalities into distinct files. The `validator.js` file handles input validation using JavaScript, while the `auth.py` file manages user authentication using Python.

## Key Files
- **validator.js**: This file contains the logic for validating user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before proceeding with authentication.
  
- **auth.py**: The `auth.py` file is responsible for handling user authentication processes. It includes functions for verifying user credentials and granting access to authorized users.

## Usage
1. To utilize the validation functionality, refer to the `validator.js` file and incorporate the validation logic into your application's input handling processes.
   
2. For user authentication, utilize the functions provided in the `auth.py` file to authenticate users based on their credentials.

3. Ensure that the validation and authentication processes are integrated seamlessly into your project to enhance security and user experience.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in other parts of the application.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Register a new user with a unique username.
- `login(username: str, password: str) -> Optional[str]`: Authenticate user and return a session token.
- `logout(session_token: str) -> bool`: End a user session.
- `is_authenticated(session_token: str) -> bool`: Check if a session token is valid.

**Usage:** Instantiate `UserAuth` to manage user authentication. Call `register_user` to add new users, `login` to authenticate users and get a session token, `logout` to end a session, and `is_authenticated` to check session validity.

**Dependencies:** `hashlib`, `json`, `datetime`, `timedelta`, `typing`

---
*Auto-generated documentation - Last updated: 2025-07-17 18:42:55*
