# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes the following key components:
- `validator.js`: A JavaScript file containing functions for validating user input.
- `auth.py`: A Python file responsible for handling user authentication processes.

## Key Files
### validator.js
- **Role**: Contains functions for validating user input.
- **Size**: 1212 characters
- **Usage**: Ensures that user-provided data meets specified criteria before processing.

### auth.py
- **Role**: Manages user authentication processes.
- **Size**: 2198 characters
- **Usage**: Handles user login, registration, and authentication tasks.

## Usage
1. Use `validator.js` to validate user input by calling the appropriate functions within your JavaScript code.
2. Utilize `auth.py` for user authentication tasks such as login, registration, and authentication processes.
3. Ensure to integrate these files into your project's user authentication flow for secure and reliable user interactions.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3 to 20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: Used for hashing passwords.
- `json`: Not used in this file but imported.
- `datetime`: Used for handling date and time operations.
- `timedelta`: Used for calculating expiration time for session tokens.
- `typing`: Used for type hints in function definitions.

---
*Auto-generated documentation - Last updated: 2025-07-18 02:18:32*
