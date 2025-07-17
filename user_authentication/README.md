# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. It handles validation of user input and authentication processes.

## Structure
The folder is organized to separate the validation logic implemented in `validator.js` (JavaScript) and the authentication functionality in `auth.py` (Python).

## Key Files
- **validator.js**: This file contains the JavaScript code for validating user input. It plays a crucial role in ensuring that user data meets the required criteria before proceeding with authentication.
  
- **auth.py**: The `auth.py` file contains the Python code responsible for handling user authentication processes. It manages user login, registration, and authentication within the system.

## Usage
1. **validator.js**: To use the validation logic provided in `validator.js`, import the necessary functions into your JavaScript files. Call the appropriate validation functions on user input data to ensure it meets the required criteria.

2. **auth.py**: Utilize the functions defined in `auth.py` to implement user authentication features in your Python application. Import the necessary functions to handle user registration, login, and authentication processes effectively.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates an email address using a regular expression.
- `validatePassword(password)`: Validates a password based on length and character requirements.
- `validateUsername(username)`: Validates a username for length and character restrictions.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character complexity.

**Usage:** To use this file, import `InputValidator` class where needed and call the respective validation functions or password strength function.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user's session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your Python application.

**Dependencies:**
- `hashlib`: For hashing functions.
- `json`: For JSON serialization.
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 20:08:16*
