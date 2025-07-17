# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files, `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. **validator.js**: This file contains client-side validation logic for user input. It plays a crucial role in ensuring that user data meets the required criteria before submission.
   
2. **auth.py**: The `auth.py` file is responsible for server-side authentication processes. It manages user authentication, login, and session handling on the backend.

## Usage
1. To utilize the client-side validation functionality, refer to the `validator.js` file. Modify the validation rules as needed to suit the project requirements.
   
2. For server-side authentication tasks, interact with the `auth.py` file. Implement additional authentication logic or integrate it with existing authentication systems as necessary.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength level of a password based on various criteria.

**Usage:** To use this file, import `InputValidator` class from `validator.js` into your code.

```javascript
const InputValidator = require('./validator.js');
```

Then, you can use the validation methods like `InputValidator.validateEmail(email)` or `InputValidator.getPasswordStrength(password)`.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and hashed password.
- `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token for active sessions.
- `logout(session_token: str) -> bool`: Ends a user session by removing the session token from active sessions.
- `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations like registration, login, logout, and session validation.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 17:39:11*
