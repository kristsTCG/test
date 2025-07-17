# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. These files handle user validation and authentication processes.

## Structure
The folder `user_authentication` contains two key files:
- `validator.js`: A JavaScript file with 1212 characters that handles user input validation.
- `auth.py`: A Python file with 2198 characters responsible for user authentication processes.

## Key Files
### validator.js
- **Purpose**: Handles user input validation.
- **Character Count**: 1212
- **Role**: Ensures that user input meets specified criteria before processing.

### auth.py
- **Purpose**: Manages user authentication processes.
- **Character Count**: 2198
- **Role**: Handles user login, registration, and authentication tasks.

## Usage
1. To use the `validator.js` file:
   - Ensure the file is imported into the relevant JavaScript file.
   - Call the validation functions provided within `validator.js` to validate user input.

2. To work with `auth.py`:
   - Import the file into your Python script.
   - Utilize the functions within `auth.py` for user authentication tasks such as login, registration, and authentication.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as checking password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength and format of a password.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the provided validation functions in your authentication logic.

**Dependencies:** No external dependencies required.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user's session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your Python application.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 14:27:09*
