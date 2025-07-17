# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` for client-side input validation written in JavaScript and `auth.py` for server-side authentication logic written in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic to ensure that user input meets specified criteria before submitting it to the server. It plays a crucial role in maintaining data integrity and security.
- **auth.py**: The `auth.py` file is responsible for handling server-side authentication processes. It manages user login, registration, and authentication using Python. This file is essential for securing user accounts and controlling access to the application.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to match the project's requirements.
   - Include the `validator.js` file in your HTML pages using a script tag.
   - Call the validation functions from your form submission logic to validate user input before sending it to the server.

2. **auth.py**:
   - Implement additional authentication features such as password hashing, token generation, or two-factor authentication.
   - Integrate the authentication logic with your application's user management system.
   - Securely store sensitive information such as passwords and tokens to prevent unauthorized access.

By following the guidelines outlined in the key files, you can effectively manage user authentication within your project.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates an email address using a regular expression.
- `validatePassword(password)`: Validates a password based on specific criteria.
- `validateUsername(username)`: Validates a username for length and allowed characters.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
  - `hash_password(password: str) -> str`: Hashes the provided password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token if successful.
  - `logout(session_token: str) -> bool`: Ends a user session based on the provided session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and the user is authenticated.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your Python application.

**Dependencies:**
- `hashlib`: Used for hashing passwords.
- `json`: Used for JSON serialization (not used in the provided code but imported).
- `datetime`: Used for date and time operations.
- `timedelta`: Used for calculating expiration time for user sessions.
- `typing.Optional`: Used for type hinting in function definitions.
- `typing.Dict`: Used for type hinting in function definitions.

---
*Auto-generated documentation - Last updated: 2025-07-17 19:28:57*
