# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. **validator.js**
   - Role: This file contains functions for validating user input data.
   - Size: 1212 characters
   - Language: JavaScript

2. **auth.py**
   - Role: This file handles user authentication logic, such as login, registration, and session management.
   - Size: 2198 characters
   - Language: Python

## Usage
1. **validator.js**
   - To use the validation functions in `validator.js`, import the necessary functions into your JavaScript files.
   - Example:
     ```javascript
     import { validateEmail, validatePassword } from './validator.js';
     
     const email = 'example@email.com';
     if (validateEmail(email)) {
         console.log('Email is valid');
     } else {
         console.log('Email is invalid');
     }
     ```

2. **auth.py**
   - Utilize the authentication functionalities provided in `auth.py` by importing and calling the necessary functions in your Python code.
   - Example:
     ```python
     from auth import login, register
     
     username = 'example_user'
     password = 'secure_password'
     
     if login(username, password):
         print('Login successful')
     else:
         print('Login failed')
     ```

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, logout, and session authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user's session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations. Call methods like `register_user`, `login`, `logout`, and `is_authenticated` as needed.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating expiration time for session tokens.
- `typing`: For type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-18 02:41:07*
