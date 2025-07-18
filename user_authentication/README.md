# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` for client-side input validation in JavaScript and `auth.py` for server-side authentication logic in Python.

## Key Files
- `validator.js`: This file contains client-side validation logic written in JavaScript to ensure that user input meets specified criteria before submitting it to the server.
- `auth.py`: The `auth.py` file is responsible for server-side authentication tasks in Python. It manages user authentication, login, and authorization processes within the application.

## Usage
1. **validator.js**: To use the client-side validation logic provided in `validator.js`, include the script in your HTML file using `<script src="path/to/validator.js"></script>`. Then, call the appropriate validation functions on user input fields to ensure data integrity.
   
2. **auth.py**: Utilize the authentication functionalities provided in `auth.py` by importing the necessary functions into your Python scripts. Implement user authentication, login, and authorization processes as needed within your application using the functions defined in this file.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as password strength assessment.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Calculates the strength level of a password based on various criteria.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
  - `hash_password(password: str) -> str`: Hashes a password using SHA-256.
  - `register_user(username: str, email: str, password: str) -> bool`: Registers a new user with a unique username, email, and password.
  - `login(username: str, password: str) -> Optional[str]`: Authenticates a user and returns a session token.
  - `logout(session_token: str) -> bool`: Ends a user session based on the session token.
  - `is_authenticated(session_token: str) -> bool`: Checks if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations. Call the methods to register users, login, logout, and check authentication status.

**Dependencies:** 
- `hashlib`: for hashing passwords.
- `json`: for JSON serialization.
- `datetime`: for working with dates and times.
- `timedelta`: for calculating time differences.
- `typing`: for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 05:00:08*
