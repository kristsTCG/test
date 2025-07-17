# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files, `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
  
- **auth.py**: The Python file `auth.py` is responsible for handling the authentication process. It includes functions for user login, registration, and other authentication-related tasks.

## Usage
To utilize the functionalities provided in this folder:
1. Review the `validator.js` file for validation logic and ensure it aligns with the project's requirements.
2. Explore the `auth.py` file to understand the authentication process flow and customize it as needed for the project.
3. Integrate the validation and authentication functionalities into the project's user management system as per the project's requirements.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long, alphanumeric, and contains underscores only.
- `getPasswordStrength(password)`: Determines the strength of the input password based on length and character types.

**Usage:** To use this file, import it into your project where input validation is needed:
```javascript
const InputValidator = require('./validator.js');
```

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
  - `logout(session_token: str) -> bool`: Ends a user session.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Instantiate `UserAuth` to manage user authentication operations. Call `register_user` to register a new user, `login` to authenticate and get a session token, `logout` to end a session, and `is_authenticated` to check session validity.

**Dependencies:** `hashlib`, `json`, `datetime`, `timedelta`, `Optional`, `Dict`

---
*Auto-generated documentation - Last updated: 2025-07-17 17:34:40*
