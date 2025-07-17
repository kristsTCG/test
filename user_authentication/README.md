# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This JavaScript file contains functions to validate user input data. It plays a crucial role in ensuring that user data meets the required criteria for authentication.
  
- **auth.py**: The Python file `auth.py` is responsible for handling user authentication processes. It manages user login, registration, and authentication using secure methods.

## Usage
1. To utilize the functionalities provided by `validator.js`, import the file into your JavaScript code and use the validation functions as needed.
   
2. For user authentication tasks, import `auth.py` into your Python code. Use the functions within `auth.py` to manage user login, registration, and authentication processes securely.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on various criteria.

**Usage:** To use this file, import `InputValidator` class and call the desired validation methods on user input.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user session.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For JSON operations.
- `datetime`: For working with dates and times.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 16:02:13*
