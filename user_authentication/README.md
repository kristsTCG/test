# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This module handles user validation and authentication processes.

## Structure
The folder is organized to centralize all user authentication-related code. It includes two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. `validator.js`: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
   
2. `auth.py`: The Python file `auth.py` is responsible for handling user authentication processes. It manages user login, registration, and authentication logic within the project.

## Usage
To utilize the user authentication functionality provided in this folder, developers can refer to the respective files for implementing user validation and authentication processes. Ensure to integrate these files into the project's authentication flow for secure user interactions.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on various criteria.

**Usage:** To use this file, import `InputValidator` class in your code and call the desired validation methods.

```javascript
const InputValidator = require('./validator.js');

if (InputValidator.validateEmail('example@email.com')) {
    console.log('Email is valid');
}

console.log(InputValidator.getPasswordStrength('StrongPassword123'));
```

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file provides a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
- `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token if successful.
- `logout(session_token: str) -> bool`: Ends a user session based on the provided session token.
- `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and the user is authenticated.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations. Call the methods to register users, log in, log out, and check authentication status.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing.Optional`: For type hinting the return value of login method.

---
*Auto-generated documentation - Last updated: 2025-07-17 15:09:26*
