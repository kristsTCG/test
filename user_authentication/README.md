# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. These files handle user validation and authentication processes.

## Structure
The folder is organized to separate the validation logic implemented in JavaScript from the authentication logic implemented in Python.

## Key Files
- `validator.js`: This JavaScript file contains the logic for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
- `auth.py`: The Python file `auth.py` is responsible for handling user authentication processes. It manages user login, registration, and session management within the application.

## Usage
1. To utilize the validation functionality, refer to `validator.js`. Modify or extend the validation rules as needed for your project requirements.
2. For user authentication tasks such as login and registration, interact with the functions provided in `auth.py`. Ensure to integrate these functions into the relevant parts of your application to enable secure user authentication.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates an email address format using a regular expression.
- `validatePassword(password)`: Validates a password format requiring at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates a username format requiring 3-20 characters, alphanumeric, and underscores only.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** This file can be imported as a module in other JavaScript files to perform input validation for user authentication.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password()`: Method to hash a password using SHA-256.
- `register_user()`: Method to register a new user with a unique username, email, and password.
- `login()`: Method to authenticate a user and generate a session token for active sessions.
- `logout()`: Method to end a user session by removing the session token.
- `is_authenticated()`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints in function definitions.

---
*Auto-generated documentation - Last updated: 2025-07-17 23:49:56*
