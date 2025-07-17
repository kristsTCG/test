# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized with two key files: `validator.js` written in JavaScript and `auth.py` written in Python. These files handle user input validation and authentication processes respectively.

## Key Files
- **validator.js**: This file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria before proceeding with authentication.
  
- **auth.py**: The `auth.py` file is responsible for handling user authentication processes. It includes functions for verifying user credentials and managing user sessions.

## Usage
To utilize the functionalities provided in this folder:
1. Review the `validator.js` file to understand the validation rules and functions available for user input.
2. Explore the `auth.py` file to implement user authentication logic in your project.
3. Ensure to integrate these files with other parts of the project that require user authentication capabilities.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates an email address format using a regular expression.
- `validatePassword(password)`: Validates a password format requiring at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates a username format requiring 3-20 characters, alphanumeric characters, and underscores only.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character complexity.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 20:56:44*
