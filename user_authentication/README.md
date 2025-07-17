# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities within the project. It includes validation logic in JavaScript and authentication logic in Python.

## Structure
The folder is organized to handle user authentication processes. It contains two key files, `validator.js` for input validation and `auth.py` for user authentication.

## Key Files
1. `validator.js`: This JavaScript file contains logic for validating user inputs. It plays a crucial role in ensuring that user-provided data meets the required criteria for authentication.
   
2. `auth.py`: The Python file `auth.py` is responsible for handling user authentication processes. It manages user login, registration, and authentication within the system.

## Usage
To utilize the functionalities provided in the `user_authentication` folder:
1. Use the `validator.js` file to validate user inputs before processing authentication requests.
2. Incorporate the `auth.py` file to manage user authentication processes such as login and registration.

Ensure to follow the specific guidelines and functions defined in each file for seamless integration and operation of user authentication features in the project.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class from `validator.js` and call the desired validation functions or password strength calculation function.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class managing user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user's session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** To use this file, create an instance of `UserAuth` and call its methods for user registration, login, logout, and session validation.

**Dependencies:** The file imports `hashlib`, `json`, `datetime`, `timedelta`, and `Optional` from `typing`.

---
*Auto-generated documentation - Last updated: 2025-07-17 15:49:08*
