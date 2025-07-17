# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It consists of two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
  
- **auth.py**: The Python file `auth.py` is responsible for handling the authentication process. It manages user login, registration, and authentication tasks within the system.

## Usage
To utilize the functionality provided in this folder:
1. Review the `validator.js` file to understand the validation logic and criteria for user input.
2. Explore the `auth.py` file to grasp the authentication process flow and functions available for user management.
3. Integrate these files into your project to enable user authentication features effectively.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of being at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character complexity.

**Usage:** To use this file, import `InputValidator` class from `validator.js` into your code.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
  - `hash_password`: Method to hash a password using SHA-256.
  - `register_user`: Method to register a new user with a unique username, email, and password.
  - `login`: Method to authenticate a user with a username and password and generate a session token.
  - `logout`: Method to end a user session based on the session token.
  - `is_authenticated`: Method to check if a session token is still valid.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing functions.
- `json`: For JSON serialization and deserialization.
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hinting.

---
*Auto-generated documentation - Last updated: 2025-07-17 16:34:59*
