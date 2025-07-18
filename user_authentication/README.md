# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This module is responsible for validating user input and handling user authentication using both JavaScript and Python.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` for client-side input validation in JavaScript and `auth.py` for server-side authentication in Python.

## Key Files
- **validator.js**: This JavaScript file (1212 characters) is crucial for client-side input validation. It ensures that user input meets the required criteria before submitting it for authentication.
  
- **auth.py**: This Python file (2198 characters) is essential for server-side authentication. It manages user authentication processes, such as verifying credentials and granting access to authorized users.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to suit the project's requirements.
   - Include this file in the client-side code to validate user input before sending it for authentication.

2. **auth.py**:
   - Implement additional authentication logic as required by the project.
   - Integrate this file into the server-side code to handle user authentication processes effectively.

Ensure that both files work together seamlessly to provide a secure and reliable user authentication system.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3 to 20 characters long, containing only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character complexity.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization and deserialization.
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 08:40:29*
