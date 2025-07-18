# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` for client-side input validation written in JavaScript and `auth.py` for server-side authentication logic written in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic to ensure that user input meets specified criteria before submission.
- **auth.py**: The `auth.py` file is responsible for server-side authentication processes, such as verifying user credentials and managing user sessions.

## Usage
1. To utilize the client-side validation provided by `validator.js`, include the script in your HTML file using `<script src="path/to/validator.js"></script>`. Then, call the appropriate validation functions on user input fields.
   
2. For server-side authentication functionalities, import and use the `auth.py` module in your Python backend code. Implement the necessary authentication logic based on your project requirements.

3. Ensure to maintain the integrity and security of user authentication processes by regularly updating and testing the code in this folder.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email follows a standard email format.
- `validatePassword(password)`: Validates if the input password meets specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates if the input username meets specific criteria (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the provided validation methods.

**Dependencies:** None

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash passwords using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user's session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and not expired.

**Usage:** Import `auth.py` and create an instance of `UserAuth` to utilize the user authentication functionalities.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-18 00:56:00*
