# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. This includes validation of user input and handling user authentication using JavaScript and Python.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes a JavaScript file for client-side validation (`validator.js`) and a Python file for server-side authentication (`auth.py`).

## Key Files
- `validator.js`: This JavaScript file contains functions for validating user input on the client-side before submitting it to the server. It plays a crucial role in ensuring data integrity and security.
- `auth.py`: The Python file `auth.py` is responsible for handling user authentication on the server-side. It manages user login, registration, and authentication processes.

## Usage
1. To utilize the client-side validation provided by `validator.js`, include this file in your HTML file using a script tag.
2. Use the functions in `validator.js` to validate user input fields before submitting forms.
3. In your server-side code, import and utilize the functionalities provided in `auth.py` for user authentication processes such as login and registration.

Remember to customize the authentication logic to fit your project's specific requirements and security needs.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username allowing alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on various criteria.

**Usage:** To use this file, import `InputValidator` class in your code and call the validation methods as needed.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash passwords using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user's session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize user authentication features.

**Dependencies:**
- `hashlib`: Used for hashing passwords.
- `json`: Not used in the provided code.
- `datetime`: Used for managing timestamps and session expiration.
- `typing`: Used for type hints in function definitions.

---
*Auto-generated documentation - Last updated: 2025-07-18 02:18:53*
