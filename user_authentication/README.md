# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized with two key files: `validator.js` written in JavaScript and `auth.py` written in Python. These files handle user input validation and authentication processes respectively.

## Key Files
- `validator.js`: This file contains functions to validate user input such as email addresses, passwords, and other form data. It plays a crucial role in ensuring data integrity and security.
- `auth.py`: The `auth.py` file is responsible for handling user authentication processes such as login, logout, and session management. It interacts with the database to verify user credentials and maintain user sessions.

## Usage
1. To use the validation functions in `validator.js`, import the necessary functions into your JavaScript files and call them with the appropriate input data.
2. For user authentication functionalities, import and utilize the methods provided in `auth.py` within your Python code. Ensure proper handling of user login and session management to secure user accounts.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength checking.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** This file can be imported as a module in other JavaScript files using `require` or ES6 `import` statements.

**Dependencies:** No external dependencies are required for this file.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session based on the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 15:29:02*
