# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. These files handle user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes two key files: `validator.js` for client-side validation written in JavaScript and `auth.py` for server-side authentication written in Python.

## Key Files
1. **validator.js**: This file contains client-side validation logic for user input. It ensures that the data entered by the user meets the required criteria before submission.
   
2. **auth.py**: The `auth.py` file is responsible for server-side authentication processes. It handles user login, registration, and authentication using Python.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to suit the project's requirements.
   - Include the `validator.js` file in your HTML pages using the `<script>` tag to enable client-side validation.

2. **auth.py**:
   - Utilize the functions defined in `auth.py` for user authentication tasks.
   - Integrate the authentication logic with your backend server to secure user access to the application.

Ensure that both client-side and server-side authentication processes are synchronized to provide a seamless user experience and maintain security standards.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the format of a password (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates the format of a username (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** This file can be imported as a module to perform input validation tasks in user authentication processes.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password()`: Method to hash a password using SHA-256.
- `register_user()`: Method to register a new user with a unique username, email, and password.
- `login()`: Method to authenticate a user with a username and password and generate a session token.
- `logout()`: Method to end a user's session by invalidating the session token.
- `is_authenticated()`: Method to check if a session token is valid and the user is authenticated.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in the provided code snippet).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints (not used in the provided code snippet).

---
*Auto-generated documentation - Last updated: 2025-07-17 19:29:20*
