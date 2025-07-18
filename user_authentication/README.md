# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` for client-side input validation in JavaScript and `auth.py` for server-side authentication logic in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic written in JavaScript. It ensures that user input meets specified criteria before submission.
- **auth.py**: The `auth.py` file contains server-side authentication code written in Python. It handles user authentication processes such as login, registration, and session management.

## Usage
1. **validator.js**:
   - To use the client-side validation logic, include `validator.js` in your HTML file using a script tag.
   - Call the validation functions provided in `validator.js` on user input fields to ensure data integrity.

2. **auth.py**:
   - Import `auth.py` in your Python project to utilize the authentication functionalities.
   - Use the functions defined in `auth.py` to handle user authentication tasks such as login, registration, and managing user sessions.

Ensure that both client-side and server-side authentication components work together seamlessly to provide a secure user authentication experience in the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates an email address based on a regex pattern.
- `validatePassword(password)`: Validates a password based on length and complexity requirements.
- `validateUsername(username)`: Validates a username based on length and allowed characters.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class in your code and call the respective validation functions as needed.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** User authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
  - `logout(session_token: str) -> bool`: Ends a user session based on the session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Instantiate `UserAuth` to utilize user registration, login, logout, and session validation functionalities.

**Dependencies:**
- `hashlib`: Provides hashing algorithms for secure password storage.
- `json`: Used for JSON serialization and deserialization.
- `datetime`: Handles date and time operations.
- `timedelta`: Represents a duration of time.

---
*Auto-generated documentation - Last updated: 2025-07-18 02:21:40*
