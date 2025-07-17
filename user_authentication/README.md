# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. These files handle user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes two key files, `validator.js` and `auth.py`, which are responsible for validating user input and handling authentication logic, respectively.

## Key Files
1. **validator.js**
   - Type: JavaScript
   - Size: 1212 characters
   - Role: This file contains functions to validate user input data, ensuring that the data meets the required criteria before proceeding with authentication processes.

2. **auth.py**
   - Type: Python
   - Size: 2198 characters
   - Role: The `auth.py` file implements the authentication logic for users. It handles user login, registration, and authentication processes within the system.

## Usage
1. **validator.js**:
   - To use the validation functions in `validator.js`, import the file into your JavaScript code.
   - Call the appropriate validation functions provided in `validator.js` to validate user input data before processing it further.

2. **auth.py**:
   - Import `auth.py` into your Python code to access the authentication functionalities.
   - Utilize the functions defined in `auth.py` for user registration, login, and authentication processes as needed in your project.

Ensure that you understand the roles of each file in the `user_authentication` folder to effectively implement user authentication features in your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long, alphanumeric, and contains underscores only.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class in your code. You can then call the validation functions and password strength assessment method as needed.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and hashed password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token for active sessions.
  - `logout(session_token: str) -> bool`: Ends a user session based on the provided session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and active.

**Usage:** Import the `UserAuth` class from this file to manage user authentication in your Python application.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization and deserialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 19:25:12*
