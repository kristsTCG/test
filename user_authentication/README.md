# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` for client-side input validation using JavaScript and `auth.py` for server-side authentication logic written in Python.

## Key Files
1. **validator.js**: This file contains client-side validation logic to ensure that user input meets specified criteria before submitting it to the server. It plays a crucial role in enhancing user experience by providing real-time feedback on input errors.

2. **auth.py**: The `auth.py` file is responsible for handling server-side authentication processes. It manages user login, registration, and authentication using Python. This file ensures secure access to the application by verifying user credentials.

## Usage
To utilize the functionalities provided in the `user_authentication` folder:
1. Modify the validation criteria in `validator.js` to suit the project's requirements.
2. Implement the server-side authentication logic in `auth.py` to authenticate users securely.
3. Ensure that both client-side and server-side components work seamlessly together to provide a robust user authentication system.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of being at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long, alphanumeric, and contains underscores only.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user's session.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization and deserialization.
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hinting in Python code.

---
*Auto-generated documentation - Last updated: 2025-07-17 19:53:10*
