# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
  
- **auth.py**: The `auth.py` file is written in Python and is responsible for handling the authentication logic. It manages user authentication processes such as login, registration, and token generation.

## Usage
To utilize the functionalities provided in this folder:
1. Review the `validator.js` file to understand the validation rules and functions available.
2. Explore the `auth.py` file to comprehend the authentication logic and methods implemented.
3. Integrate these files into your project to enable user authentication features effectively.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength and format of a password (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates the format of a username (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Register a new user with a unique username, email, and password.
- `login(username: str, password: str) -> Optional[str]`: Authenticate a user and return a session token.
- `logout(session_token: str) -> bool`: End a user session based on the session token.
- `is_authenticated(session_token: str) -> bool`: Check if a session token is valid and active.

**Usage:** To use this file, create an instance of the `UserAuth` class and call its methods for user registration, login, logout, and authentication.

**Dependencies:** 
- `hashlib`: for hashing passwords using SHA-256.
- `json`: for handling JSON data.
- `datetime`: for working with dates and times.
- `timedelta`: for calculating time differences.
- `typing`: for type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 14:12:34*
