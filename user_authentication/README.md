# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication processes. It contains two key files: `validator.js` written in JavaScript for input validation and `auth.py` written in Python for authentication logic.

## Key Files
1. **validator.js**
   - Role: Responsible for validating user input.
   - Size: 1212 characters
   - Language: JavaScript

2. **auth.py**
   - Role: Handles authentication logic for user authentication.
   - Size: 2198 characters
   - Language: Python

## Usage
1. **validator.js**
   - To use the validation functions in `validator.js`, import the file into your JavaScript code.
   - Call the appropriate validation functions provided in `validator.js` to validate user input before processing.

2. **auth.py**
   - Import `auth.py` into your Python code to utilize the authentication logic.
   - Use the functions defined in `auth.py` to authenticate users based on the project's requirements.

Ensure to follow the documentation and comments within the files for a better understanding of the functions and methods provided for user authentication.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user's session.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to manage user authentication processes.

**Dependencies:** 
- `hashlib`: for hashing passwords.
- `json`: for handling JSON data.
- `datetime`: for working with dates and times.
- `timedelta`: for calculating time differences.
- `typing`: for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 14:38:12*
