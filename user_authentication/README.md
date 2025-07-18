# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities within the project. It includes validation logic in JavaScript and authentication logic in Python.

## Structure
The folder is organized to handle user authentication processes. The key components include:
- `validator.js`: Contains JavaScript code for validating user input data.
- `auth.py`: Contains Python code for user authentication and authorization.

## Key Files
### validator.js
- Role: Responsible for validating user input data.
- Size: 1212 characters

### auth.py
- Role: Handles user authentication and authorization.
- Size: 2198 characters

## Usage
1. To use the validation logic in `validator.js`, import the file and call the appropriate validation functions on user input data.
2. For user authentication and authorization, utilize the functions and classes defined in `auth.py` by importing and integrating them into the project's authentication flow.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Determines the strength level of a password based on length and character requirements.

**Usage:** To use this file, import `InputValidator` class into your code and call the desired validation functions or password strength function as needed.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user's session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations like registration, login, and session handling.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 01:04:54*
