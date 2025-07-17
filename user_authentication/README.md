# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. These files handle user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes validator.js for client-side validation written in JavaScript and auth.py for server-side authentication written in Python.

## Key Files
1. **validator.js**: This file contains client-side validation logic for user inputs. It plays a crucial role in ensuring that user-provided data meets the required criteria before sending it to the server for authentication.

2. **auth.py**: The `auth.py` file is responsible for server-side authentication processes. It handles user login, registration, and authentication using Python. This file interacts with the database to verify user credentials and manage user sessions.

## Usage
1. **validator.js**:
   - Modify the validation rules in `validator.js` to suit the specific requirements of the project.
   - Include `validator.js` in your HTML files using a script tag to enable client-side validation.

2. **auth.py**:
   - Implement additional authentication features or customize the existing ones in `auth.py` as needed.
   - Integrate `auth.py` with your backend application to enable user authentication functionalities.
   - Ensure proper error handling and secure authentication practices in the code.

By following the guidelines above, you can effectively utilize the user authentication functionalities provided in the `user_authentication` folder of the project.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including validating email, password, and username formats, as well as determining password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Determines the strength level of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class in your code and call the desired validation functions or password strength checker.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user's session by invalidating the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:** 
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hinting (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-17 17:05:01*
