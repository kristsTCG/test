# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This functionality is responsible for validating user input and handling authentication processes.

## Structure
The folder is organized to separate the validation logic implemented in JavaScript and the authentication logic implemented in Python.

## Key Files
- `validator.js`: This JavaScript file contains the validation logic for user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before proceeding with authentication.
- `auth.py`: The Python file `auth.py` is responsible for handling the authentication process. It manages user authentication, login, and session management within the project.

## Usage
1. To utilize the validation logic, refer to `validator.js` for functions and methods related to validating user input.
2. For authentication functionalities, interact with `auth.py` to handle user authentication, login, and session management processes.
3. Ensure to integrate these files into the project's authentication flow to enhance security and user experience.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username allowing alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password and returns a descriptive level.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password()`: Method to hash a password using SHA-256.
- `register_user()`: Method to register a new user with a unique username, email, and password.
- `login()`: Method to authenticate a user with a username and password, returning a session token.
- `logout()`: Method to end a user session based on the session token.
- `is_authenticated()`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hinting in Python.

---
*Auto-generated documentation - Last updated: 2025-07-17 23:53:59*
