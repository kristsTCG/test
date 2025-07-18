# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks. It includes two key files: `validator.js` written in JavaScript for input validation and `auth.py` written in Python for authentication logic.

## Key Files
1. `validator.js`: This file contains functions for validating user input data. It plays a crucial role in ensuring that the data entered by users meets the required criteria.
   
2. `auth.py`: The `auth.py` file handles the authentication process for users. It manages user login, registration, and authentication logic within the system.

## Usage
To work with the code in this folder:
1. Use `validator.js` functions to validate user input data before processing it further.
2. Utilize `auth.py` for implementing user authentication features such as login, registration, and authentication logic.
3. Ensure to maintain the integrity of user data by following the validation rules defined in `validator.js`.
4. Implement secure authentication processes using the functions provided in `auth.py`.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication. It provides methods to validate email, password, and username inputs, as well as determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of the input password based on length and character types.

**Usage:** To use this file, import `InputValidator` class from `validator.js` into your code.

```javascript
const InputValidator = require('./validator.js');

// Example usage
if (InputValidator.validateEmail('example@email.com')) {
    console.log('Email is valid');
}

console.log(InputValidator.getPasswordStrength('StrongPassword123'));
```

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user's session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations. Call methods like `register_user`, `login`, `logout`, and `is_authenticated` as needed.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-18 02:12:00*
