# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It includes scripts for validating user input and handling authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It consists of two key files, `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
1. **validator.js**
   - Role: Responsible for validating user input data.
   - Size: 1212 characters
   - Language: JavaScript

2. **auth.py**
   - Role: Manages user authentication processes.
   - Size: 2198 characters
   - Language: Python

## Usage
1. **validator.js**:
   - To use the validator script, import it into your JavaScript file using `require` or `import`.
   - Call the appropriate validation functions provided in `validator.js` to validate user input data.

2. **auth.py**:
   - Import the `auth` module into your Python script to access authentication functionalities.
   - Utilize the functions within `auth.py` to handle user authentication tasks within your project.

Ensure that you understand the specific functions and methods provided in each file to effectively implement user authentication features in your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates an email address format using a regular expression.
- `validatePassword(password)`: Validates a password format requiring at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates a username format requiring 3-20 characters, alphanumeric and underscores only.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use its validation and strength assessment methods.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user's session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and the user is authenticated.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 18:31:18*
