# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This functionality is responsible for validating user input and handling user authentication processes.

## Structure
The folder is organized to separate the validation logic written in JavaScript (`validator.js`) from the authentication logic written in Python (`auth.py`). This separation allows for a clear distinction between the two aspects of user authentication.

## Key Files
- `validator.js`: This JavaScript file contains the validation logic for user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before proceeding with the authentication process.
- `auth.py`: The Python file `auth.py` is responsible for handling the authentication process. It manages user authentication, such as verifying user credentials and granting access to authorized users.

## Usage
1. To utilize the validation logic, refer to the `validator.js` file and incorporate the validation functions into your user input forms or data processing scripts.
2. For user authentication processes, interact with the `auth.py` file. Use the functions and methods provided within this file to authenticate users and manage access control within your application.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters long and consists of alphanumeric characters and underscores only.
- `getPasswordStrength(password)`: Calculates the strength of a password based on its length and character composition.

**Usage:** To use this file, import it into your code using `const InputValidator = require('./validator.js');` or a similar method depending on your project setup. Then, you can call the validation functions as needed.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, logout, and session authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user's session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** To use this file, create an instance of `UserAuth` and call its methods for user registration, login, logout, and session authentication.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in the provided code snippet).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints in function signatures.

---
*Auto-generated documentation - Last updated: 2025-07-17 17:58:56*
