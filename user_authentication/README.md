# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It includes a JavaScript file for validation logic and a Python file for handling authentication processes.

## Structure
The folder is organized to centralize all user authentication-related code. It follows a modular approach with separate files for different aspects of user authentication.

## Key Files
1. **validator.js**: This JavaScript file contains validation logic for user inputs related to authentication. It plays a crucial role in ensuring that user-provided data meets the required criteria for authentication.
   
2. **auth.py**: The Python file `auth.py` is responsible for handling authentication processes such as user login, registration, and password management. It serves as the backend logic for user authentication within the project.

## Usage
1. To utilize the validation logic provided in `validator.js`, import the necessary functions into your JavaScript files and call them as needed to validate user inputs.
   
2. For user authentication functionalities such as login and registration, interact with the functions defined in `auth.py` from your Python code. Ensure to follow the defined authentication processes and error handling mechanisms in place.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength evaluation.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username allowing alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Evaluates the strength of a password based on length and character complexity.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with username and password and generate a session token.
- `logout`: Method to end a user's session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and not expired.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your Python application.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-18 04:43:18*
