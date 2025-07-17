# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files, `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
  
- **auth.py**: The Python file `auth.py` is responsible for handling user authentication processes. It includes functions for user login, registration, and authentication.

## Usage
To utilize the code in this folder effectively, follow these steps:
1. Review the `validator.js` file to understand the validation logic and criteria.
2. Explore the `auth.py` file to familiarize yourself with the authentication processes implemented.
3. Integrate these files into your project as needed for user authentication functionalities.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates that a password meets certain criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates that a username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** To use this file, import it using `require` or `import` statements, then call the desired validation functions on user input.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file provides a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication, registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication. Use the provided methods to register users, authenticate logins, manage sessions, and check authentication status.

**Dependencies:** 
- `hashlib`: For hashing functions.
- `json`: For JSON serialization and deserialization.
- `datetime`: For date and time handling.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 16:26:00*
