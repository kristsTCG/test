# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It includes scripts for validating user input and handling authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It consists of two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This JavaScript file contains functions to validate user input for authentication purposes. It plays a crucial role in ensuring that user-provided data meets the required criteria for authentication.
  
- **auth.py**: The Python script `auth.py` is responsible for handling user authentication processes. It manages user login, registration, and authentication tasks within the project.

## Usage
To utilize the functionalities provided in this folder:
1. Review the `validator.js` file to understand the validation logic and customize it as needed for your project.
2. Explore the `auth.py` script to integrate user authentication features into your application.
3. Ensure that the functions in both files are appropriately called and integrated with other parts of the project that require user authentication.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class in your code and call the validation methods as needed.

**Dependencies:** No external dependencies are required for this file.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session by providing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** 
1. Create an instance of `UserAuth` to manage user authentication.
2. Call `register_user` to register a new user.
3. Call `login` to authenticate a user and obtain a session token.
4. Use the session token for subsequent authenticated actions.
5. Call `logout` to end a user session.
6. Call `is_authenticated` to check if a session token is valid.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-17 15:17:50*
