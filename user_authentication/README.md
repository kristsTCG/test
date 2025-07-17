# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. These files handle validation and authentication processes for user accounts.

## Structure
The folder is organized to separate the validation logic implemented in `validator.js` (JavaScript) and the authentication logic in `auth.py` (Python).

## Key Files
- **validator.js**: This file contains the validation logic for user inputs, ensuring that data entered by users meets the required criteria. It plays a crucial role in maintaining data integrity and security.
  
- **auth.py**: The `auth.py` file is responsible for handling user authentication processes. It manages user login, registration, and authentication using secure methods to verify user identities.

## Usage
1. **validator.js**:
   - To use the validation functions in `validator.js`, import the file into your JavaScript code.
   - Call the appropriate validation functions provided in `validator.js` to validate user inputs such as email addresses, passwords, etc.

2. **auth.py**:
   - Import the `auth.py` file into your Python code to access the authentication functionalities.
   - Utilize the functions defined in `auth.py` for user registration, login, and authentication processes within your application.

Ensure that you follow the guidelines and best practices implemented in these files to maintain secure user authentication within your project.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication system.

**Dependencies:** None.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by deleting the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization and deserialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 19:13:19*
