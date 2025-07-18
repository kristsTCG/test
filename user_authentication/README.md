# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities within the project. It includes validation logic in JavaScript and authentication logic in Python.

## Structure
The folder is organized to handle user authentication processes. It includes two key files: `validator.js` for input validation and `auth.py` for user authentication.

## Key Files
- **validator.js**: This JavaScript file contains logic for validating user inputs. It plays a crucial role in ensuring that user-provided data meets the required criteria before proceeding with authentication processes.
  
- **auth.py**: The Python file `auth.py` is responsible for handling user authentication within the project. It manages user login, registration, and authentication processes.

## Usage
To utilize the code in this folder:
1. Use `validator.js` to validate user inputs before processing authentication requests.
2. Incorporate `auth.py` to manage user authentication processes such as login, registration, and authentication.
3. Ensure to follow the defined validation rules in `validator.js` to maintain data integrity and security in the authentication process.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long, alphanumeric, and allows underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user session.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization and deserialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hinting support.

---
*Auto-generated documentation - Last updated: 2025-07-18 08:50:36*
