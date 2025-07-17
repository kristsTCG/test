# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized with two key files: `validator.js` written in JavaScript and `auth.py` written in Python. These files handle user input validation and authentication logic respectively.

## Key Files
- `validator.js`: This file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria before proceeding with authentication.
- `auth.py`: The `auth.py` file is responsible for handling user authentication processes. It manages user login, registration, and authentication logic within the system.

## Usage
1. To utilize the validation functions provided in `validator.js`, import the necessary functions into your JavaScript files and call them as needed to validate user input data.
2. For user authentication functionalities, import and utilize the methods defined in `auth.py` within your Python scripts. These methods can be used for user login, registration, and authentication processes.

Ensure that you follow the specific usage instructions and guidelines provided within each file to integrate user authentication features seamlessly into your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long, alphanumeric, and contains underscores only.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file and use its static methods for input validation and password strength assessment.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
  - `logout(session_token: str) -> bool`: Ends a user session based on the provided session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Instantiate `UserAuth` to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: Used for hashing passwords.
- `json`: Used for JSON operations.
- `datetime`: Used for working with dates and times.
- `timedelta`: Used for representing a duration of time.
- `typing`: Used for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 17:04:12*
