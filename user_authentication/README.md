# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes two key files: `validator.js` for client-side validation in JavaScript and `auth.py` for server-side authentication in Python.

## Key Files
1. **validator.js**: This JavaScript file contains client-side validation logic for user input. It ensures that user-provided data meets specified criteria before submission.
   
2. **auth.py**: The Python file `auth.py` is responsible for server-side authentication processes. It manages user login, registration, and authentication against the backend database.

## Usage
1. **validator.js**:
   - To use the client-side validation logic, include `validator.js` in your HTML file using a script tag.
   - Call the validation functions provided in `validator.js` on user input fields to validate user data before form submission.

2. **auth.py**:
   - Import `auth.py` in your Python project to utilize the authentication functionalities.
   - Use the functions defined in `auth.py` to handle user login, registration, and authentication processes.
   - Ensure proper configuration of the backend database connection for seamless authentication operations.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets complexity requirements.
- `validateUsername(username)`: Validates if the input username meets length and character requirements.
- `getPasswordStrength(password)`: Determines the strength level of the input password based on length and character types.

**Usage:** To use this file, import `InputValidator` class in your code and call the desired validation functions or password strength function as needed.

**Dependencies:** No external dependencies are required for this file.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password()`: Method to hash a password using SHA-256.
- `register_user()`: Method to register a new user with a unique username, email, and password.
- `login()`: Method to authenticate a user with a username and password and generate a session token.
- `logout()`: Method to end a user's session by invalidating the session token.
- `is_authenticated()`: Method to check if a session token is valid and the user is authenticated.

**Usage:** Instantiate the `UserAuth` class to use the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 18:29:06*
