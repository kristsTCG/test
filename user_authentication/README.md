# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks. It contains two key files: `validator.js` for client-side input validation in JavaScript and `auth.py` for server-side authentication logic in Python.

## Key Files
1. **validator.js**: This file contains client-side validation logic written in JavaScript. It ensures that user input meets specified criteria before submission.
   
2. **auth.py**: The `auth.py` file contains server-side authentication logic written in Python. It handles user authentication processes such as login, registration, and session management.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to suit the project's requirements.
   - Include the `validator.js` file in your HTML pages using the `<script>` tag.
   - Call the validation functions from your form submission events to validate user input.

2. **auth.py**:
   - Customize the authentication logic to integrate with your project's user management system.
   - Import and use the functions from `auth.py` in your server-side code to authenticate users and manage sessions.

Ensure that both client-side and server-side authentication processes are in sync to provide a secure and seamless user experience.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates an email address using a regular expression.
- `validatePassword(password)`: Validates a password based on length and character requirements.
- `validateUsername(username)`: Validates a username for length and character restrictions.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character complexity.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing password using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 17:02:52*
