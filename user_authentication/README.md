# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This functionality is crucial for managing user access and security.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes validator.js for client-side validation and auth.py for server-side authentication logic.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation functions to ensure that user input meets specified criteria before submitting it for authentication.
- **auth.py**: The Python file auth.py implements server-side authentication logic, handling user login, registration, and session management.

## Usage
1. To utilize the client-side validation functions, reference the validator.js file in your HTML or JavaScript code.
2. Use the functions provided in validator.js to validate user input fields such as email addresses, passwords, etc.
3. In your server-side code, import and utilize the functions defined in auth.py to manage user authentication processes, including login, registration, and session handling.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates an email address based on a regular expression pattern.
- `validatePassword(password)`: Validates a password based on specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates a username based on specific criteria (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class in your code and call the desired validation functions or password strength function.

**Dependencies:** None.

## auth.py

**Purpose:**  
User authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session using a session token.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:**  
Instantiate `UserAuth` to access user authentication functionalities like registration, login, logout, and session validation.

**Dependencies:**  
- `hashlib`: For hashing functions.
- `json`: For JSON handling.
- `datetime`: For date and time operations.
- `timedelta`: For time duration calculations.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 00:45:28*
