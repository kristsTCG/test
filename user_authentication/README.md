# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains a JavaScript file for validation (`validator.js`) and a Python file for authentication (`auth.py`).

## Key Files
- `validator.js`: This JavaScript file contains functions for validating user input. It plays a crucial role in ensuring that user data meets the required criteria before authentication.
- `auth.py`: The Python file `auth.py` is responsible for handling user authentication processes. It manages user login, registration, and authentication within the system.

## Usage
To utilize the user authentication functionality provided in this folder, developers can refer to the `validator.js` file for input validation requirements. Additionally, they can interact with the `auth.py` file to implement user authentication processes such as login and registration. Ensure to follow the guidelines and functions defined in these files for seamless integration of user authentication features in the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character requirements.

**Usage:** Import `InputValidator` class from this file to use the provided validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
  - `logout(session_token: str) -> bool`: Ends a user session.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Instantiate `UserAuth` to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing functions.
- `json`: For JSON serialization/deserialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hinting.

---
*Auto-generated documentation - Last updated: 2025-07-17 18:44:29*
