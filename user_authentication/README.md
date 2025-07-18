# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` for client-side input validation in JavaScript and `auth.py` for server-side authentication logic in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic written in JavaScript. It ensures that user input meets specified criteria before submitting to the server for authentication.
  
- **auth.py**: The `auth.py` file contains server-side authentication logic written in Python. It handles user authentication processes such as verifying credentials, generating tokens, and managing user sessions.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to match the project requirements.
   - Include the `validator.js` script in your HTML files to enable client-side validation.

2. **auth.py**:
   - Implement additional authentication methods or customize the existing logic to suit your project's needs.
   - Integrate the authentication functionalities provided in `auth.py` with your server-side codebase.

Ensure that both client-side and server-side authentication processes are in sync to provide a secure and seamless user experience.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of being at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on its length and character composition.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None

## auth.py

**Purpose:** User authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password, returning a session token.
- `logout`: Method to end a user's session using their session token.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate `UserAuth` to manage user authentication, registration, login, logout, and session validation.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For JSON operations.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 00:54:51*
