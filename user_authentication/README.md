# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It focuses on validating user input and handling authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` for client-side validation written in JavaScript and `auth.py` for server-side authentication written in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic for user input. It ensures that user-provided data meets the required criteria before submitting it for authentication.
  
- **auth.py**: The `auth.py` file is responsible for server-side authentication processes. It manages user login, registration, and authentication using Python. This file interacts with the database to verify user credentials and grant access.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to match the project's requirements.
   - Include the `validator.js` file in your HTML templates using `<script>` tags.
   - Call the validation functions from your form submission logic to validate user input before sending it to the server.

2. **auth.py**:
   - Configure the database connection settings in `auth.py` to match your database setup.
   - Implement additional authentication logic such as password hashing and token generation if required.
   - Integrate the authentication endpoints provided in `auth.py` with your project's routing mechanism.

Ensure to test the user authentication functionalities thoroughly to guarantee secure and reliable user interactions.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username to be alphanumeric with underscores and within a specific length range.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Method to register a new user.
- `login(username: str, password: str) -> Optional[str]`: Method to authenticate a user and return a session token.
- `logout(session_token: str) -> bool`: Method to end a user session.
- `is_authenticated(session_token: str) -> bool`: Method to check if a session is valid.

**Usage:** Instantiate `UserAuth` to manage user authentication. Call `register_user` to register a new user, `login` to authenticate and get a session token, `logout` to end a session, and `is_authenticated` to check session validity.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization.
- `datetime`: For handling date and time.
- `timedelta`: For calculating time differences.
- `typing`: For type hinting.

---
*Auto-generated documentation - Last updated: 2025-07-17 14:44:16*
