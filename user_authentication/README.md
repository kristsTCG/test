# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files, `validator.js` and `auth.py`, which are crucial for validating user input and implementing authentication logic, respectively.

## Key Files
1. `validator.js`: This JavaScript file contains functions for validating user input. It plays a crucial role in ensuring that user-provided data meets the required criteria for authentication.
   
2. `auth.py`: This Python file handles the authentication logic for users. It manages user login, registration, and authentication processes within the project.

## Usage
To utilize the functionalities provided in the `user_authentication` folder:
1. Modify the `validator.js` file to customize input validation rules as per project requirements.
2. Utilize the functions defined in `auth.py` to handle user authentication processes such as login, registration, and authentication.
3. Ensure that both files are integrated correctly within the project to enable seamless user authentication functionalities.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username allowing only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class from this module and call the desired validation functions or password strength calculation function.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user's session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication processes.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with date and time information.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 22:01:06*
