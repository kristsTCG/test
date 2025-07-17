# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This module handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes validator.js for client-side validation and auth.py for server-side authentication logic.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation functions for ensuring user input meets specified criteria. It plays a crucial role in enhancing user experience by providing real-time feedback on form inputs.
  
- **auth.py**: The Python file `auth.py` is responsible for server-side authentication processes. It manages user login, registration, and authentication using secure protocols. This file is essential for ensuring the security and integrity of user accounts.

## Usage
To utilize the user authentication functionality provided in this folder, follow these steps:
1. Use the functions defined in `validator.js` to validate user inputs on the client side before submitting forms.
2. Implement the authentication logic from `auth.py` on the server side to handle user login, registration, and authentication processes securely.
3. Ensure that both client-side and server-side validation mechanisms are in sync to provide a seamless and secure user authentication experience.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username allowing alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class where input validation is needed.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and not expired.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization and deserialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 18:23:19*
