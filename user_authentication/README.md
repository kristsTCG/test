# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes the following key components:
- `validator.js`: A JavaScript file containing functions for validating user input data. (1212 characters)
- `auth.py`: A Python file responsible for handling user authentication logic. (2198 characters)

## Key Files
### validator.js
- Role: Validates user input data to ensure it meets specified criteria.
- Size: 1212 characters

### auth.py
- Role: Manages user authentication processes such as login, logout, and user session handling.
- Size: 2198 characters

## Usage
1. To utilize the validation functions in `validator.js`, import the necessary functions into your JavaScript files and call them as needed to validate user input data.

Example:
```javascript
import { validateUsername, validatePassword } from './validator.js';

if (validateUsername(username) && validatePassword(password)) {
    // Proceed with user registration
} else {
    // Display error messages to the user
}
```

2. For user authentication tasks, interact with the functions in `auth.py` by importing and using them in your Python scripts.

Example:
```python
from auth import login, logout

if login(username, password):
    # User authentication successful
    # Perform further actions
else:
    # User authentication failed
    # Handle accordingly
```

Ensure to follow the specific usage guidelines provided within each file for seamless integration and functionality.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email address is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on its length and character composition.

**Usage:** This file can be imported as a module to perform input validation for user authentication in a Node.js application.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** User authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Register a new user with username, email, and password.
- `login(username: str, password: str) -> Optional[str]`: Authenticate user and return session token.
- `logout(session_token: str) -> bool`: End user session.
- `is_authenticated(session_token: str) -> bool`: Check if session token is valid.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your Python application.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For JSON operations.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 15:23:21*
