# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It is responsible for validating user input and handling authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` and `auth.py`.

## Key Files
- `validator.js`: This JavaScript file is 1212 characters long and is responsible for validating user input data related to authentication. It ensures that the data provided by users meets the required criteria for authentication.
  
- `auth.py`: This Python file is 2198 characters long and handles the authentication logic for users. It includes functions for user login, registration, and password management.

## Usage
To work with the code in this folder:
1. Use `validator.js` to validate user input data before proceeding with authentication processes.
2. Utilize `auth.py` to implement user authentication functionalities such as login, registration, and password management.
3. Ensure that the functions in `auth.py` are integrated with the rest of the project to enable secure user authentication.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username allowing only alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Determines the strength level of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password()`: Method to hash a password using SHA-256.
- `register_user()`: Method to register a new user with a unique username, email, and password.
- `login()`: Method to authenticate a user with a username and password and generate a session token.
- `logout()`: Method to end a user's session based on the session token.
- `is_authenticated()`: Method to check if a session token is valid and still active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with date and time information.
- `timedelta`: For calculating time differences.
- `typing`: For type hints in function definitions.

---
*Auto-generated documentation - Last updated: 2025-07-17 17:48:05*
