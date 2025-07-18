# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` for client-side input validation in JavaScript and `auth.py` for server-side authentication logic in Python.

## Key Files
1. `validator.js`: This JavaScript file is responsible for validating user input on the client-side. It contains functions to ensure that user input meets specified criteria before submission.
   
2. `auth.py`: The Python file `auth.py` handles server-side authentication processes. It includes functions for user login, registration, and authentication checks.

## Usage
1. To utilize the client-side input validation, refer to the functions defined in `validator.js`. Integrate these functions into your frontend code to validate user input before sending it to the server.

2. For server-side authentication tasks, utilize the functions provided in `auth.py`. These functions can be called within your backend code to handle user login, registration, and authentication processes effectively.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates that a password meets the criteria of being at least 8 characters long with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates that a username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on its length and character composition.

**Usage:** This file can be imported as a module in other JavaScript files to perform input validation tasks related to user authentication.

**Dependencies:** No external dependencies are required for this file.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user's session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing functions.
- `json`: For JSON serialization and deserialization.
- `datetime`: For working with dates and times.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 09:24:36*
