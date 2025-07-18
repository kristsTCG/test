# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. These files handle user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes validator.js for client-side validation written in JavaScript and auth.py for server-side authentication written in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic for user inputs. It plays a crucial role in ensuring data integrity and security on the front end.
  
- **auth.py**: The `auth.py` file is responsible for server-side authentication processes. It manages user authentication, login, and session handling on the backend.

## Usage
1. **validator.js**:
   - To use the client-side validation logic, include `validator.js` in your HTML file using a script tag.
   - Modify the validation rules and error messages as needed for your project.
   - Call the validation functions on user input events to validate form fields.

2. **auth.py**:
   - Import `auth.py` in your Python project to leverage its authentication functionalities.
   - Use the provided functions for user login, authentication, and session management.
   - Customize the authentication logic to fit your project's requirements.

Ensure to maintain the integrity and security of user authentication processes while working with the code in this folder.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long, alphanumeric, and contains underscores only.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user's session.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** This file can be imported to implement user authentication in Python applications.

**Dependencies:**
- `hashlib`: For hashing functions.
- `json`: For JSON handling.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 01:34:11*
