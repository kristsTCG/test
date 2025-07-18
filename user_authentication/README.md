# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes validator.js for client-side input validation and auth.py for server-side authentication logic.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation logic for user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before submission.
- **auth.py**: The Python file auth.py is responsible for server-side authentication processes. It manages user authentication, login, and authorization within the application.

## Usage
1. To utilize the client-side validation provided by `validator.js`, include the file in your HTML document using a script tag.
2. Implement the server-side authentication logic by importing and using the functions defined in `auth.py` within your Python application.
3. Ensure to customize the authentication logic as per your project requirements and integrate it seamlessly with the rest of your application's functionality.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is between 3 to 20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types, returning a descriptive strength level.

**Usage:** This file can be imported using `require` or `import` statements to access the input validation functions.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** User authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
  - `logout(session_token: str) -> bool`: Ends a user session.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Instantiate `UserAuth` to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing functions.
- `json`: For JSON serialization/deserialization.
- `datetime`: For working with dates and times.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 04:21:44*
