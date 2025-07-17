# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes two key files: `validator.js` for client-side validation in JavaScript and `auth.py` for server-side authentication in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic for user inputs. It ensures that user-provided data meets the required criteria before submission.
- **auth.py**: The `auth.py` file handles server-side authentication processes. It verifies user credentials, generates tokens, and manages user sessions securely.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to suit the project's requirements.
   - Include the script in your HTML files using `<script src="path/to/validator.js"></script>`.

2. **auth.py**:
   - Import the `auth` module in your Python scripts to utilize its authentication functionalities.
   - Implement the necessary endpoints to handle user login, registration, and token generation.

Ensure proper integration of these files with other components of the project for seamless user authentication.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates if the input username meets specific criteria (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file and use its static methods to perform input validation and password strength assessment.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
  - `logout(session_token: str) -> bool`: Ends a user session.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session is valid.

**Usage:** Instantiate `UserAuth` to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing functions.
- `json`: For JSON serialization.
- `datetime`: For handling date and time.
- `timedelta`: For time-based calculations.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 19:25:58*
