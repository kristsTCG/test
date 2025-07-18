# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files, `validator.js` for client-side input validation written in JavaScript and `auth.py` for server-side authentication logic written in Python.

## Key Files
1. `validator.js`: This file contains client-side input validation logic to ensure that user input meets specified criteria before submission. It plays a crucial role in enhancing data integrity and security.
   
2. `auth.py`: The `auth.py` file is responsible for server-side authentication processes. It manages user authentication, such as login, logout, and session management. This file is essential for securing user accounts and controlling access to protected resources.

## Usage
1. To utilize the client-side input validation, refer to the `validator.js` file. Customize the validation rules according to your project requirements by modifying the JavaScript functions.
   
2. For server-side authentication functionalities, interact with the `auth.py` file. Implement login and logout mechanisms, handle user sessions, and enforce access control based on the provided authentication logic.

Ensure to integrate these files seamlessly into your project to establish a robust user authentication system.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric and underscores within a specific length range.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** This file can be imported as a module to perform input validation tasks in user authentication processes.

**Dependencies:** None

## auth.py

**Purpose:** This file provides a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by deleting the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: Used for hashing passwords.
- `json`: Not currently used but imported.
- `datetime`: Used for handling date and time operations.
- `timedelta`: Used for calculating expiration time for session tokens.
- `typing`: Used for type hints in function definitions.

---
*Auto-generated documentation - Last updated: 2025-07-18 03:09:40*
