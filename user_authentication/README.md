# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It includes a JavaScript file for validation logic and a Python file for handling authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files, `validator.js` for client-side validation and `auth.py` for server-side authentication.

## Key Files
1. **validator.js**
   - Role: Manages client-side validation logic for user input.
   - Size: 1212 characters
   - Language: JavaScript

2. **auth.py**
   - Role: Handles server-side authentication processes.
   - Size: 2198 characters
   - Language: Python

## Usage
1. **validator.js**
   - Modify validation rules: Update the validation logic in this file to customize the validation rules for user input on the client-side.
   - Integrate with front-end: Link this file to your front-end code to enable real-time validation of user input.

2. **auth.py**
   - Configure authentication methods: Implement and customize authentication methods as per project requirements.
   - Integrate with back-end: Ensure this file is properly integrated into your back-end system to handle user authentication securely.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on its length and character composition.

**Usage:** Import `InputValidator` class from this file to use the provided validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations like registration, login, logout, and session validation.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-18 06:49:45*
