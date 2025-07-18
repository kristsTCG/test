# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript for input validation and `auth.py` written in Python for authentication logic.

## Key Files
1. `validator.js`: This file contains functions for validating user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before proceeding with authentication.
   
2. `auth.py`: This file handles the authentication logic for verifying user credentials and granting access to authorized users. It is responsible for securely managing user authentication processes.

## Usage
1. To use the `validator.js` file, import it into your JavaScript code and call the validation functions as needed to validate user input before authentication.
   
2. For the `auth.py` file, integrate it into your Python application to handle user authentication. Utilize the provided functions to authenticate users securely and manage access control.

Ensure to follow best practices for user authentication and data validation while working with the code in this folder.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long, alphanumeric, and allows underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash passwords using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: Used for hashing functions.
- `json`: Used for JSON serialization and deserialization.
- `datetime`: Used for working with dates and times.
- `timedelta`: Used for representing time differences.
- `typing`: Used for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 01:36:24*
