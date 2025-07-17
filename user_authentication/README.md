# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` for client-side validation written in JavaScript and `auth.py` for server-side authentication written in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic with 1212 characters. It is responsible for validating user input on the client side before submitting it to the server.
  
- **auth.py**: With 2198 characters, `auth.py` is the server-side authentication script written in Python. It handles user authentication processes such as login, registration, and authentication token generation.

## Usage
1. To utilize the client-side validation provided by `validator.js`, include the script in your HTML file using `<script src="path/to/validator.js"></script>`. Then, call the validation functions as needed in your front-end code.
   
2. For server-side authentication tasks, import and use the `auth.py` module in your Python backend code. Implement the provided functions for user authentication processes in your application logic.

3. Ensure that both client-side and server-side components work together seamlessly to provide a secure and user-friendly authentication experience for your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Determines the strength level of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class where input validation is needed.

```javascript
const InputValidator = require('./validator.js');

// Example usage
if (InputValidator.validateEmail('example@email.com')) {
    console.log('Valid email address');
}

console.log(InputValidator.getPasswordStrength('StrongPassword123'));
```

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token if successful.
  - `logout(session_token: str) -> bool`: Ends a user session based on the session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations like registration, login, and session handling.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization and deserialization.
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 16:13:09*
