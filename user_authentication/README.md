# user_authentication

## Overview
The `user_authentication` folder contains code related to user authentication functionalities in the project. It includes validation logic in JavaScript and authentication logic in Python.

## Structure
The folder is organized to handle user authentication tasks. It consists of two key files: `validator.js` for input validation and `auth.py` for user authentication.

## Key Files
1. `validator.js`: This JavaScript file contains 1212 characters of code responsible for validating user inputs. It ensures that the data entered by users meets the required criteria before proceeding with authentication processes.

2. `auth.py`: The Python file `auth.py` contains 2198 characters of code dedicated to user authentication. It manages the authentication process, verifying user credentials and granting access based on the provided information.

## Usage
To utilize the functionalities provided in this folder:
- Use the `validator.js` file to validate user inputs before proceeding with authentication.
- Implement the authentication logic from `auth.py` to authenticate users within the project.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric and underscore characters.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class in your code:
```javascript
const InputValidator = require('./validator.js');
```

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user's session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and has not expired.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 04:06:49*
