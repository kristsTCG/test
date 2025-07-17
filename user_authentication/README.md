# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic for user input. It ensures that the data entered by the user meets the required criteria before submission.
  
- **auth.py**: This file contains server-side authentication logic using Python. It handles user authentication processes such as login, logout, and session management.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to suit the project's requirements.
   - Include the script in your HTML files to enable client-side validation.

2. **auth.py**:
   - Implement additional authentication features such as two-factor authentication or password reset functionality.
   - Integrate the authentication logic with your backend server to secure user access.

Ensure that both files work seamlessly together to provide a robust user authentication system for your project.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of being at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on its length and character composition.

**Usage:** This file can be imported into other JavaScript files using `require` or `import` statements to access the input validation functions.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication processes.

**Dependencies:** 
- `hashlib`: Used for hashing passwords.
- `json`: Not used in this file but imported.
- `datetime`: Used for handling date and time information.
- `timedelta`: Used to calculate session expiration time.
- `typing`: Used for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 18:10:49*
