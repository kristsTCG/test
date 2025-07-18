# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It consists of two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This JavaScript file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
  
- **auth.py**: The Python file `auth.py` is responsible for handling user authentication processes. It includes functions for user login, registration, and authentication checks.

## Usage
To utilize the functionality provided in this folder:
1. Review the `validator.js` file to understand the validation logic and criteria for user input.
2. Explore the `auth.py` file to implement user authentication features such as login, registration, and authentication checks.
3. Integrate these files into your project to enable secure user authentication processes.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username, allowing only alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types, returning a descriptive level.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, logout, and session authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user's session by providing the session token.
- `is_authenticated`: Method to check if a session token is valid and not expired.

**Usage:** To use this file, create an instance of `UserAuth` and call its methods for user registration, login, logout, and session validation.

**Dependencies:** 
- `hashlib`: Used for hashing passwords.
- `json`: Not used in the provided code but imported.
- `datetime`: Used for managing timestamps and session expiration.
- `typing`: Used for type hints in function definitions.

---
*Auto-generated documentation - Last updated: 2025-07-18 02:01:16*
