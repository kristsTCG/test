# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This functionality is crucial for managing user access and security.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes validator.js for client-side validation and auth.py for server-side authentication logic.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation functions to ensure that user input meets specified criteria before submitting it for authentication.
- **auth.py**: The Python file auth.py implements server-side authentication logic, including user login, registration, and password management.

## Usage
1. **validator.js**: Use the functions in this file to validate user input on the client side before sending it for authentication. Import and call these functions in your front-end scripts to enhance user experience and prevent invalid data submission.
   
2. **auth.py**: Utilize the functions in this Python file to handle user authentication on the server side. Implement login, registration, and password management functionalities by importing and using the defined methods in your backend scripts.

Ensure to maintain the integrity of user authentication processes by following best practices and security measures outlined in the code files.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on its length and character composition.

**Usage:** This file can be imported as a module in other JavaScript files to perform input validation for user authentication.

**Dependencies:** No external dependencies are required for this file.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 21:36:37*
