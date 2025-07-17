# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities in the project. It includes validation logic in JavaScript and authentication logic in Python.

## Structure
The folder is organized to handle user authentication processes. It contains two key files: `validator.js` for input validation and `auth.py` for user authentication.

## Key Files
- **validator.js**: This JavaScript file contains 1212 characters of code responsible for validating user inputs. It ensures that the data entered by users meets the required criteria.
  
- **auth.py**: This Python file contains 2198 characters of code dedicated to user authentication. It handles the process of verifying user credentials and granting access to authorized users.

## Usage
To utilize the code in this folder:
1. Use the functions defined in `validator.js` to validate user inputs before processing.
2. Import and utilize the authentication methods provided in `auth.py` to authenticate users within the project.

Ensure that the code in these files is integrated correctly with the rest of the project's authentication system for seamless user authentication processes.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates if a password meets the criteria of being at least 8 characters long with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if a username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 15:03:23*
