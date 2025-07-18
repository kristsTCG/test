# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. These files handle validation of user input and authentication processes.

## Structure
The folder is organized to separate the validation logic implemented in `validator.js` (JavaScript) and the authentication functionality in `auth.py` (Python).

## Key Files
- **validator.js**: This file contains the JavaScript code for validating user input. It plays a crucial role in ensuring that user data meets the required criteria before proceeding with authentication.
  
- **auth.py**: The `auth.py` file is written in Python and is responsible for handling user authentication processes. It manages user login, registration, and authentication within the system.

## Usage
1. **validator.js**: To use the validation logic provided in `validator.js`, import the necessary functions into your JavaScript files. You can then call these functions to validate user input before processing it further.

2. **auth.py**: Utilize the functions and classes defined in `auth.py` to implement user authentication features in your Python application. This file provides the necessary methods for user registration, login, and authentication. Ensure to handle user authentication securely to protect user data.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specified criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Determines the strength level of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class in your code and call the desired validation functions as needed.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user authentication, registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password, returning a session token.
- `logout`: Method to end a user session by providing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication. Use the provided methods to register users, log in, log out, and check authentication status.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 07:05:09*
