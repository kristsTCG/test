# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. These files handle validation and authentication processes for user accounts.

## Structure
The folder is organized to separate the validation logic in `validator.js` (JavaScript) and the authentication logic in `auth.py` (Python).

## Key Files
- `validator.js`: This file contains the JavaScript code for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria before proceeding with authentication.
  
- `auth.py`: The `auth.py` file contains Python code responsible for user authentication processes. It manages user login, registration, and authentication within the system.

## Usage
1. To utilize the validation functionality, refer to `validator.js` and incorporate the validation methods into your user input forms.
   
2. For user authentication features, interact with `auth.py` to handle user login, registration, and authentication processes within your project.

3. Ensure to maintain the integrity of the validation and authentication processes to enhance the security of user accounts within the system.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the format of a password (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates the format of a username (3-20 characters, alphanumeric and underscores only).
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, logout, and session authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user's session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations. Call the provided methods to register users, authenticate logins, manage sessions, and check authentication status.

**Dependencies:** 
- `hashlib`: for hashing passwords.
- `json`: for JSON serialization (not used in this file).
- `datetime`: for working with dates and times.
- `timedelta`: for calculating time differences.
- `typing`: for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 01:50:36*
