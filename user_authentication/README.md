# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. These files handle user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- `validator.js`: This JavaScript file contains code for validating user input data. It plays a crucial role in ensuring that user data meets the required criteria before proceeding with authentication processes.
- `auth.py`: The Python file `auth.py` is responsible for handling user authentication logic. It manages user login, registration, and authentication processes within the project.

## Usage
To utilize the functionalities provided in this folder:
1. Review the code in `validator.js` to understand the validation criteria for user input data.
2. Explore the logic in `auth.py` to implement user authentication processes such as login, registration, and authentication.
3. Integrate these files into your project to enhance user authentication security and functionality.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is between 3 to 20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates and returns the strength level of a given password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user session.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 07:32:03*
