# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It includes validation logic in JavaScript and authentication logic in Python.

## Structure
The folder is organized to handle user authentication tasks. It contains two key files: `validator.js` for input validation and `auth.py` for user authentication.

## Key Files
- `validator.js`: This JavaScript file contains logic for validating user input. It plays a crucial role in ensuring that the data entered by users meets the required criteria.
- `auth.py`: This Python file handles user authentication processes such as login, registration, and session management. It is responsible for verifying user credentials and granting access to authorized users.

## Usage
1. To utilize the validation functionality provided by `validator.js`, import the file into your JavaScript code and call the appropriate validation functions as needed.
2. For user authentication tasks, import `auth.py` into your Python code and utilize the authentication methods to manage user login and registration processes.
3. Ensure to follow the documentation within each file for specific usage instructions and function parameters.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length and character requirements.
- `validateUsername(username)`: Validates the format of a username allowing alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and the presence of lowercase, uppercase, numbers, and special characters.

**Usage:** To use this file, import `InputValidator` class into your code and call the desired validation functions as needed.

```javascript
const InputValidator = require('./validator.js');

if (InputValidator.validateEmail('example@email.com')) {
    console.log('Email is valid');
}

if (InputValidator.validatePassword('StrongPass123!')) {
    console.log('Password meets requirements');
}

console.log(InputValidator.getPasswordStrength('Password123'));
```

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** User authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with username and password and generate a session token.
- `logout`: Method to end a user's session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate `UserAuth` to utilize user authentication features like registration, login, logout, and session validation.

**Dependencies:**
- `hashlib`: For hashing functions.
- `json`: For JSON serialization.
- `datetime`: For handling date and time.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 14:00:56*
