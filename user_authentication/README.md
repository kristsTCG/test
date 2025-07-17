# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes validator.js for client-side input validation and auth.py for server-side authentication processes.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation logic for user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before submission.
  
- **auth.py**: The Python file `auth.py` is responsible for server-side authentication processes. It manages user authentication, such as login, registration, and session management.

## Usage
1. **validator.js**:
   - Modify the validation rules in `validator.js` to suit the specific requirements of the project.
   - Include `validator.js` in your HTML files using a script tag to enable client-side validation.

2. **auth.py**:
   - Implement the necessary authentication logic in `auth.py`, such as user registration, login, and password hashing.
   - Integrate `auth.py` with other parts of the project that require user authentication functionalities.

Ensure that both files work together seamlessly to provide a secure and user-friendly authentication experience for the project users.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates an email address using a regular expression.
- `validatePassword(password)`: Validates a password based on specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates a username for length (3-20 characters) and character restrictions (alphanumeric and underscores only).
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user's session.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization.
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 20:28:20*
