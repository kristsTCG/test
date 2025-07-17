# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This module is responsible for validating user input and handling user authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes the following key components:
- `validator.js`: A JavaScript file containing functions for validating user input data.
- `auth.py`: A Python file that implements user authentication logic.

## Key Files
### validator.js
This file contains functions to validate user input data, ensuring that the data meets the required criteria before processing it further.

### auth.py
The `auth.py` file is crucial for handling user authentication processes. It includes functions for user login, registration, and other authentication-related tasks.

## Usage
1. To utilize the validation functions in `validator.js`, import the necessary functions into your JavaScript files and call them as needed to validate user input data.
   
   Example:
   ```javascript
   import { validateUsername, validatePassword } from './validator.js';
   
   if (validateUsername(username) && validatePassword(password)) {
       // Proceed with further processing
   } else {
       // Display error messages to the user
   }
   ```

2. In Python scripts, import the `auth.py` module to access user authentication functionalities. Use the provided functions for user login, registration, and other authentication tasks.

   Example:
   ```python
   from auth import login, register
   
   user_credentials = {
       'username': 'example_user',
       'password': 'secure_password'
   }
   
   if login(user_credentials):
       # User authentication successful
   else:
       # User authentication failed
   ```

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets certain criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates if the input username meets certain criteria (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class in your code. Example: `const InputValidator = require('./validator.js');`

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, logout, and session validation.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and not expired.

**Usage:** To use this authentication system, create an instance of `UserAuth` and call its methods for user registration, login, logout, and session validation.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating expiration time for session tokens.
- `typing`: For type hints in function signatures.

---
*Auto-generated documentation - Last updated: 2025-07-17 15:57:01*
