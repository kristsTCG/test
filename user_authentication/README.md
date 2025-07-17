# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This module handles user validation and authentication processes.

## Structure
The folder `user_authentication` is organized to include the following key components:
- `validator.js`: A JavaScript file containing functions for validating user input and data.
- `auth.py`: A Python file responsible for handling user authentication logic.

## Key Files
### validator.js
- Role: This file contains functions for validating user input and data.
- Path: `user_authentication/validator.js`
- Size: 1212 characters

### auth.py
- Role: This file manages user authentication processes.
- Path: `user_authentication/auth.py`
- Size: 2198 characters

## Usage
1. To utilize the validation functions in `validator.js`, import the necessary functions into your JavaScript files.
2. Use the functions provided in `validator.js` to validate user input and data.
3. In Python scripts, import `auth.py` to access user authentication functionalities.
4. Implement the authentication logic provided in `auth.py` to handle user authentication within your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user's session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 20:31:46*
