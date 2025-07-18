# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` for client-side validation written in JavaScript and `auth.py` for server-side authentication logic written in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic to ensure that user input meets specified criteria before submitting to the server. It plays a crucial role in enhancing user experience by providing real-time feedback on input fields.
  
- **auth.py**: The `auth.py` file is responsible for server-side authentication processes. It manages user login, registration, and authentication logic to ensure secure access to the application. This file interacts with the database to verify user credentials and manage user sessions.

## Usage
1. **validator.js**: To use the `validator.js` file, include it in your HTML file using a script tag. You can then call the validation functions provided in this file on your input fields to validate user input before submission.

2. **auth.py**: To utilize the `auth.py` file, ensure it is integrated into your server-side codebase. You can call the authentication functions defined in this file to handle user login, registration, and authentication processes. Make sure to configure the database connection settings within this file for seamless operation.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Determines the strength level of a password based on length and character requirements.

**Usage:** To use this file, import `InputValidator` class into your code and call the desired validation functions as needed.

**Dependencies:** No external dependencies are required for using the functionalities provided in this file.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user's session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with date and time.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 01:38:48*
