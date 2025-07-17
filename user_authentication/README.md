# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. These files handle user validation and authentication processes.

## Structure
The folder is organized to separate the validation logic implemented in `validator.js` (JavaScript) and the authentication functionality in `auth.py` (Python).

## Key Files
- **validator.js**: This JavaScript file contains the logic for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
  
- **auth.py**: The Python file `auth.py` is responsible for handling user authentication processes. It manages user login, registration, and authentication within the system.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to suit the project's requirements.
   - Integrate the validation functions into the user input forms to ensure data integrity.

2. **auth.py**:
   - Use the provided functions to authenticate users during login and registration processes.
   - Customize the authentication logic to align with the project's security standards.

Ensure that any modifications made to these files adhere to the project's authentication guidelines and security protocols.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of a password and returns a descriptive level.

**Usage:** To use this file, import `InputValidator` class in your code and call the validation functions as needed.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Import the `UserAuth` class from this file to handle user authentication in your Python application.

**Dependencies:**
- `hashlib`: Used for hashing passwords.
- `json`: Used for JSON serialization (not utilized in this code).
- `datetime`: Used for working with dates and times.
- `timedelta`: Used for calculating time differences.
- `typing`: Used for type hints (not utilized in this code).

---
*Auto-generated documentation - Last updated: 2025-07-17 16:49:14*
