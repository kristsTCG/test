# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` for client-side input validation written in JavaScript and `auth.py` for server-side authentication logic written in Python.

## Key Files
- **validator.js**: This file contains client-side validation functions to ensure that user input meets specified criteria before submitting it to the server. It plays a crucial role in enhancing data integrity and security.
  
- **auth.py**: The `auth.py` file is responsible for handling server-side authentication processes. It manages user login, registration, and authentication using Python. This file is essential for securing user accounts and controlling access to sensitive information.

## Usage
1. **validator.js**:
   - To use the validation functions in `validator.js`, include the file in your HTML document using a `<script>` tag.
   - Call the appropriate validation functions on user input fields to ensure data integrity and security.
   
2. **auth.py**:
   - Import the `auth` module in your Python project to access the authentication functionalities.
   - Utilize the provided functions for user registration, login, and authentication to secure user accounts and manage access control.

Ensure to follow best practices for user authentication and data validation while working with the code in this folder.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates if the input username meets specific criteria (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and return a session token.
- `logout`: Method to end a user session using the session token.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your Python application.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON operations.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 21:12:25*
