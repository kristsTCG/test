# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities in the project. It includes files for validating user input and handling authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. **validator.js**: This file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
   
2. **auth.py**: The `auth.py` file is responsible for managing user authentication processes in Python. It handles tasks such as user login, registration, and authentication checks.

## Usage
To work with the code in this folder:
1. Use `validator.js` functions to validate user input data before processing authentication requests.
2. Utilize `auth.py` functions to manage user authentication processes within the project.
3. Ensure that the code in these files is integrated correctly with other components that interact with user authentication functionalities.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username allowing alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character complexity.

**Usage:** Import `InputValidator` class from this file to use the provided validation methods in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, logout, and session authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: Used for hashing passwords.
- `json`: Not used in the provided code but imported.
- `datetime`: Used for working with dates and times.
- `timedelta`: Used for calculating time differences.
- `typing`: Used for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 07:59:08*
