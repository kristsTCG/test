# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. These files handle user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes two key files: `validator.js` and `auth.py`.

## Key Files
- **validator.js**: This JavaScript file contains code for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
  
- **auth.py**: This Python file is responsible for handling user authentication processes. It manages user login, registration, and authentication using secure methods.

## Usage
To utilize the functionalities provided in this folder:
1. Review the code in `validator.js` to understand the validation logic and criteria.
2. Explore `auth.py` to implement user authentication processes in the project.
3. Integrate these files into the project's authentication system as needed.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username, allowing alphanumeric characters and underscores only.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session creation, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and not expired.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations like registration, login, and session management.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization and deserialization.
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 18:31:41*
