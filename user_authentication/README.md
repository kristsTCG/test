# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities within the project. It handles tasks such as validating user input and managing user authentication using both JavaScript and Python.

## Structure
The folder is organized to separate the JavaScript and Python code for user authentication. The `validator.js` file contains JavaScript functions for validating user input, while the `auth.py` file contains Python code for managing user authentication.

## Key Files
- **validator.js**: This file contains JavaScript functions for validating user input, ensuring that the data entered by users meets the required criteria.
- **auth.py**: The `auth.py` file includes Python code responsible for managing user authentication processes, such as user login, registration, and authentication.

## Usage
1. **validator.js**:
   - To use the functions in `validator.js`, import the file into your JavaScript code using `import validator from './validator.js';`.
   - Call the specific validation functions as needed, passing the user input as arguments.
   - Example: `validator.validateEmail(email)` to validate an email address.

2. **auth.py**:
   - To utilize the authentication functionalities in `auth.py`, import the necessary functions into your Python code using `from auth import login, register, authenticate`.
   - Use the imported functions to handle user authentication processes such as login, registration, and authentication.
   - Example: `login(username, password)` to authenticate a user's login credentials.

Ensure to follow the documentation within each file for specific function usage and parameters.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long, alphanumeric, and contains underscores only.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character complexity.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user's session.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hinting.

---
*Auto-generated documentation - Last updated: 2025-07-17 18:53:13*
