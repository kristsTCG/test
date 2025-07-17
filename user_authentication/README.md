# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
  
- **auth.py**: The `auth.py` file is responsible for handling user authentication logic using Python. It manages user login, registration, and authentication processes within the system.

## Usage
1. **validator.js**:
   - To use the functions in `validator.js`, import the file into your JavaScript project.
   - Utilize the validation functions provided in `validator.js` to validate user input data before processing it further.

2. **auth.py**:
   - Import `auth.py` into your Python project to access the user authentication functionalities.
   - Use the functions defined in `auth.py` to implement user login, registration, and authentication features in your application.

Ensure to follow the documentation within each file for specific usage instructions and guidelines.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username allowing alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class from `validator.js` and call the desired validation methods as needed.

```javascript
const InputValidator = require('./validator.js');

const email = 'example@email.com';
const isEmailValid = InputValidator.validateEmail(email);

const password = 'StrongPassword123';
const isPasswordValid = InputValidator.validatePassword(password);

const username = 'user_123';
const isUsernameValid = InputValidator.validateUsername(username);

const passwordStrength = InputValidator.getPasswordStrength(password);
```

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 19:18:17*
