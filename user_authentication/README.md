# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It includes a JavaScript file for validation logic and a Python file for handling authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files, `validator.js` for client-side validation and `auth.py` for server-side authentication.

## Key Files
1. **validator.js**
   - Role: Handles client-side validation logic for user input.
   - Size: 1212 characters
   - Language: JavaScript

2. **auth.py**
   - Role: Manages server-side authentication processes.
   - Size: 2198 characters
   - Language: Python

## Usage
1. **validator.js**
   - Ensure the `validator.js` file is included in your HTML file using a script tag.
   - Use the functions defined in `validator.js` to validate user input on the client-side before submitting forms.

2. **auth.py**
   - Import the `auth.py` module in your Python code where authentication is required.
   - Utilize the functions provided in `auth.py` to authenticate users and manage user sessions securely.

Remember to handle user authentication securely to protect user data and ensure the integrity of the system.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters, alphanumeric, and underscores only.
- `getPasswordStrength(password)`: Calculates the strength level of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user's session using their session token.
- `is_authenticated`: Method to check if a session token is valid and the user is authenticated.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-18 08:28:53*
