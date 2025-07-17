# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. **validator.js**
   - Type: JavaScript
   - Size: 1212 characters
   - Role: Responsible for validating user input data to ensure it meets specified criteria before processing it further.

2. **auth.py**
   - Type: Python
   - Size: 2198 characters
   - Role: Manages the authentication process for users, including login, logout, and session management.

## Usage
1. To utilize the validation functionality, refer to `validator.js` and incorporate the validation methods into your code where necessary.
   
2. For user authentication tasks such as login and session management, interact with the functions provided in `auth.py` to ensure secure user authentication within the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file and use its static methods to validate user inputs.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session by deleting the session token.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization/deserialization.
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hints in function definitions.

---
*Auto-generated documentation - Last updated: 2025-07-17 14:35:14*
