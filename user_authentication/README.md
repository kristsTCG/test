# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It handles validation of user input and authentication processes.

## Structure
The folder is organized to separate the validation logic in `validator.js` (JavaScript) and the authentication logic in `auth.py` (Python).

## Key Files
- **validator.js**: This file contains the validation logic for user input. It ensures that the data provided by users meets the required criteria before proceeding with authentication processes.
  
- **auth.py**: The `auth.py` file houses the authentication logic using Python. It manages user authentication, including login, registration, and session management.

## Usage
1. To utilize the validation capabilities, refer to `validator.js` for functions and methods related to validating user input.
2. For authentication functionalities, interact with `auth.py` to handle user authentication processes such as login, registration, and session management.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long, alphanumeric, and contains underscores only.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user's session using their session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 17:20:59*
