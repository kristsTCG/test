# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. It includes a JavaScript file for validation and a Python file for handling authentication.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes a validator script for client-side validation and an authentication script for server-side authentication.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation logic for user input. It plays a crucial role in ensuring data integrity before sending it to the server.
- **auth.py**: The Python file `auth.py` is responsible for server-side authentication processes. It manages user login, registration, and authentication tasks.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to suit the project's requirements.
   - Include the script in your HTML files using `<script src="path/to/validator.js"></script>`.

2. **auth.py**:
   - Import the `auth` module in your Python scripts to access authentication functionalities.
   - Utilize the provided functions for user registration, login, and authentication processes.

Ensure to maintain the integrity and security of user authentication data throughout the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username (alphanumeric and underscores only).
- `getPasswordStrength(password)`: Determines the strength of a password and returns a corresponding level.

**Usage:** To use this file, import `InputValidator` class from `validator.js` and call the desired validation functions or password strength function.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON handling (not used in this file).
- `datetime`: For working with date and time.
- `timedelta`: For calculating time differences.
- `typing`: For type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-17 15:16:18*
