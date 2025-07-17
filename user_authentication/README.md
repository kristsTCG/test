# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. These files handle user validation and authentication processes.

## Structure
The folder is organized to manage user authentication operations efficiently. It includes validator.js for client-side validation and auth.py for server-side authentication logic.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation functions for user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before submission.
  
- **auth.py**: The Python file `auth.py` is responsible for server-side authentication processes. It manages user authentication, login, and access control within the application.

## Usage
1. **validator.js**:
   - Modify the validation functions to suit the specific requirements of the project.
   - Include the `validator.js` file in your HTML pages using `<script src="path/to/validator.js"></script>`.

2. **auth.py**:
   - Implement additional authentication logic as needed.
   - Integrate the authentication functionalities provided in `auth.py` with your application's backend services.

By following the instructions above, you can effectively utilize the user authentication features provided in the `user_authentication` folder.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as checking password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric and underscore characters.
- `getPasswordStrength(password)`: Determines the strength level of a password based on various criteria.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
  - `logout(session_token: str) -> bool`: Ends a user session based on the session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Create an instance of `UserAuth` to handle user authentication operations. Call `register_user` to register a new user, `login` to authenticate and generate a session token, `logout` to end a session, and `is_authenticated` to check session validity.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization.
- `datetime`: For date and time operations.
- `timedelta`: For calculating expiration time of sessions.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 16:18:21*
