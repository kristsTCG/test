# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` for client-side input validation using JavaScript and `auth.py` for server-side authentication using Python.

## Key Files
1. **validator.js**
   - Role: Handles client-side input validation.
   - Size: 1212 characters
   - Language: JavaScript

2. **auth.py**
   - Role: Manages server-side authentication logic.
   - Size: 2198 characters
   - Language: Python

## Usage
1. **validator.js**:
   - Ensure the file is included in the appropriate HTML file using `<script src="validator.js"></script>`.
   - Modify the validation rules as needed to suit the project requirements.
   - Use functions provided in `validator.js` to validate user input on the client-side.

2. **auth.py**:
   - Integrate the authentication logic into the server-side codebase.
   - Utilize the functions in `auth.py` to authenticate users securely.
   - Customize the authentication process based on the project's authentication requirements.

By following the guidelines above, developers can effectively implement user authentication features using the code in the `user_authentication` folder.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a correct format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters, alphanumeric, and underscores only.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password()`: Method to hash a password using SHA-256.
- `register_user()`: Method to register a new user with a unique username, email, and password.
- `login()`: Method to authenticate a user with a username and password and generate a session token.
- `logout()`: Method to end a user session by invalidating the session token.
- `is_authenticated()`: Method to check if a session token is valid and not expired.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing functions.
- `json`: For JSON serialization and deserialization.
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 00:57:34*
