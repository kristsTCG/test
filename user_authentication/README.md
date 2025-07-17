# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This JavaScript file contains logic for validating user input related to authentication. It plays a crucial role in ensuring that user data meets the required criteria for authentication.
  
- **auth.py**: The Python file `auth.py` is responsible for handling authentication processes within the project. It manages user login, registration, and authentication tasks.

## Usage
To work with the code in this folder:
1. Review the `validator.js` file to understand the validation logic for user input.
2. Explore the `auth.py` file to grasp the authentication processes implemented in Python.
3. Use the functions and methods defined in these files to integrate user authentication features into the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates an email address using a regular expression.
- `validatePassword(password)`: Validates a password based on specific criteria.
- `validateUsername(username)`: Validates a username for length and character restrictions.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class where input validation is needed:
```javascript
const InputValidator = require('./validator.js');

const email = 'test@example.com';
if (InputValidator.validateEmail(email)) {
    console.log('Email is valid');
}

const password = 'SecurePass123!';
if (InputValidator.validatePassword(password)) {
    console.log('Password is valid');
}

const username = 'user_123';
if (InputValidator.validateUsername(username)) {
    console.log('Username is valid');
}

const passwordStrength = InputValidator.getPasswordStrength(password);
console.log('Password strength:', passwordStrength);
```

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and has not expired.

**Usage:** Instantiate the `UserAuth` class to utilize user authentication functionalities like registration, login, session management, and authentication.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with date and time information.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 16:50:29*
