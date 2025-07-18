# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. It includes a JavaScript file for validation logic and a Python file for handling authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It consists of two key files: `validator.js` for client-side validation and `auth.py` for server-side authentication.

## Key Files
1. **validator.js**: This JavaScript file contains client-side validation logic for user input. It ensures that user-provided data meets the required criteria before submission.
   
2. **auth.py**: The Python file `auth.py` handles server-side authentication processes. It manages user login, registration, and authentication against the system.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to suit the project's requirements.
   - Include the `validator.js` file in your HTML pages using a script tag.
   - Call the validation functions from your form submission logic to validate user input.

2. **auth.py**:
   - Customize the authentication logic to integrate with your project's user management system.
   - Import the `auth.py` file in your main application file or other relevant modules.
   - Use the provided functions for user login, registration, and authentication within your application's routes or controllers.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on its length and character composition.

**Usage:** This file can be imported using `require` or `import` statements to access the input validation functionalities provided by the `InputValidator` class.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session management.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and has not expired.

**Usage:** This file can be imported into other Python scripts to handle user authentication tasks.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 05:02:58*
