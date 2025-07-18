# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks. It contains validator.js for client-side input validation and auth.py for server-side authentication logic.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation logic for user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before submission.
  
- **auth.py**: This Python file is responsible for server-side authentication processes. It manages user authentication, including login, registration, and session management.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to suit the project's requirements.
   - Include the script in your HTML files to enable client-side validation.

2. **auth.py**:
   - Integrate the authentication logic into your server-side codebase.
   - Utilize the provided functions for user registration, login, and session management.

Ensure that both client-side and server-side components work together seamlessly to provide a secure and user-friendly authentication experience.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Determines the strength level of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class where input validation is required.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: Used for hashing passwords.
- `json`: Not used in this file but imported.
- `datetime`: Used for handling date and time operations.
- `timedelta`: Used for calculating expiration time for session tokens.
- `typing`: Used for type hints in function definitions.

---
*Auto-generated documentation - Last updated: 2025-07-18 01:59:15*
