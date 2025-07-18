# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. These files handle user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. **validator.js**: This JavaScript file contains 1212 characters and is responsible for validating user input data. It ensures that the data provided by users meets the required criteria for authentication.
   
2. **auth.py**: This Python file consists of 2198 characters and handles the authentication logic for users. It verifies user credentials and manages the authentication process within the system.

## Usage
To utilize the functionalities provided by the `user_authentication` folder, follow these steps:
1. Use the `validator.js` file to validate user input data before processing it for authentication.
2. Utilize the `auth.py` file to authenticate users based on their credentials and manage the authentication flow within the system.

Ensure that you integrate these files into your project's authentication system to enhance security and user verification processes.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long, alphanumeric, and contains underscores only.
- `getPasswordStrength(password)`: Determines the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the provided validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file provides a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and not expired.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations like registration, login, logout, and session validation.

**Dependencies:** 
- `hashlib` for hashing functions.
- `json` for JSON serialization (not used in this file).
- `datetime` for working with dates and times.
- `timedelta` for calculating time differences.
- `typing` for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 03:52:33*
