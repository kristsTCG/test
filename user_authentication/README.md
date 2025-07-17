# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic for user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before submission.
  
- **auth.py**: The `auth.py` file contains server-side authentication logic implemented in Python. It manages user authentication processes such as login, registration, and session management.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to match the project's requirements.
   - Include the `validator.js` file in your HTML pages using `<script>` tags.
   - Call the validation functions from your form submission events to validate user input.

2. **auth.py**:
   - Configure the authentication settings such as database connections and encryption methods.
   - Import the `auth.py` module in your main application file to utilize the authentication functionalities.
   - Implement user authentication flows using the provided functions in `auth.py`.

Ensure that both client-side and server-side authentication mechanisms work seamlessly together to provide a secure and user-friendly authentication experience.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including validating email, password, and username formats, as well as determining the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numeric characters.
- `validateUsername(username)`: Validates the format of a username, allowing only alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and the presence of different character types.

**Usage:** Import the `InputValidator` class from this file to use the provided validation methods in your authentication logic.

**Dependencies:** No external dependencies required for this file.

## auth.py

**Purpose:** This file provides a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user's session by deleting the session token.
- `is_authenticated`: Method to check if a session token is valid and not expired.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For working with JSON data.
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 22:50:37*
