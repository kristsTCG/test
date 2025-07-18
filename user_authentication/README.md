# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. These files handle user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes `validator.js` for client-side validation in JavaScript and `auth.py` for server-side authentication in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic for user input. It ensures that user-provided data meets specified criteria before submission.
- **auth.py**: The `auth.py` file is responsible for server-side authentication processes. It manages user login, registration, and authentication using Python.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to suit the project's requirements.
   - Include the `validator.js` file in the relevant HTML pages to enable client-side validation.

2. **auth.py**:
   - Implement additional authentication features such as password hashing and session management.
   - Integrate the authentication logic into the project's backend to secure user access.

Ensure that both client-side and server-side authentication mechanisms work seamlessly together to provide a secure user authentication experience.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on various criteria.

**Usage:** Import the `InputValidator` class from this file to use the provided validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user's session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is still valid.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations. Call the methods within the class to register users, log in, log out, and check authentication status.

**Dependencies:** 
- `hashlib`: for hashing functions.
- `json`: for JSON serialization and deserialization.
- `datetime`: for date and time operations.
- `timedelta`: for time duration calculations.
- `typing`: for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 05:48:46*
