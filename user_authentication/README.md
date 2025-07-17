# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` written in JavaScript for input validation and `auth.py` written in Python for authentication logic.

## Key Files
1. `validator.js`: This file contains functions for validating user input such as email addresses, passwords, and other form data. It ensures that the data entered by users meets the required criteria before proceeding with authentication processes.

2. `auth.py`: This file is responsible for handling user authentication logic. It includes functions for user login, registration, password hashing, and session management. The authentication process is managed and executed through this Python script.

## Usage
1. To utilize the validation functions provided in `validator.js`, import the file into your JavaScript code and call the necessary functions to validate user input before processing it further.

2. For user authentication tasks, import `auth.py` into your Python code. Use the functions defined within this file to manage user login, registration, password handling, and session management within your application.

3. Ensure to follow the documentation within each file for specific function usage and parameters to effectively implement user authentication features in your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username, allowing alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types, returning a descriptive level.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
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
- `typing`: Used for type hinting.

---
*Auto-generated documentation - Last updated: 2025-07-17 23:44:39*
