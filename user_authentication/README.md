# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It handles validation and authentication processes for user accounts.

## Structure
The folder is organized to manage user authentication logic efficiently. It includes two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. **validator.js**
   - Role: Responsible for validating user input data.
   - Size: 1212 characters
   - Language: JavaScript

2. **auth.py**
   - Role: Manages user authentication processes.
   - Size: 2198 characters
   - Language: Python

## Usage
1. **validator.js**
   - To use the validation functions provided in `validator.js`, import the module into your JavaScript files.
   - Example:
     ```javascript
     import { validateEmail, validatePassword } from './validator.js';
     
     const email = 'example@example.com';
     if (validateEmail(email)) {
         console.log('Email is valid');
     } else {
         console.log('Email is invalid');
     }
     ```

2. **auth.py**
   - Utilize the authentication functionalities provided in `auth.py` by importing the module into your Python scripts.
   - Example:
     ```python
     from auth import authenticate_user, create_user
     
     username = 'example_user'
     password = 'password123'
     
     create_user(username, password)
     
     if authenticate_user(username, password):
         print('User authenticated successfully')
     else:
         print('Authentication failed')
     ```

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric and underscore characters.
- `getPasswordStrength(password)`: Determines the strength level of a password based on various criteria.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user's session based on the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 03:38:08*
