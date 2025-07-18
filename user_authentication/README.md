# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. These files handle user validation and authentication processes.

## Structure
The folder `user_authentication` contains two key files:
- `validator.js`: A JavaScript file with 1212 characters responsible for user input validation.
- `auth.py`: A Python file with 2198 characters handling user authentication processes.

## Key Files
### validator.js
- **Role**: Responsible for validating user input data.
- **Size**: 1212 characters
- **Language**: JavaScript

### auth.py
- **Role**: Handles user authentication processes.
- **Size**: 2198 characters
- **Language**: Python

## Usage
1. To utilize the user input validation functionality, refer to `validator.js`. Modify the validation rules as needed to suit the project requirements.
2. For user authentication processes, interact with `auth.py`. Implement login, registration, and authentication logic based on the project specifications.

Ensure to maintain the integrity and security of user data throughout the authentication processes.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including validating email, password, and username formats, as well as checking password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** This file can be imported into other JavaScript files using `require` or `import` statements to utilize the input validation functions provided.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 02:38:17*
