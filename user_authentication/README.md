# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication features. It includes validator.js for client-side validation and auth.py for server-side authentication.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation logic for user inputs. It ensures that user-provided data meets specified criteria before submitting to the server.
  
- **auth.py**: This Python file is responsible for server-side authentication. It manages user login, registration, and authentication processes using secure methods.

## Usage
1. **validator.js**:
   - Modify validation rules as needed by updating the logic in this file.
   - Include this file in your HTML pages to enable client-side validation for user inputs.

2. **auth.py**:
   - Integrate the authentication functionalities provided in this file with your server-side code.
   - Use the defined functions for user registration, login, and authentication within your application.

Ensure to handle user authentication securely to protect user data and maintain system integrity.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** This file can be imported as a module in other JavaScript files to perform input validation tasks for user authentication.

**Dependencies:** No external dependencies are required for this file.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, logout, and session validation.
- `hash_password`: Method to hash passwords using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user's session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Import the `UserAuth` class from this file to implement user authentication in your Python application.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For adding time intervals to dates.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 08:06:24*
