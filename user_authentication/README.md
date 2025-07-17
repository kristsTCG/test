# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It consists of two key files, `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. `validator.js`: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria before proceeding with authentication processes.
   
2. `auth.py`: The Python file `auth.py` is responsible for handling user authentication logic. It manages user login, registration, and authentication processes within the application.

## Usage
To utilize the functionalities provided in the `user_authentication` folder:
- Review the `validator.js` file for validation functions and ensure proper input validation in your application.
- Utilize the `auth.py` file to implement user authentication features such as login, registration, and authentication in your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length and character requirements.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Determines the strength level of a password based on various criteria.

**Usage:** To use this file, import `InputValidator` class in your code and call the validation functions as needed.

```javascript
const InputValidator = require('./validator.js');

if (InputValidator.validateEmail('example@email.com')) {
    console.log('Email is valid');
}

console.log(InputValidator.getPasswordStrength('StrongPassword123'));
```

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
  - `logout(session_token: str) -> bool`: Ends a user session based on the session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Instantiate `UserAuth` to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: Used for hashing passwords.
- `json`: Not used in the provided code but imported.
- `datetime`: Used for working with dates and times.
- `timedelta`: Used for calculating time differences.
- `typing`: Used for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 19:14:16*
