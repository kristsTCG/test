# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files, `validator.js` for client-side validation written in JavaScript and `auth.py` for server-side authentication written in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic for user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before submission.
- **auth.py**: The `auth.py` file handles server-side authentication processes. It manages user authentication, login, and session handling on the server side.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to match the project's requirements.
   - Include the `validator.js` file in your HTML pages using `<script>` tags.
   - Call the validation functions from your form submission logic to validate user input.

2. **auth.py**:
   - Implement additional authentication logic as required by the project.
   - Integrate the authentication functionality into your server-side codebase.
   - Ensure proper error handling and security measures are in place to protect user data.

By following the guidelines above, you can effectively utilize the user authentication functionality provided in the `user_authentication` folder of the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength and format of a password.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Determines the strength level of a password based on length and character requirements.

**Usage:** Import `InputValidator` class from this file to use the provided validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user's session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and not expired.

**Usage:** Instantiate `UserAuth` to utilize user authentication functionalities like registration, login, logout, and session validation.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 00:49:10*
