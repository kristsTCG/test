# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. These files handle user validation and authentication processes.

## Structure
The folder is organized to separate the validation logic in `validator.js` (JavaScript) and the authentication logic in `auth.py` (Python).

## Key Files
- `validator.js`: This file contains the JavaScript code for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria.
- `auth.py`: The Python file `auth.py` is responsible for handling user authentication processes. It manages user login, registration, and authentication functionalities.

## Usage
1. To work with the validation logic, refer to `validator.js`. This file contains functions for validating user input data such as email addresses, passwords, and other user information.
2. For user authentication processes, utilize `auth.py`. This file provides functions for user login, registration, and authentication. Make sure to integrate these functions into the project's user management system.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates that a password meets specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates that a username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character complexity.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization.
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 16:02:43*
