# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. These files handle user validation and authentication processes.

## Structure
The folder is organized to manage user authentication logic efficiently. It includes validator.js for client-side validation written in JavaScript and auth.py for server-side authentication written in Python.

## Key Files
- **validator.js** (JavaScript): This file contains client-side validation logic for user inputs. It ensures that user-provided data meets the required criteria before submission.
- **auth.py** (Python): This file handles server-side authentication processes. It verifies user credentials, generates tokens, and manages user sessions.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to match the project's requirements.
   - Include the script in HTML files where user input validation is required.

2. **auth.py**:
   - Configure the authentication methods based on the project's security needs.
   - Integrate the authentication logic with other parts of the project that require user authentication.

Ensure to test the user authentication functionalities thoroughly to maintain the security and integrity of the application.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication process.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, logout, and session authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user's session by deleting the session token.
- `is_authenticated`: Method to check if a session token is valid and not expired.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations. Call methods like `register_user`, `login`, `logout`, and `is_authenticated` as needed.

**Dependencies:** 
- `hashlib` for hashing functions.
- `json` for JSON serialization (not used in the provided code).
- `datetime` for working with dates and times.
- `timedelta` for calculating time differences.
- `typing` for type hints (not used in the provided code).

---
*Auto-generated documentation - Last updated: 2025-07-17 22:52:01*
