# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This module handles user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes `validator.js` for client-side validation written in JavaScript and `auth.py` for server-side authentication written in Python.

## Key Files
- `validator.js`: This file contains client-side validation logic for user inputs. It plays a crucial role in ensuring that user-provided data meets the required criteria before submission.
- `auth.py`: The `auth.py` file is responsible for server-side authentication processes. It manages user authentication, login, and session handling within the application.

## Usage
To utilize the user authentication functionality in this folder:
1. Review and understand the validation logic in `validator.js` to ensure data integrity on the client side.
2. Implement the server-side authentication logic provided in `auth.py` to manage user authentication and sessions effectively.
3. Integrate these files into your project to enable secure user authentication processes.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength of the input password based on length and character complexity.

**Usage:** Import the `InputValidator` class from this file and use its static methods for input validation and password strength assessment.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, logout, and session authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user's session by removing the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-17 17:22:10*
