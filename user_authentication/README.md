# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` written in JavaScript for client-side validation and `auth.py` written in Python for server-side authentication.

## Key Files
- **validator.js**: This file contains client-side validation logic for user inputs. It ensures that user data meets specified criteria before submission.
- **auth.py**: The `auth.py` file handles server-side authentication processes. It manages user login, registration, and authentication against stored credentials.

## Usage
1. **validator.js**:
   - Modify the validation rules in this file to suit the project's requirements.
   - Include this script in your HTML files to enable client-side validation.

2. **auth.py**:
   - Use the functions in this file to implement user authentication features.
   - Integrate these authentication processes with your backend server logic for secure user access.

Ensure to test the functionality of both files thoroughly to maintain a secure and user-friendly authentication system.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file and use its static methods for input validation and password strength evaluation.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality. It allows users to register, login, logout, and check authentication status.

**Key Components:**
- `UserAuth`: Class that manages user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user's session by providing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON operations.
- `datetime`: For handling date and time.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 09:09:02*
