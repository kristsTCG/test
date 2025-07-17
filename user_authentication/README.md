# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It consists of two key files, `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. **validator.js**
   - Type: JavaScript
   - Size: 1212 characters
   - Description: This file contains functions for validating user input, ensuring data integrity and security in the authentication process.

2. **auth.py**
   - Type: Python
   - Size: 2198 characters
   - Description: The `auth.py` file handles the authentication logic, such as user login, registration, and session management. It interacts with the database to authenticate users securely.

## Usage
To utilize the functionalities provided in the `user_authentication` folder, follow these steps:
1. Use the functions defined in `validator.js` to validate user input before processing it further.
2. Incorporate the authentication logic from `auth.py` into your project to enable secure user authentication features.
3. Ensure that the necessary dependencies and configurations are set up to support the user authentication functionalities provided in this folder.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates a password based on specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates a username for length (3-20 characters) and character restrictions (alphanumeric and underscores only).
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your Python application.

**Dependencies:**
- `hashlib`: For hashing functions.
- `json`: For JSON serialization.
- `datetime`: For date and time operations.
- `timedelta`: For time duration calculations.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 14:06:13*
