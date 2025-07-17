# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript for input validation and `auth.py` written in Python for handling authentication logic.

## Key Files
1. **validator.js**
   - Role: Responsible for validating user input data.
   - Language: JavaScript
   - Size: 1212 characters

2. **auth.py**
   - Role: Manages user authentication processes.
   - Language: Python
   - Size: 2198 characters

## Usage
1. **validator.js**
   - To use the validation functions in `validator.js`, import the necessary functions into your JavaScript files.
   - Example:
     ```javascript
     import { validateEmail, validatePassword } from './validator.js';
     
     const email = 'example@email.com';
     if (validateEmail(email)) {
         // Email is valid
     } else {
         // Email is invalid
     }
     ```

2. **auth.py**
   - Utilize the authentication functionalities provided in `auth.py` by importing the necessary functions into your Python scripts.
   - Example:
     ```python
     from auth import authenticate_user, generate_token
     
     username = 'example_user'
     password = 'secure_password'
     
     if authenticate_user(username, password):
         token = generate_token(username)
         # Proceed with authenticated actions using the generated token
     else:
         # Authentication failed, handle accordingly
     ```

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username, allowing only alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: Used for hashing passwords.
- `json`: Not used in this file but imported.
- `datetime`: Used for date and time operations.
- `timedelta`: Used for calculating expiration time for session tokens.
- `typing`: Used for type hinting in function definitions.

---
*Auto-generated documentation - Last updated: 2025-07-17 18:50:19*
