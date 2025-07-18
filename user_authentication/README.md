# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities within the project. It includes validation logic in JavaScript and authentication logic in Python.

## Structure
The folder is organized to handle user authentication tasks. It contains two key files: `validator.js` for input validation and `auth.py` for user authentication.

## Key Files
1. `validator.js`: This JavaScript file contains logic for validating user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before proceeding with authentication.
   
2. `auth.py`: The Python file `auth.py` is responsible for handling user authentication processes. It manages user login, registration, and authentication tasks within the project.

## Usage
To utilize the functionalities provided in this folder:
- Use the `validator.js` file to validate user input data before processing authentication.
- Utilize the `auth.py` file to manage user authentication tasks such as login, registration, and authentication processes.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on various criteria.

**Usage:** To use this file, import `InputValidator` class where input validation is needed and call the respective validation functions.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file provides a user authentication system with login and registration functionality.

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
- `datetime`: Used for working with dates and times.
- `timedelta`: Used for calculating time differences.
- `typing`: Used for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 02:13:41*
