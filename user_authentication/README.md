# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript for input validation and `auth.py` written in Python for authentication processes.

## Key Files
1. **validator.js**: This file contains functions for validating user input, ensuring data integrity and security.
2. **auth.py**: This file handles user authentication processes, such as login, registration, and password management.

## Usage
To utilize the functionality provided in this folder:
- Use the functions in `validator.js` to validate user input before processing.
- Implement the authentication logic in `auth.py` to manage user authentication within the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class from `validator.js` into your code.

```javascript
const InputValidator = require('./validator.js');

// Example usage
if (InputValidator.validateEmail('example@email.com')) {
    // Email is valid
}

const passwordStrength = InputValidator.getPasswordStrength('StrongPassword123');
console.log(passwordStrength); // Output: 'Strong'
```

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user's session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your Python application.

**Dependencies:**
- `hashlib`: Used for hashing passwords.
- `json`: Used for JSON serialization (not used in this file).
- `datetime`: Used for working with dates and times.
- `timedelta`: Used for calculating time differences.
- `typing`: Used for type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-17 13:59:25*
