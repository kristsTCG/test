# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes validator.js for client-side input validation and auth.py for server-side authentication logic.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation functions to ensure that user input meets specified criteria before submission.
- **auth.py**: This Python file handles server-side authentication processes, such as verifying user credentials and generating access tokens.

## Usage
1. **validator.js**: To use the validation functions in this file, include it in your HTML file using a script tag. You can then call the validation functions as needed to validate user input before form submission.
   
   Example:
   ```html
   <script src="validator.js"></script>
   <script>
       // Call validation functions here
   </script>
   ```

2. **auth.py**: Incorporate the authentication logic from this file into your server-side code to manage user authentication. You can import and use the functions provided in `auth.py` to authenticate users and handle access control.

   Example:
   ```python
   from auth import authenticate_user

   # Call the authenticate_user function to verify user credentials
   ```

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of being at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is between 3 to 20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on its length and the presence of lowercase, uppercase, numbers, and special characters.

**Usage:** This file can be imported into other JavaScript files using `require` or `import` statements to perform input validation for user authentication processes.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file provides a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 16:16:21*
