# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` for client-side input validation using JavaScript and `auth.py` for server-side authentication logic using Python.

## Key Files
- **validator.js**: This file is responsible for client-side input validation. It contains 1212 characters of JavaScript code to ensure that user inputs meet specified criteria before submission.
  
- **auth.py**: The `auth.py` file contains 2198 characters of Python code that handle server-side authentication processes. This file manages user login, registration, and authentication logic to ensure secure access to the application.

## Usage
To utilize the user authentication functionality in this folder:
1. Use `validator.js` to implement client-side input validation by including the necessary scripts in your HTML files.
2. Incorporate `auth.py` into your server-side code to manage user authentication processes, such as login and registration.
3. Ensure that both files are integrated seamlessly with the rest of your project to provide a secure and user-friendly authentication experience.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** To use this file, import it into your project using `const InputValidator = require('./validator.js');` and then call the validation functions as needed.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user's session by providing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided by this file.

**Dependencies:**
- `hashlib`: For hashing functions.
- `json`: For JSON serialization and deserialization.
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 03:08:04*
