# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. It includes scripts for validating user input and handling user authentication using JavaScript and Python.

## Structure
The folder is organized to handle user authentication tasks. It contains two key files: `validator.js` for client-side input validation and `auth.py` for server-side authentication logic.

## Key Files
- **validator.js**: This JavaScript file contains functions for validating user input on the client-side. It plays a crucial role in ensuring that user-provided data meets the required criteria before submission.
  
- **auth.py**: The Python script `auth.py` is responsible for handling user authentication on the server-side. It manages user login, registration, and authentication processes.

## Usage
1. **validator.js**:
   - Include `validator.js` in your HTML file using `<script>` tags.
   - Call the validation functions provided in `validator.js` to validate user input fields before form submission.

2. **auth.py**:
   - Import `auth.py` in your Python project to utilize the authentication functionalities.
   - Use the functions defined in `auth.py` to handle user registration, login, and authentication processes.

Ensure to follow the documentation within each file for specific usage instructions and function details.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric and underscore characters.
- `getPasswordStrength(password)`: Determines the strength level of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the provided validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user's session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** This file can be imported and used to handle user authentication in Python applications.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 07:59:32*
