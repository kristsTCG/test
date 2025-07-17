# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This module handles user validation and authentication processes.

## Structure
The folder is organized to centralize all user authentication logic. It includes validator.js for client-side validation and auth.py for server-side authentication.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation logic for user inputs. It plays a crucial role in ensuring data integrity before sending it to the server.
  
- **auth.py**: This Python file handles server-side authentication processes. It manages user login, registration, and authentication against the database.

## Usage
1. To utilize the client-side validation provided by `validator.js`, include this file in your HTML `<script>` tag.
2. Use the functions defined in `auth.py` to authenticate users on the server-side. Make sure to integrate these functions with your backend logic for user management.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including validating email, password, and username inputs, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username, allowing alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types, returning a descriptive level.

**Usage:** Import the `InputValidator` class from this file to use its validation methods in user authentication processes.

**Dependencies:** No external dependencies are required for this file.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib` for hashing functions.
- `json` for JSON serialization and deserialization.
- `datetime` for date and time operations.
- `timedelta` from `datetime` for time-based calculations.
- `typing.Optional` and `typing.Dict` for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 15:54:13*
