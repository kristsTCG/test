# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It consists of two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
  
- **auth.py**: The Python file `auth.py` is responsible for handling the authentication process. It manages user login, registration, and authentication procedures within the system.

## Usage
To utilize the functionality provided in this folder:
1. Review the `validator.js` file for validation functions and ensure they are integrated into user input forms.
2. Utilize the `auth.py` file for implementing user authentication processes such as login, registration, and authentication logic within the project.
3. Ensure that both files are appropriately imported and utilized in the relevant parts of the project where user authentication is required.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the format of a password, requiring at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates the format of a username, allowing 3-20 characters that are alphanumeric and underscores only.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character requirements.

**Usage:** This file can be imported into other JavaScript files using `require` or `import` statements to access the input validation functions provided by the `InputValidator` class.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user's session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided by this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 18:00:46*
