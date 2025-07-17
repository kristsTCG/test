# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
  
- **auth.py**: The Python file `auth.py` is responsible for handling user authentication processes. It includes functions for user login, registration, and authentication.

## Usage
To utilize the functionalities provided in this folder:
1. Review the `validator.js` file to understand the validation logic and criteria.
2. Explore the `auth.py` file to implement user authentication processes in the project.
3. Integrate these files into the project's authentication system as needed.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric and underscore characters.
- `getPasswordStrength(password)`: Determines the strength level of a password based on various criteria.

**Usage:** To use this file, import `InputValidator` class where input validation is needed.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
  
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and hashed password.
  
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user with a username and password, returning a session token if successful.
  
  - `logout(session_token: str) -> bool`: Ends a user session based on the provided session token.
  
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and the user is authenticated.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations like registration, login, session handling, and authentication.

**Dependencies:** 
- `hashlib` for hashing functions.
- `json` for JSON serialization and deserialization.
- `datetime` for working with dates and times.
- `timedelta` for calculating time differences.
- `typing.Optional` for type hinting.
- `typing.Dict` for type hinting dictionaries.

---
*Auto-generated documentation - Last updated: 2025-07-17 23:06:33*
