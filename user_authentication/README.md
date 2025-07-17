# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities within the project. This includes validating user input and handling user authentication processes.

## Structure
The folder is organized to separate the validation logic in `validator.js` written in JavaScript and the authentication logic in `auth.py` written in Python.

## Key Files
- `validator.js`: This file contains the validation logic for user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before proceeding with authentication processes.
  
- `auth.py`: This file contains the authentication logic for verifying user credentials and managing user authentication within the system. It is responsible for handling user login, logout, and session management.

## Usage
1. To utilize the validation functionality, refer to `validator.js` and incorporate the validation methods into your user input processing flow.
   
2. For user authentication processes, utilize `auth.py` to handle user login, logout, and session management within your application.

3. Ensure to maintain the integrity and security of user authentication by following best practices and integrating these components securely within your project.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication. It provides methods to validate email addresses, passwords, and usernames, as well as determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase letters, lowercase letters, and numbers.
- `validateUsername(username)`: Validates the format of a username, allowing alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Calculates the strength of a password based on various criteria and returns a descriptive level.

**Usage:** To use this file, import `InputValidator` class where input validation is required and call the respective methods as needed.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, logout, and session authentication.
- `hash_password`: Method to hash a given password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user's session by removing the session token from active sessions.
- `is_authenticated`: Method to check if a session token is valid and not expired.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 23:11:46*
