# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files, `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This JavaScript file contains functions for validating user input. It plays a crucial role in ensuring that user data meets specified criteria before proceeding with authentication processes.
  
- **auth.py**: The Python file `auth.py` is responsible for handling user authentication logic. It manages user login, registration, and authentication processes within the system.

## Usage
1. **validator.js**:
   - To use the functions in `validator.js`, import the file into your JavaScript project.
   - Call the validation functions as needed to validate user input before processing it further.
  
2. **auth.py**:
   - Import `auth.py` into your Python project to access the authentication functionalities.
   - Utilize the provided functions for user login, registration, and authentication processes within your application.

Ensure to follow the documentation within each file for specific usage instructions and parameters.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of being at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of a password based on its length and character composition.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication operations.
  - `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Method to register a new user.
  - `login(username: str, password: str) -> Optional[str]`: Method to authenticate a user and return a session token.
  - `logout(session_token: str) -> bool`: Method to end a user session.
  - `is_authenticated(session_token: str) -> bool`: Method to check if a session token is valid.

**Usage:** Instantiate `UserAuth` to manage user authentication operations. Call methods like `register_user`, `login`, `logout`, and `is_authenticated` as needed.

**Dependencies:** 
- `hashlib`: Used for hashing passwords.
- `json`: Not used in the provided code but imported.
- `datetime`: Used for working with dates and times.
- `timedelta`: Used for adding time intervals to `datetime`.

---
*Auto-generated documentation - Last updated: 2025-07-17 22:02:19*
