# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It includes a JavaScript file for validation and a Python file for handling authentication.

## Structure
The folder is organized to handle user authentication tasks. It contains two key files, `validator.js` for client-side validation and `auth.py` for server-side authentication.

## Key Files
1. **validator.js**: This JavaScript file contains client-side validation logic for user input. It ensures that user-provided data meets the required criteria before submission.
   
2. **auth.py**: The Python file `auth.py` handles server-side authentication processes. It manages user login, registration, and authentication against the system.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed by updating the logic within `validator.js`.
   - Include the script in your HTML file using `<script src="path/to/validator.js"></script>`.

2. **auth.py**:
   - Use the functions provided in `auth.py` to implement user authentication features in your Python application.
   - Ensure to configure the necessary database connections and security measures as per your project requirements.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the provided validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user's session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** This file can be imported into other Python scripts to handle user authentication processes.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-18 04:14:26*
