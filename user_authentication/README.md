# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. **validator.js**
   - Language: JavaScript
   - Size: 1212 characters
   - Role: Responsible for validating user input data to ensure it meets specified criteria and formats.

2. **auth.py**
   - Language: Python
   - Size: 2198 characters
   - Role: Manages user authentication processes such as login, registration, and user session handling.

## Usage
1. **validator.js**
   - To use the validation functions provided in `validator.js`, import the necessary functions into your JavaScript files using `import { functionName } from './validator.js';`.
   - Call the required validation functions passing the user input data as arguments to validate the input.

2. **auth.py**
   - Import the `auth` module into your Python scripts using `from auth import *`.
   - Utilize the functions provided in `auth.py` for user authentication tasks such as login, registration, and session management.

Ensure to follow the documentation within each file for specific usage instructions and guidelines.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates an email address based on a regular expression.
- `validatePassword(password)`: Validates a password to ensure it meets specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates a username to ensure it is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of a password based on its length and character composition.

**Usage:** This file can be imported into other JavaScript files using `require` or `import` statements to perform input validation for user authentication.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session management, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 20:28:40*
