# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities in the project. It includes validation logic in JavaScript and authentication logic in Python.

## Structure
The folder is organized to handle user authentication processes. It contains two key files, `validator.js` for input validation and `auth.py` for user authentication.

## Key Files
- **validator.js**: This JavaScript file contains logic for validating user inputs. It plays a crucial role in ensuring that user-provided data meets the required criteria before proceeding with authentication processes.
- **auth.py**: The Python file `auth.py` is responsible for handling user authentication functionalities. It manages user login, registration, and authentication processes within the project.

## Usage
To work with the code in this folder:
1. Modify the `validator.js` file to customize input validation rules as per project requirements.
2. Utilize the `auth.py` file to integrate user authentication functionalities into the project.
3. Ensure proper integration of these files with other components that interact with user authentication processes.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specified criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on length and character requirements.

**Usage:** To use this file, import `InputValidator` class in your code and call the desired validation methods as needed.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and not expired.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: Used for hashing passwords.
- `json`: Not currently used but imported.
- `datetime`: Used for handling date and time operations.
- `timedelta`: Used for calculating expiration time for session tokens.
- `typing`: Used for type hinting in method signatures.

---
*Auto-generated documentation - Last updated: 2025-07-18 04:36:10*
