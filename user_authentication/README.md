# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It handles tasks such as validating user input and managing user authentication using both JavaScript and Python.

## Structure
The folder is organized to separate the validation logic (validator.js) written in JavaScript and the authentication logic (auth.py) written in Python.

## Key Files
- **validator.js**: This file contains the validation logic for user input. It ensures that the data entered by users meets the required criteria before proceeding with authentication.
- **auth.py**: The `auth.py` file is responsible for handling user authentication using Python. It manages user login, registration, and authentication processes within the project.

## Usage
1. **validator.js**:
   - Modify the validation criteria in the `validator.js` file to suit the project's requirements.
   - Import and use the validation functions in other parts of the project where user input validation is needed.

2. **auth.py**:
   - Implement additional authentication features as needed by extending the functionalities provided in the `auth.py` file.
   - Integrate the authentication logic into the project's user management system for seamless user authentication processes.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as checking password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username allowing alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** This file can be imported as a module in a Node.js application using `require` or `import` statements.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user session by deleting the session token.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:** 
- `hashlib` for hashing functions.
- `json` for JSON serialization.
- `datetime` for date and time operations.
- `timedelta` for calculating time differences.
- `typing` for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 22:45:44*
