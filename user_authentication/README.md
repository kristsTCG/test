# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities in the project. It handles user validation and authentication processes.

## Structure
The folder is organized to handle user authentication logic using both JavaScript and Python. It includes two key files: `validator.js` for client-side validation and `auth.py` for server-side authentication.

## Key Files
- `validator.js`: This JavaScript file contains client-side validation logic for user inputs. It ensures that user-provided data meets specified criteria before submission.
- `auth.py`: This Python file handles server-side authentication processes. It verifies user credentials, generates tokens, and manages user sessions.

## Usage
1. To use the client-side validation logic, refer to `validator.js` in your HTML file using `<script>` tags. Customize the validation rules as needed for your project.
2. For server-side authentication, import `auth.py` in your Python application. Use the provided functions to authenticate users and manage sessions securely.

Ensure to follow best practices for user authentication and data security when working with the code in this folder.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user's session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is still valid.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: Used for hashing passwords.
- `json`: Not used in the provided code but imported.
- `datetime`: Used for handling date and time operations.
- `timedelta`: Used for calculating expiration time for session tokens.
- `typing`: Used for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 05:54:45*
