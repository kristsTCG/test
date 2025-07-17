# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files, `validator.js` for client-side validation written in JavaScript and `auth.py` for server-side authentication logic written in Python.

## Key Files
- `validator.js`: This file contains client-side validation logic to ensure that user input meets specified criteria before submitting it to the server.
  
- `auth.py`: This file contains server-side authentication logic to verify user credentials and manage user authentication processes.

## Usage
1. To use the client-side validation provided by `validator.js`, include this file in your HTML file using a script tag.
   
2. Utilize the functions and methods defined in `validator.js` to validate user input before submitting forms or making requests to the server.
   
3. For server-side authentication, import and use the functions defined in `auth.py` in your Python application to authenticate users and manage user sessions securely.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the specified criteria.
- `validateUsername(username)`: Validates if the input username meets the specified criteria.
- `getPasswordStrength(password)`: Determines the strength of the input password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies are required for this file.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user's session.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your Python application.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hinting in Python.

---
*Auto-generated documentation - Last updated: 2025-07-17 17:12:25*
