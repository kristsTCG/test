# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities within the project. It handles user validation and authentication processes.

## Structure
The folder is organized to separate the validation logic in a JavaScript file (`validator.js`) and the authentication logic in a Python file (`auth.py`).

## Key Files
- **validator.js**: This JavaScript file contains the logic for validating user input data. It ensures that the data provided by users meets the required criteria for authentication.
  
- **auth.py**: The Python file `auth.py` is responsible for handling user authentication processes. It includes functions for user login, registration, and authentication.

## Usage
1. To use the validation logic, refer to `validator.js`. You can import and utilize the validation functions in your JavaScript code to validate user input data before proceeding with authentication processes.

2. For user authentication functionalities, refer to `auth.py`. Import the necessary functions into your Python code to handle user login, registration, and authentication processes within your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username allowing alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on various criteria.

**Usage:** To use this file, import `InputValidator` class in your code and call the validation methods as needed.

```javascript
const InputValidator = require('./validator.js');

if (InputValidator.validateEmail('example@email.com')) {
    console.log('Email is valid');
}

const passwordStrength = InputValidator.getPasswordStrength('StrongPassword123');
console.log('Password strength:', passwordStrength);
```

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Register a new user with a unique username.
- `login(username: str, password: str) -> Optional[str]`: Authenticate user and return a session token.
- `logout(session_token: str) -> bool`: End a user session.
- `is_authenticated(session_token: str) -> bool`: Check if a session token is valid.

**Usage:** Instantiate `UserAuth` to utilize user authentication functionalities like registration, login, logout, and session validation.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization and deserialization.
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing.Optional`: For type hinting optional return values.
- `typing.Dict`: For type hinting dictionary structures.

---
*Auto-generated documentation - Last updated: 2025-07-18 01:43:12*
