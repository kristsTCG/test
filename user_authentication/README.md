# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user inputs and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` for client-side input validation written in JavaScript and `auth.py` for server-side authentication logic written in Python.

## Key Files
1. **validator.js**
   - Role: Responsible for validating user inputs on the client-side.
   - Size: 1212 characters
   - Language: JavaScript

2. **auth.py**
   - Role: Handles server-side authentication processes.
   - Size: 2198 characters
   - Language: Python

## Usage
1. **validator.js**
   - Ensure the `validator.js` file is linked to your HTML file where user inputs need validation.
   - Modify the validation rules as per your project requirements.
   - Use the functions provided in `validator.js` to validate user inputs before submitting forms.

2. **auth.py**
   - Integrate the `auth.py` file with your server-side application.
   - Utilize the authentication functions defined in `auth.py` to authenticate users during login or other secure operations.
   - Customize the authentication logic to suit your project's security needs.

By following the guidelines above, you can effectively implement user authentication features using the code in the `user_authentication` folder.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of the input password based on length and character types.

**Usage:** To use this file, import it as a module in your JavaScript code using `const InputValidator = require('./validator.js');`.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file provides a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: Used for hashing passwords.
- `json`: Not used in this file but imported.
- `datetime`: Used for handling date and time operations.
- `timedelta`: Used for calculating expiration time for session tokens.
- `typing`: Used for type hints in function definitions.

---
*Auto-generated documentation - Last updated: 2025-07-18 02:02:46*
