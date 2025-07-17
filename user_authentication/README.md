# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript for input validation and `auth.py` written in Python for authentication processes.

## Key Files
- **validator.js**: This file is responsible for validating user input, ensuring that the data provided meets the required criteria. It plays a crucial role in maintaining data integrity and security.
  
- **auth.py**: The `auth.py` file handles user authentication processes such as login, logout, and session management. It is essential for verifying user identities and controlling access to protected resources.

## Usage
1. **validator.js**:
   - To use the validation functions in `validator.js`, import the file into your JavaScript code.
   - Call the appropriate validation functions provided in `validator.js` to validate user input before processing it further.

2. **auth.py**:
   - Import `auth.py` into your Python code to access the authentication functionalities.
   - Utilize the functions defined in `auth.py` for user login, logout, and session management.
   - Ensure proper error handling and security measures are implemented when integrating authentication features into your project.

By following the guidelines above, you can effectively leverage the user authentication capabilities provided in the `user_authentication` folder for your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3 to 20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-17 16:53:26*
