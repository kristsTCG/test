# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript for input validation and `auth.py` written in Python for authentication logic.

## Key Files
1. `validator.js`: This file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria before proceeding with authentication processes.
   
2. `auth.py`: This file is responsible for handling user authentication logic. It manages user login, registration, and authentication processes within the system.

## Usage
To work with the code in this folder:
- Use `validator.js` functions to validate user input data before processing authentication.
- Utilize `auth.py` methods for implementing user authentication functionalities in the project.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates if a password meets complexity requirements (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates if a username meets length and character requirements (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Determines the strength level of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: Used for hashing passwords.
- `json`: Used for JSON serialization and deserialization.
- `datetime`: Used for handling date and time operations.
- `timedelta`: Used for calculating time differences.
- `typing`: Used for type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 09:28:45*
