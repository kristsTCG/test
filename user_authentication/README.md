# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` for client-side validation in JavaScript and `auth.py` for server-side authentication in Python.

## Key Files
- **validator.js**: This JavaScript file contains functions for validating user input on the client-side. It plays a crucial role in ensuring that user-provided data meets the required criteria before submitting it to the server.
  
- **auth.py**: The Python file `auth.py` handles server-side authentication processes. It manages user authentication, such as login, logout, and session management, to ensure secure access to the application.

## Usage
1. **validator.js**:
   - Modify the validation functions as needed to suit the specific input requirements of the project.
   - Include the `validator.js` file in your HTML pages using `<script src="path/to/validator.js"></script>`.

2. **auth.py**:
   - Implement the necessary authentication logic within the functions defined in `auth.py`.
   - Integrate the authentication functionality with other parts of the project that require user authentication.
   - Ensure proper error handling and security measures are in place to protect user data.

By following the guidelines above, you can effectively utilize the user authentication features provided in the `user_authentication` folder of the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username allowing only alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Determines the strength level of a password based on length and character complexity.

**Usage:** Import the `InputValidator` class from this file to use the provided validation methods in your authentication logic.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token if successful.
  - `logout(session_token: str) -> bool`: Ends a user session based on the provided session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and the user is authenticated.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: Used for hashing passwords.
- `json`: Used for JSON serialization and deserialization.
- `datetime`: Used for working with dates and times.
- `timedelta`: Used for calculating time differences.
- `typing`: Used for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 15:46:42*
