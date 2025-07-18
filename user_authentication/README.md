# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic for user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before submission.
  
- **auth.py**: The `auth.py` file contains server-side authentication logic written in Python. It manages user authentication processes, such as login, registration, and password management.

## Usage
1. To utilize the client-side validation provided by `validator.js`, include the script in your HTML file using `<script src="path/to/validator.js"></script>`. Then, call the validation functions as needed in your front-end code.

2. For server-side authentication functionalities, import and use the `auth.py` module in your Python backend code. This file provides functions for handling user authentication tasks securely.

3. Ensure that both client-side and server-side authentication logic work together seamlessly to provide a robust user authentication system within your project.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength level of a password based on length and character types.

**Usage:** Import `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file provides a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and not expired.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization and deserialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 08:58:44*
