# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This module handles user validation and authentication processes.

## Structure
The folder is organized to separate the validation logic in `validator.js` written in JavaScript and the authentication logic in `auth.py` written in Python.

## Key Files
1. **validator.js**: This file contains the validation logic for user inputs. It ensures that the data provided by users meets the required criteria before proceeding with authentication.
   
2. **auth.py**: The `auth.py` file contains the authentication logic for verifying user credentials and granting access to the system. It manages the login and authentication process for users.

## Usage
1. **validator.js**: To use the validation logic provided in `validator.js`, import the module into your JavaScript code and call the necessary functions to validate user inputs before authentication.
   
2. **auth.py**: To utilize the authentication functionalities in `auth.py`, import the module into your Python code and use the provided functions to authenticate users based on their credentials.

Ensure that you follow the guidelines and integrate these files appropriately within your project to handle user authentication securely.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long, alphanumeric, and contains underscores only.
- `getPasswordStrength(password)`: Determines the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the provided validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your Python application.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For working with JSON data.
- `datetime`: For handling date and time information.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 02:07:53*
