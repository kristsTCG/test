# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` for client-side input validation in JavaScript and `auth.py` for server-side authentication logic in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic written in JavaScript. It plays a crucial role in ensuring that user input is valid before submitting it to the server for authentication.
  
- **auth.py**: The `auth.py` file contains server-side authentication logic written in Python. It handles user authentication processes, such as verifying user credentials and generating authentication tokens.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to suit the project requirements.
   - Include the `validator.js` file in your HTML pages using `<script>` tags.
   - Call the validation functions defined in `validator.js` on user input fields to validate user input.

2. **auth.py**:
   - Implement additional authentication logic as required by the project.
   - Integrate the authentication functions from `auth.py` into your server-side codebase to handle user authentication processes.
   - Ensure proper error handling and security measures are in place to protect user data during authentication.

By following the guidelines above, you can effectively utilize the user authentication functionalities provided in the `user_authentication` folder of the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validation of email, password, and username formats, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates if the input email address is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3 to 20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on its length and character types.

**Usage:** This file can be imported using `require` or `import` statements in other JavaScript files to perform input validation for user authentication.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** User authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user authentication operations.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Register a new user with username, email, and password.
- `login(username: str, password: str) -> Optional[str]`: Authenticate user and return a session token.
- `logout(session_token: str) -> bool`: End a user session.
- `is_authenticated(session_token: str) -> bool`: Check if a session token is valid.

**Usage:** Instantiate `UserAuth` to manage user authentication. Call `register_user` to add a new user, `login` to authenticate and get a session token, `logout` to end a session, and `is_authenticated` to check if a session is valid.

**Dependencies:** `hashlib`, `json`, `datetime`, `timedelta`, `Optional`, `Dict` from `typing`.

---
*Auto-generated documentation - Last updated: 2025-07-18 06:40:50*
