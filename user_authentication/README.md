# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This functionality is crucial for managing user accounts, authentication, and authorization.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes validator.js for client-side validation logic in JavaScript and auth.py for server-side authentication logic in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic for user input. It ensures that user-provided data meets the required criteria before submission.
- **auth.py**: The `auth.py` file is responsible for server-side authentication processes. It handles user login, registration, and authentication using Python.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to match the project's requirements.
   - Include `validator.js` in your HTML files to enable client-side validation.

2. **auth.py**:
   - Implement additional authentication features as required.
   - Integrate `auth.py` with your backend server to manage user authentication.

Ensure that both client-side and server-side authentication processes are in sync to provide a secure and seamless user experience.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a correct format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3 to 20 characters long and contains only alphanumeric characters and underscores.
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
    - `logout(session_token: str) -> bool`: Ends a user session based on the provided session token.
    - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided by the methods within the class.

**Dependencies:**
- `hashlib`: For hashing functions.
- `json`: For JSON serialization and deserialization.
- `datetime`: For working with dates and times.
- `timedelta`: For representing differences between dates and times.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 20:50:38*
