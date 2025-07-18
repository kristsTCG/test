# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. These files handle user validation and authentication processes.

## Structure
The folder is organized to manage user authentication features efficiently. It includes validator.js for client-side validation and auth.py for server-side authentication.

## Key Files
- **validator.js**: This JavaScript file contains client-side validation logic for user inputs. It plays a crucial role in ensuring that user-provided data meets the required criteria before submission.
  
- **auth.py**: The Python file `auth.py` is responsible for server-side authentication processes. It manages user authentication, login, and authorization within the system.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to suit the project requirements.
   - Include the `validator.js` file in your HTML pages using `<script>` tags.
   - Call the validation functions on user input events to validate form fields.

2. **auth.py**:
   - Import the `auth.py` module in your Python scripts where authentication is required.
   - Utilize the provided functions for user login, authentication, and authorization.
   - Customize the authentication logic to integrate with your existing user management system.

Ensure that both client-side and server-side authentication processes are in sync to provide a secure and seamless user experience.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and a number.
- `validateUsername(username)`: Validates if the input username is 3-20 characters long, alphanumeric, and contains underscores only.
- `getPasswordStrength(password)`: Determines the strength of the input password based on length and character types.

**Usage:** This file can be imported using `require` or `import` statements to access the input validation utilities for user authentication.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user's session.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to use the provided authentication functionalities.

**Dependencies:**
- `hashlib`: For hashing passwords.
- `json`: For JSON serialization (not used in this file).
- `datetime`: For handling date and time operations.
- `timedelta`: For calculating time differences.
- `typing`: For type hints (not used in this file).

---
*Auto-generated documentation - Last updated: 2025-07-18 04:17:00*
