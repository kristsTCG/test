# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript for input validation and `auth.py` written in Python for handling authentication processes.

## Key Files
- `validator.js`: This file contains functions for validating user input data to ensure it meets specified criteria. It plays a crucial role in maintaining data integrity and security.
- `auth.py`: This file is responsible for managing user authentication processes such as login, logout, and user session management. It interacts with the database to verify user credentials and authorize access.

## Usage
1. **validator.js**: To use the validation functions in this file, import them into your JavaScript files where input validation is required. Call the appropriate functions with user input data as parameters to validate the input.
   
   Example:
   ```javascript
   import { validateEmail } from './validator.js';
   
   const email = 'example@example.com';
   if (validateEmail(email)) {
       // Proceed with the email validation logic
   } else {
       // Handle invalid email input
   }
   ```

2. **auth.py**: To utilize the authentication functionalities provided in this file, import the necessary functions into your Python scripts where user authentication is needed. Implement the authentication flow based on the functions available in `auth.py`.
   
   Example:
   ```python
   from auth import login
   
   username = 'user123'
   password = 'password123'
   if login(username, password):
       # User authentication successful
   else:
       # User authentication failed
   ``` 

Ensure to follow best practices and security measures when integrating these files into your project to maintain a secure user authentication system.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the specified criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates if the input username meets the specified criteria (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication process.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
  - `logout(session_token: str) -> bool`: Ends a user session based on the session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Instantiate `UserAuth` to utilize user registration, login, logout, and authentication functionalities.

**Dependencies:**
- `hashlib`: Used for hashing passwords.
- `json`: Not used in the provided code but imported.
- `datetime`: Used for timestamp operations.
- `timedelta`: Used for calculating session expiration time.
- `typing`: Used for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 22:52:47*
