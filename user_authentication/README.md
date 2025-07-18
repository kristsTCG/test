# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files, `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. `validator.js`: This file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
   
2. `auth.py`: This Python file handles the authentication process for users. It includes functions for user login, registration, and other authentication-related tasks.

## Usage
To work with the code in this folder:
1. Use the functions in `validator.js` to validate user input data before processing it further.
2. Utilize the functions in `auth.py` to implement user authentication features such as login, registration, and password reset.
3. Ensure that the code in both files is integrated seamlessly with other parts of the project that require user authentication functionality.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of being at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** 
To use this file, import it in your code:
```javascript
const InputValidator = require('./validator.js');
```
Then, you can use the validation functions like:
```javascript
const isValidEmail = InputValidator.validateEmail('example@email.com');
const isValidPassword = InputValidator.validatePassword('StrongPassword123');
const isValidUsername = InputValidator.validateUsername('user_name123');
const passwordStrength = InputValidator.getPasswordStrength('GoodPassword123!');
```

**Dependencies:** None

## auth.py

**Purpose:** User authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates user and returns a session token.
  - `logout(session_token: str) -> bool`: Ends a user session.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session is valid.

**Usage:** Instantiate `UserAuth` to utilize user authentication functionalities.

**Dependencies:** `hashlib`, `json`, `datetime`, `timedelta`, `typing`.

---
*Auto-generated documentation - Last updated: 2025-07-18 00:02:55*
