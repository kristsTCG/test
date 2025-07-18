# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It includes scripts for validating user input and handling authentication processes.

## Structure
The folder is organized to handle user authentication logic using both JavaScript and Python. The key components include a validator script written in JavaScript and an authentication script written in Python.

## Key Files
- `validator.js`: This JavaScript file contains functions for validating user input, ensuring data integrity and security during the authentication process.
- `auth.py`: The Python script handles user authentication, including login, registration, and password management functionalities.

## Usage
1. To utilize the validation functions, refer to `validator.js` and import the necessary functions into your JavaScript files.
2. For user authentication processes, interact with the functions defined in `auth.py` using Python scripts or integrate them into your project as needed.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numeric characters.
- `validateUsername(username)`: Validates the format of a username, allowing only alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Determines the strength level of a password based on various criteria.

**Usage:** Import the `InputValidator` class from this file to use the provided validation functions in your authentication logic.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token if successful.
  - `logout(session_token: str) -> bool`: Ends a user session based on the provided session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and the user is authenticated.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your Python application.

**Dependencies:** 
- `hashlib`: For hashing functions.
- `json`: For JSON serialization and deserialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 03:58:48*
