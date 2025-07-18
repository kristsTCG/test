# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user inputs and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. `validator.js`: This file contains functions for validating user inputs such as email addresses, passwords, and other user data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
   
2. `auth.py`: This Python file is responsible for handling user authentication processes. It includes functions for user login, registration, and authentication checks. `auth.py` interacts with the database to verify user credentials and manage user sessions.

## Usage
1. To utilize the validation functions provided in `validator.js`, import the file into your JavaScript code and call the necessary validation functions with user inputs as parameters.
   
2. For user authentication tasks, import `auth.py` into your Python code. Use the functions within `auth.py` to manage user registration, login, and authentication processes. Ensure that the necessary database connections are established for authentication to work correctly.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates that a password meets certain criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates that a username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** This file can be imported as a module in a Node.js application using `const InputValidator = require('./validator.js');`.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization and deserialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 07:59:57*
