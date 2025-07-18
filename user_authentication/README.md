# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files, `validator.js` for client-side input validation written in JavaScript, and `auth.py` for server-side authentication logic written in Python.

## Key Files
- `validator.js`: This file contains client-side validation logic to ensure that user input meets specified criteria before submission.
- `auth.py`: This file contains server-side authentication logic to verify user credentials and manage user sessions securely.

## Usage
1. To use the client-side validation provided in `validator.js`, include the script in your HTML file using `<script src="path/to/validator.js"></script>`. Then, call the appropriate validation functions on user input fields.
   
2. To implement server-side authentication using `auth.py`, import the necessary functions into your Python script and utilize them to authenticate users and manage sessions securely. Make sure to handle authentication responses appropriately in your application logic.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength evaluation.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username allowing alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Evaluates the strength of a password based on length and character requirements.

**Usage:** To use this file, import `InputValidator` class where input validation is needed and call the appropriate validation methods.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password, generating a session token.
- `logout`: Method to end a user session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib` for hashing functions.
- `json` for JSON serialization.
- `datetime` and `timedelta` from `datetime` module for handling timestamps.
- `typing` for type hinting support.

---
*Auto-generated documentation - Last updated: 2025-07-18 08:46:49*
