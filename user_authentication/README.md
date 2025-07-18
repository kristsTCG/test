# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It includes validation logic in JavaScript and authentication logic in Python.

## Structure
The folder is organized to handle user authentication tasks. It contains the following key files:
- `validator.js`: JavaScript file for validating user input data.
- `auth.py`: Python file for handling user authentication processes.

## Key Files
### validator.js
This file contains validation logic for user input data. It ensures that the data provided by users meets the required criteria before proceeding with authentication processes.

### auth.py
The `auth.py` file is responsible for managing user authentication within the project. It handles user login, registration, and authentication processes using Python.

## Usage
To utilize the functionalities provided in this folder:
1. Use the `validator.js` file to validate user input data before processing authentication.
2. Implement the authentication logic provided in the `auth.py` file to manage user authentication processes within the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Determines the strength level of a password.

**Usage:** To use this file, import `InputValidator` class where input validation is needed and call the respective validation functions or password strength function.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 08:05:06*
