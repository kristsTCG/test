# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This module handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication logic. It includes validator.js for client-side validation written in JavaScript and auth.py for server-side authentication written in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic for user input. It plays a crucial role in ensuring that user-provided data meets specified criteria before submission.
- **auth.py**: The `auth.py` file is responsible for server-side authentication processes. It manages user authentication, login, and authorization within the application.

## Usage
1. **validator.js**: To use the client-side validation logic, include `validator.js` in your HTML file using a script tag.
   ```html
   <script src="path/to/validator.js"></script>
   ```
   You can then call the validation functions defined in `validator.js` to validate user input before form submission.

2. **auth.py**: To utilize the server-side authentication functionalities, import `auth.py` in your Python project.
   ```python
   from user_authentication.auth import authenticate_user, login_user
   ```
   You can then use the provided functions like `authenticate_user` and `login_user` to handle user authentication and login processes in your application.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the specified criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates if the input username meets the specified criteria (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the provided validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

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
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-17 22:19:53*
