# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This functionality is crucial for managing user access and security within the application.

## Structure
The folder is organized to handle user authentication processes. It includes validator.js for client-side validation and auth.py for server-side authentication logic.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation functions to ensure that user input meets specified criteria before submitting to the server.
- **auth.py**: This Python file contains server-side authentication logic, handling user login, registration, and authentication processes.

## Usage
1. To use the client-side validation functions in `validator.js`, include the file in your HTML document using a script tag.
2. Utilize the functions provided in `validator.js` to validate user input fields before submitting forms.
3. In the server-side code, import `auth.py` to access the authentication logic for user registration, login, and authentication processes.
4. Customize the authentication logic in `auth.py` to suit the requirements of your project.
5. Ensure proper error handling and security measures are in place when integrating the authentication functionality into your application.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength level of a password based on various criteria.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and still active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: for hashing passwords.
- `json`: for JSON serialization and deserialization.
- `datetime`: for working with dates and times.
- `timedelta`: for calculating time differences.
- `typing`: for type hinting in Python.

---
*Auto-generated documentation - Last updated: 2025-07-17 20:16:11*
