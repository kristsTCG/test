# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic for user input. It ensures that the data entered by the user meets the required criteria before submission.
  
- **auth.py**: This file contains server-side authentication logic written in Python. It handles user authentication processes such as login, registration, and password management.

## Usage
1. To utilize the client-side validation provided by `validator.js`, include this file in your HTML file using a script tag.
   ```html
   <script src="path/to/validator.js"></script>
   ```

2. Use the functions defined in `validator.js` to validate user input before submitting a form.
   ```javascript
   // Example usage of validator functions
   if (validateUsername(username) && validatePassword(password)) {
       // Proceed with form submission
   } else {
       // Display error messages to the user
   }
   ```

3. Incorporate the server-side authentication logic from `auth.py` into your Python application by importing the necessary functions.
   ```python
   from auth import login, register, change_password
   ```

4. Call the appropriate functions from `auth.py` to handle user authentication processes within your application.
   ```python
   # Example usage of authentication functions
   if login(username, password):
       # Redirect user to the dashboard
   else:
       # Display login error message
   ```

By following these steps, you can effectively implement user authentication features using the code provided in the `user_authentication` folder.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates a password based on specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates a username for length (3-20 characters) and alphanumeric characters and underscores only.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, and session handling.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token.
- `logout`: Method to end a user's session.
- `is_authenticated`: Method to check if a session token is valid.

**Usage:** Instantiate the `UserAuth` class to manage user authentication operations.

**Dependencies:**
- `hashlib`: For hashing functions.
- `json`: For JSON serialization.
- `datetime`: For date and time operations.
- `timedelta`: For time duration calculations.
- `typing`: For type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 00:22:28*
