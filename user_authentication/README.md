# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities in the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized with two key files:
- `validator.js`: A JavaScript file with 1212 characters, responsible for validating user input.
- `auth.py`: A Python file with 2198 characters, handling user authentication processes.

## Key Files
### validator.js
This file is crucial for ensuring that user input meets the required criteria. It contains functions for validating user data before processing it further.

### auth.py
The `auth.py` file is essential for managing user authentication within the project. It handles processes such as user login, registration, and authentication checks.

## Usage
1. To utilize the validation functions in `validator.js`, import the file into your JavaScript code and call the appropriate validation functions as needed.
2. For user authentication processes, import `auth.py` into your Python code and utilize its functions for user login, registration, and authentication checks.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file and use its static methods for input validation.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user's session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization and deserialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 21:27:56*
