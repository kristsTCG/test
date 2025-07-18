# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. These files handle validation of user input and authentication processes.

## Structure
The folder is organized to separate the validation logic in `validator.js` written in JavaScript and the authentication logic in `auth.py` written in Python.

## Key Files
- **validator.js**: This file contains the validation logic for user input. It ensures that the data provided by users meets the required criteria before proceeding with authentication.
- **auth.py**: The `auth.py` file is responsible for handling user authentication processes. It verifies user credentials and grants access based on the authentication outcome.

## Usage
1. To utilize the validation logic, refer to the `validator.js` file. Modify or extend the validation rules as needed for your project.
2. For user authentication functionalities, interact with the `auth.py` file. Implement any additional authentication steps required for your project's security needs.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Calculates the strength level of a password.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication process.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash passwords using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization and deserialization.
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hinting in function definitions.

---
*Auto-generated documentation - Last updated: 2025-07-18 04:14:46*
