# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. These files handle user validation and authentication processes.

## Structure
The folder is organized to manage user authentication features efficiently. It includes validator.js for client-side validation written in JavaScript and auth.py for server-side authentication written in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic for user input. It helps ensure that user-provided data meets the required criteria before submission.
- **auth.py**: The `auth.py` file is responsible for server-side authentication processes. It manages user authentication, login, and session handling within the application.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to suit the project's requirements.
   - Include the `validator.js` file in your HTML pages using `<script src="path/to/validator.js"></script>`.

2. **auth.py**:
   - Implement additional authentication logic as required by the project.
   - Integrate the authentication functionality into your server-side codebase.
   - Ensure proper handling of user sessions and authentication tokens.

By following the guidelines above, you can effectively utilize the user authentication features provided in this folder for your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password()`: Method to hash a password using SHA-256.
- `register_user()`: Method to register a new user with a unique username, email, and password.
- `login()`: Method to authenticate a user with a username and password and generate a session token.
- `logout()`: Method to end a user's session by invalidating the session token.
- `is_authenticated()`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 23:44:15*
