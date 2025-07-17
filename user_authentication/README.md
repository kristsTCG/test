# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. These files are responsible for validating user input and handling authentication processes.

## Structure
The folder `user_authentication` contains two key files:
- `validator.js`: A JavaScript file with 1212 characters, responsible for validating user input data.
- `auth.py`: A Python file with 2198 characters, responsible for handling user authentication processes.

## Key Files
### validator.js
- **Role**: Validates user input data.
- **Size**: 1212 characters
- **Language**: JavaScript

### auth.py
- **Role**: Handles user authentication processes.
- **Size**: 2198 characters
- **Language**: Python

## Usage
1. To utilize the validation functionality provided by `validator.js`, import the file into your JavaScript code and call the appropriate validation functions as needed.
2. To incorporate user authentication processes, import `auth.py` into your Python code and utilize the authentication methods provided within the file. Make sure to follow the documentation within the file for proper usage.

Ensure that you understand the specific functionalities and methods provided by each file before integrating them into your project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and return a session token for active sessions.
- `logout`: Method to end a user session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 21:56:08*
