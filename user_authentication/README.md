# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. These files handle user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. **validator.js**: This file contains JavaScript code for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
   
2. **auth.py**: The `auth.py` file is written in Python and is responsible for handling user authentication processes. It manages user login, registration, and authentication logic within the application.

## Usage
To utilize the functionalities provided in the `user_authentication` folder, follow these steps:
1. Review the code in `validator.js` to understand the validation criteria for user input data.
2. Explore the `auth.py` file to comprehend the user authentication processes implemented in Python.
3. Integrate the validation and authentication logic into your project as needed, ensuring proper error handling and security measures are in place.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username allowing alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password and returns a descriptive level.

**Usage:** Import the `InputValidator` class from this file to use the validation methods in your authentication logic.

**Dependencies:** No notable dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and generates a session token for active sessions.
  - `logout(session_token: str) -> bool`: Ends a user session by removing the session token from active sessions.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and not expired.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations. Call the methods within the class to register users, authenticate logins, manage sessions, and check authentication status.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing.Optional`: For type hinting.

---
*Auto-generated documentation - Last updated: 2025-07-17 21:10:40*
