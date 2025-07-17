# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. **validator.js**: This JavaScript file contains functions for validating user input. It plays a crucial role in ensuring that user data meets the required criteria before proceeding with authentication.
   
2. **auth.py**: The Python file `auth.py` is responsible for handling user authentication processes. It includes functions for user login, registration, and authentication checks.

## Usage
To work with the code in this folder:
1. Use the functions defined in `validator.js` to validate user input data before initiating any authentication processes.
2. Utilize the functions provided in `auth.py` for user login, registration, and authentication tasks within the project.
3. Ensure to maintain the integrity of the authentication logic to secure user data and prevent unauthorized access.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on length and character requirements.

**Usage:** To use this file, import it into your project using `require` or `import` statements. For example:
```javascript
const InputValidator = require('./validator.js');

if (InputValidator.validateEmail('example@email.com')) {
    // Email is valid
}
```

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
  
  - `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
  
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and hashed password.
  
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and generates a session token for active sessions.
  
  - `logout(session_token: str) -> bool`: Ends a user session based on the provided session token.
  
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and not expired.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:** 
- `hashlib`: For hashing functions.
- `json`: For JSON serialization.
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing.Optional`: For defining optional return types.
- `typing.Dict`: For defining dictionary types.

---
*Auto-generated documentation - Last updated: 2025-07-17 15:51:11*
