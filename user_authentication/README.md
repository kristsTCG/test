# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. These files handle user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes validator.js for client-side validation written in JavaScript and auth.py for server-side authentication written in Python.

## Key Files
1. **validator.js**: This file contains client-side validation logic for user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before submission.
   
2. **auth.py**: The `auth.py` file is responsible for server-side authentication processes. It manages user authentication, login, and session handling on the server side.

## Usage
To utilize the functionalities provided in this folder:
- Use `validator.js` for client-side validation by including it in your HTML files and calling the validation functions as needed.
- Incorporate `auth.py` into your server-side code to handle user authentication tasks such as login validation and session management.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class in your code:
```javascript
const InputValidator = require('./validator.js');
```
Then, you can call the validation functions and password strength assessment function as needed.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with username and password and generate a session token.
- `logout`: Method to end a user session based on the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-17 19:56:42*
