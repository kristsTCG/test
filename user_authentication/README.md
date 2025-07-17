# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It includes a JavaScript file for validation logic and a Python file for handling authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes validator.js for client-side validation and auth.py for server-side authentication.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation logic for user input. It plays a crucial role in ensuring data integrity before submitting to the server.
- **auth.py**: The Python file `auth.py` is responsible for server-side authentication processes. It manages user login, registration, and authentication tasks.

## Usage
1. **validator.js**: To use the validation logic in `validator.js`, include the file in your HTML document using a script tag. You can then call the validation functions defined in this file to validate user input before submitting forms.
   
   Example:
   ```html
   <script src="validator.js"></script>
   <script>
       // Call validation functions here
   </script>
   ```

2. **auth.py**: To utilize the authentication functionalities provided by `auth.py`, import the file in your Python project. You can then use the functions defined in this file to handle user authentication tasks such as login, registration, and token generation.

   Example:
   ```python
   from auth import login, register, generate_token
   # Use the functions for authentication tasks
   ```

Ensure proper integration of these files in your project to enhance user authentication security and functionality.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates an email address based on a regular expression pattern.
- `validatePassword(password)`: Validates a password based on specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates a username based on specific criteria (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** This file can be imported as a module in other JavaScript files using `require` or `import` statements, and then the functions can be called as needed for input validation.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user's session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication processes. Call the methods within the class to register users, authenticate logins, manage sessions, and check authentication status.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-17 22:34:40*
