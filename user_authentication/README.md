# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This module handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication features efficiently. It includes validator.js for client-side validation and auth.py for server-side authentication logic.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation functions to ensure that user input meets specified criteria before submission.
- **auth.py**: The Python file `auth.py` is responsible for server-side authentication processes, such as verifying user credentials and managing user sessions.

## Usage
1. **validator.js**:
   - Modify or add validation functions as needed to enforce specific input requirements on the client side.
   - Include the `validator.js` file in your HTML templates using `<script>` tags.

2. **auth.py**:
   - Implement additional authentication logic or customize existing functions to suit your project's requirements.
   - Integrate the authentication functionality into your server-side codebase by importing and utilizing the `auth.py` module.

Ensure that both client-side and server-side authentication components work seamlessly together to provide a secure and user-friendly authentication experience for your application.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Calculates the strength level of a password.

**Usage:** To use this file, import `InputValidator` class in your code:
```javascript
const InputValidator = require('./validator.js');
```
Then, you can use the validation methods like `InputValidator.validateEmail('example@email.com')`.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 22:35:24*
