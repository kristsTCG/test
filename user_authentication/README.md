# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` for client-side validation written in JavaScript and `auth.py` for server-side authentication logic written in Python.

## Key Files
1. **validator.js**: This file contains client-side validation logic for user inputs. It plays a crucial role in ensuring that user-provided data meets the required criteria before submission.
   
2. **auth.py**: The `auth.py` file is responsible for server-side authentication processes. It manages user authentication, login, and authorization within the system.

## Usage
1. **validator.js**:
   - To use the client-side validation logic, include `validator.js` in your HTML file using a `<script>` tag.
   - Call the appropriate validation functions defined in `validator.js` on user input fields to validate user data before submission.

2. **auth.py**:
   - Import `auth.py` in your Python project to utilize the authentication functionalities.
   - Use the provided functions in `auth.py` to handle user login, authentication, and authorization processes within your application.

Ensure that you follow the guidelines and best practices defined in each file for secure and efficient user authentication in your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates an email address based on a regular expression pattern.
- `validatePassword(password)`: Validates a password based on specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates a username based on length and character restrictions.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character complexity.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user's session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your application.

**Dependencies:** 
- `hashlib` for hashing passwords.
- `json` for JSON serialization (not used in this file).
- `datetime` for working with dates and times.
- `timedelta` for calculating time differences.
- `typing` for type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-17 14:58:38*
