# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This module handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic for user input. It ensures that user-provided data meets the required criteria before submission.
- **auth.py**: The `auth.py` file is responsible for server-side authentication processes. It manages user authentication, login, and session handling using Python.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to match the project's requirements.
   - Include the `validator.js` file in your HTML pages using a script tag.
   - Call the validation functions on user input fields to validate user data.

2. **auth.py**:
   - Import the `auth` module in your Python scripts where user authentication is required.
   - Utilize the provided functions for user login, authentication, and session management.
   - Customize the authentication logic to integrate with your project's user management system.

Ensure to maintain the integrity of user authentication processes and handle sensitive user data securely.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of being at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token if successful.
  - `logout(session_token: str) -> bool`: Ends a user session based on the session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Instantiate `UserAuth` to access user authentication functionality.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 07:30:50*
