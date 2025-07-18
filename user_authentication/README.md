# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication logic. It includes validator.js for client-side validation written in JavaScript and auth.py for server-side authentication written in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic for user inputs. It helps ensure that user-provided data meets the required criteria before submission.
- **auth.py**: The auth.py file is responsible for server-side authentication processes. It manages user authentication, login, and session handling within the application.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to match the project's requirements.
   - Include the validator.js file in your HTML pages using a script tag to enable client-side validation.

2. **auth.py**:
   - Integrate the auth.py file with your server-side code to handle user authentication.
   - Utilize the functions provided in auth.py for user login, authentication, and session management.

Ensure that both client-side and server-side validation processes are in sync to maintain a secure and user-friendly authentication system.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric and underscore characters.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** This file can be imported as a module to perform input validation for user authentication in a JavaScript application.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing password using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-18 02:46:54*
