# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This functionality is crucial for managing user access and security.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes validator.js for client-side validation written in JavaScript and auth.py for server-side authentication logic written in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic for user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before being submitted to the server.
  
- **auth.py**: The `auth.py` file is responsible for server-side authentication processes. It manages user authentication, login, and authorization within the application.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to match the project's requirements.
   - Include the `validator.js` file in your HTML templates using the `<script>` tag.
   - Call the validation functions from your form submission logic to validate user input.

2. **auth.py**:
   - Integrate the authentication logic with your application's backend.
   - Customize the authentication methods to align with your specific user authentication requirements.
   - Ensure proper error handling and security measures are in place to protect user data.

By following the guidelines above, you can effectively utilize the user authentication functionality provided in the `user_authentication` folder for your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long, alphanumeric, and allows underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, logout, and session authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations within your application.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hinting in Python code.

---
*Auto-generated documentation - Last updated: 2025-07-17 20:05:56*
