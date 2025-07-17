# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files, `validator.js` for client-side input validation written in JavaScript and `auth.py` for server-side authentication logic written in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic for user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before submission.
  
- **auth.py**: The `auth.py` file contains server-side authentication logic written in Python. It handles user authentication processes, such as login, registration, and session management.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to match the project's requirements.
   - Include the `validator.js` file in the relevant HTML pages using `<script>` tags.
   - Call the validation functions from your form submission logic to validate user input.

2. **auth.py**:
   - Implement additional authentication functionalities as required by the project.
   - Integrate the authentication logic with other parts of the project that require user authentication.
   - Ensure proper error handling and security measures are in place to protect user data.

By following the guidelines above, you can effectively utilize the `user_authentication` folder in your project for handling user authentication tasks.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters long and consists of alphanumeric characters and underscores only.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user session.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication system.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON operations.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 19:44:58*
