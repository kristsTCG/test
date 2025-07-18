# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It includes a JavaScript file for validation logic and a Python file for authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files, `validator.js` for client-side validation and `auth.py` for server-side authentication.

## Key Files
1. `validator.js`: This JavaScript file contains client-side validation logic for user inputs. It ensures that the data entered by the user meets the required criteria before submission.
   
2. `auth.py`: The Python file `auth.py` handles server-side authentication processes. It manages user login, registration, and authentication against the system.

## Usage
1. To utilize the client-side validation logic, refer to the `validator.js` file and integrate the validation functions into your frontend code.
   
2. For server-side authentication functionalities, utilize the `auth.py` file by importing the necessary functions and integrating them into your backend authentication processes.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character complexity.

**Usage:** To use this file, import `InputValidator` class where input validation is required.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user's session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 01:12:11*
