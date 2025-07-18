# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. It includes scripts for validating user input and handling authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It consists of two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. **validator.js**
   - Type: JavaScript
   - Size: 1212 characters
   - Role: Responsible for validating user input data to ensure it meets specified criteria. This file plays a crucial role in maintaining data integrity and security during the authentication process.

2. **auth.py**
   - Type: Python
   - Size: 2198 characters
   - Role: Manages the authentication logic, including user login, registration, and authentication token generation. This file is essential for handling user authentication securely within the project.

## Usage
1. **validator.js**
   - To use the `validator.js` file, import it into your JavaScript code using `import validator from './validator.js';`.
   - Utilize the functions provided in the file to validate user input data before processing it further in the authentication flow.

2. **auth.py**
   - Incorporate the `auth.py` file into your Python project by importing it with `from auth import Auth`.
   - Use the methods defined in the file to implement user authentication features such as login, registration, and token generation in your application.

Ensure to follow the coding standards and guidelines set within the project while working with the files in the `user_authentication` folder.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** This file can be imported using `require` or `import` statements in other JavaScript files to perform input validation for user authentication.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 06:42:29*
