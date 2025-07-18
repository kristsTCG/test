# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. **validator.js**: This file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
   
2. **auth.py**: The `auth.py` file is responsible for handling user authentication processes using Python. It includes functions for user login, registration, and authentication.

## Usage
To work with the code in this folder:
- Use `validator.js` for validating user input data before processing it for authentication.
- Utilize `auth.py` for implementing user authentication functionalities in Python, such as login, registration, and authentication processes.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class where input validation is needed.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
  
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and hashed password.
  
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user with a username and password, returning a session token if successful.
  
  - `logout(session_token: str) -> bool`: Ends a user session based on the provided session token.
  
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication processes.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing.Optional`: For type hinting.

---
*Auto-generated documentation - Last updated: 2025-07-18 01:46:15*
