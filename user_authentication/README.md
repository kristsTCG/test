# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks. It contains two key files: `validator.js` for client-side validation written in JavaScript and `auth.py` for server-side authentication logic written in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic to ensure that user input meets specified criteria before submitting to the server.
- **auth.py**: The `auth.py` file handles server-side authentication tasks such as verifying user credentials, generating tokens, and managing user sessions.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to match the project requirements.
   - Include `validator.js` in your HTML files using a `<script>` tag.
   - Call the validation functions from your form submission logic.

2. **auth.py**:
   - Implement additional authentication logic as required by the project.
   - Integrate the authentication functions with your backend server code.
   - Securely store sensitive information such as secret keys and tokens.

Ensure to test the user authentication functionalities thoroughly to ensure the security and reliability of the system.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3 to 20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on its length and character composition.

**Usage:** This file can be imported into other JavaScript files using `require` or `import` statements to access the input validation functions.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and not expired.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization and deserialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 01:21:02*
