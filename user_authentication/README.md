# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This module handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes validator.js for client-side validation and auth.py for server-side authentication.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation logic for user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before submission.
  
- **auth.py**: The Python file `auth.py` is responsible for server-side authentication processes. It manages user authentication, login, and session handling within the application.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to suit the project requirements.
   - Include the `validator.js` file in your HTML templates using `<script>` tags.
   - Call the validation functions from your form submission events to validate user input.

2. **auth.py**:
   - Implement additional authentication logic as required by the project.
   - Integrate the authentication functionality into your server-side application logic.
   - Ensure proper error handling and secure authentication practices are followed.

By following the guidelines above, you can effectively utilize the user authentication features provided in this folder for your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on its length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file provides a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session based on the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with date and time.
- `timedelta`: For calculating time differences.
- `typing`: For type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-17 21:51:39*
