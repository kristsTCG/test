# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities within the project. It includes validation logic in JavaScript and authentication logic in Python.

## Structure
The folder is organized to handle user authentication tasks. The key components include a validator script written in JavaScript and an authentication module in Python.

## Key Files
- **validator.js**: This JavaScript file contains validation logic for user input. It plays a crucial role in ensuring that user-provided data meets the required criteria for authentication.
- **auth.py**: The Python file `auth.py` is responsible for handling user authentication processes. It manages user login, registration, and authentication tasks within the system.

## Usage
1. To utilize the validation logic, refer to `validator.js` in your JavaScript code. Import and use the functions provided to validate user input.
2. For user authentication tasks, interact with the `auth.py` module in Python. Use the functions and classes defined within this file to manage user authentication processes in your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** This file can be imported into other JavaScript files using `require` or `import` statements to perform input validation for user authentication.

**Dependencies:** No external dependencies are required for this file.

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
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 19:55:55*
