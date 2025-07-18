# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This functionality is crucial for managing user access and security.

## Structure
The folder is organized to handle user authentication tasks efficiently. It includes validator.js for client-side validation and auth.py for server-side authentication logic.

## Key Files
1. **validator.js**: This JavaScript file contains client-side validation logic for user inputs. It plays a crucial role in ensuring that user-provided data meets the required criteria before submission.
   
2. **auth.py**: The Python file `auth.py` is responsible for server-side authentication processes. It manages user authentication, login, and session handling within the application.

## Usage
1. **validator.js**:
   - To use the validator.js file, include it in your HTML file using a script tag.
   - Utilize the functions provided in validator.js to validate user inputs on the client side before form submission.

2. **auth.py**:
   - Import the `auth` module in your Python code to access authentication functionalities.
   - Use the functions defined in auth.py to handle user authentication, login, and session management on the server side.

Ensure that both client-side and server-side authentication processes are in sync to maintain a secure user authentication system.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including validating email, password, and username formats, as well as checking password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username with alphanumeric and underscore characters.
- `getPasswordStrength(password)`: Calculates the strength of a password based on various criteria and returns a descriptive level.

**Usage:** This file can be imported into other JavaScript files using `require` or `import` statements.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session creation, and session validation.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password, returning a session token.
- `logout`: Method to end a user's session using their session token.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided by this file.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 05:33:54*
