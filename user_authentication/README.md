# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` for client-side input validation in JavaScript and `auth.py` for server-side authentication logic in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic written in JavaScript. It ensures that user input meets specified criteria before submission.
- **auth.py**: The `auth.py` file contains server-side authentication logic written in Python. It manages user authentication processes, such as login, registration, and password management.

## Usage
1. **validator.js**:
   - To use the validation functions in `validator.js`, include the file in your HTML document using a script tag.
   - Call the appropriate validation functions on user input fields to ensure data integrity before submission.

2. **auth.py**:
   - Import the `auth` module in your Python script to access authentication functionalities.
   - Utilize the provided functions for user login, registration, and password management within your server-side code.

Ensure proper integration of these files with your project's user authentication flow for secure and reliable authentication processes.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username allowing alphanumeric characters and underscores only.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class into your code and call the validation methods as needed.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, logout, and session validation.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your Python application.

**Dependencies:** 
- `hashlib` for hashing functions.
- `json` for JSON serialization.
- `datetime` for date and time operations.
- `timedelta` from `datetime` for time duration calculations.
- `typing.Optional` and `typing.Dict` for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 06:12:49*
