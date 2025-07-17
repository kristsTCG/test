# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` for client-side input validation in JavaScript and `auth.py` for server-side authentication in Python.

## Key Files
- `validator.js`: This file contains client-side validation logic written in JavaScript. It ensures that user input meets specified criteria before submitting to the server for authentication.
- `auth.py`: The `auth.py` file handles server-side authentication using Python. It includes functions to authenticate users based on their credentials and manage user sessions securely.

## Usage
1. **validator.js**:
   - To use the client-side validation logic, include `validator.js` in your HTML file using a script tag.
   - Call the appropriate validation functions defined in `validator.js` on user input fields to ensure data integrity before submission.

2. **auth.py**:
   - Import `auth.py` in your Python project to leverage the authentication functionalities.
   - Utilize the provided functions in `auth.py` to authenticate users, manage sessions, and enforce security measures for user authentication.

Ensure that both client-side and server-side authentication mechanisms work seamlessly together to provide a secure user authentication process in your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your Python application.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 22:55:24*
