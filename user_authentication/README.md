# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It consists of two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This JavaScript file contains functions for validating user input. It plays a crucial role in ensuring that user data meets specified criteria before proceeding with authentication processes.
- **auth.py**: The Python file `auth.py` is responsible for handling user authentication logic. It manages user login, registration, and authentication tasks within the project.

## Usage
To utilize the functionality provided in this folder:
1. Review the `validator.js` file to understand the validation rules applied to user input.
2. Explore the `auth.py` file to comprehend the user authentication processes implemented in the project.
3. Integrate these files into your project to enable user authentication features. Ensure to follow the guidelines and functions defined in the files for seamless authentication functionality.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class into your code and call the validation functions as needed.

```javascript
const InputValidator = require('./validator.js');

if (InputValidator.validateEmail('example@email.com')) {
    console.log('Email is valid');
}

if (InputValidator.validatePassword('StrongPassword123')) {
    console.log('Password meets criteria');
}

console.log(InputValidator.getPasswordStrength('GoodP@ssw0rd'));
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
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with date and time information.
- `timedelta`: For calculating time differences.
- `typing`: For type hints in function definitions.

---
*Auto-generated documentation - Last updated: 2025-07-17 18:06:46*
