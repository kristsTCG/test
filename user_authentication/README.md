# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` for client-side input validation in JavaScript and `auth.py` for server-side authentication in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic written in JavaScript. It ensures that user input meets specified criteria before submitting to the server for authentication.
  
- **auth.py**: The `auth.py` file contains server-side authentication logic implemented in Python. It handles user authentication requests, verifies user credentials, and manages user sessions.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to suit the project requirements.
   - Include `validator.js` in your HTML files using `<script>` tags to enable client-side validation.

2. **auth.py**:
   - Implement additional authentication methods or customize the existing logic as per project needs.
   - Ensure proper integration of `auth.py` with other backend components for seamless user authentication.

By following the guidelines outlined in the key files, developers can effectively manage user authentication processes within the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength level of a password based on various criteria.

**Usage:** This file can be imported as a module to perform input validation functions for user authentication.

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

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing functions.
- `json`: For JSON serialization and deserialization.
- `datetime`: For date and time operations.
- `timedelta`: For time duration calculations.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 00:47:15*
