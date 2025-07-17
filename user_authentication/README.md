# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes the following key components:
- `validator.js`: A JavaScript file containing functions for validating user input.
- `auth.py`: A Python file responsible for handling user authentication processes.

## Key Files
### validator.js
- Role: Contains functions for validating user input.
- Size: 1212 characters
- Language: JavaScript

### auth.py
- Role: Manages user authentication processes.
- Size: 2198 characters
- Language: Python

## Usage
1. To utilize the validation functions in `validator.js`, import the file into your JavaScript code and call the necessary functions as needed.
2. For user authentication processes, import `auth.py` into your Python code and utilize the functions provided for user authentication tasks.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session using a session token.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize user authentication functionalities.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For JSON operations.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 15:07:08*
