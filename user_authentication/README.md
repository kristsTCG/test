# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files, `validator.js` for client-side validation written in JavaScript and `auth.py` for server-side authentication written in Python.

## Key Files
1. `validator.js`: This file contains client-side validation logic for user input. It ensures that the data entered by the user meets the required criteria before submission.
   
2. `auth.py`: The `auth.py` file handles server-side authentication processes. It manages user login, registration, and authentication against the database.

## Usage
1. To utilize the client-side validation logic, refer to `validator.js`. You can customize the validation rules as per your project requirements by modifying the code in this file.

2. For server-side authentication functionalities, interact with `auth.py`. This file provides the necessary functions to authenticate users and manage their access to the system.

3. Ensure that both client-side and server-side authentication processes are in sync to provide a secure and seamless user authentication experience.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** This file can be imported into other JavaScript files using `require` or `import` statements to access the input validation functions.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, logout, and session authentication.
- `hash_password()`: Method to hash a password using SHA-256.
- `register_user()`: Method to register a new user with a unique username, email, and password.
- `login()`: Method to authenticate a user and generate a session token for active sessions.
- `logout()`: Method to end a user's session by removing the session token.
- `is_authenticated()`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 00:44:02*
