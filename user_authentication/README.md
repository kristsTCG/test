# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. **validator.js**: This file contains client-side validation logic for user input. It ensures that the data entered by the user meets the required criteria before submission.
   
2. **auth.py**: The `auth.py` file contains server-side authentication logic written in Python. It handles user authentication processes such as login, registration, and session management.

## Usage
1. **validator.js**:
   - To use the validation logic provided in `validator.js`, include the file in your HTML document using a script tag.
   - Call the validation functions defined in `validator.js` on form submission events to validate user input.

2. **auth.py**:
   - Import the `auth` module in your Python application to access the authentication functionalities.
   - Utilize the functions defined in `auth.py` for user registration, login, and managing user sessions.

Ensure to follow the documentation within each file for specific usage instructions and customization options.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Determines the strength level of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class where input validation is needed and call the respective validation methods as needed.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user's session.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing functions.
- `json`: For JSON serialization and deserialization.
- `datetime`: For working with dates and times.
- `timedelta`: For representing a duration of time.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 20:35:48*
