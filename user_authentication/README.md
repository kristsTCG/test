# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. These files handle user validation and authentication processes.

## Structure
The folder is organized to manage user authentication tasks efficiently. It includes validator.js for client-side validation written in JavaScript and auth.py for server-side authentication written in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic for user input. It ensures that user-provided data meets specified criteria before submission.
  
- **auth.py**: The `auth.py` file handles server-side authentication processes. It manages user login, registration, and authentication against the system.

## Usage
1. **validator.js**:
   - Modify the validation rules as needed to suit the project requirements.
   - Include the `validator.js` file in your HTML pages using `<script>` tags.
   - Call the validation functions on user input events to validate form data.

2. **auth.py**:
   - Implement additional authentication logic as required by the project.
   - Integrate the authentication functions into the project's backend services.
   - Ensure proper error handling and security measures are in place to protect user data.

By following the guidelines above, you can effectively utilize the user authentication functionalities provided in this folder.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class where input validation is needed.

```javascript
const InputValidator = require('./validator.js');

// Example usage
if (InputValidator.validateEmail('example@email.com')) {
    console.log('Email is valid');
}
```

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** User authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class to manage user authentication operations.
- `hash_password(password: str) -> str`: Method to hash a password using SHA-256.
- `register_user(username: str, email: str, password: str) -> bool`: Register a new user with username, email, and password.
- `login(username: str, password: str) -> Optional[str]`: Authenticate user and return session token.
- `logout(session_token: str) -> bool`: End user session by deleting the session token.
- `is_authenticated(session_token: str) -> bool`: Check if the session token is valid.

**Usage:** Create an instance of `UserAuth` to manage user authentication. Call `register_user` to add a new user, `login` to authenticate and get a session token, `logout` to end a session, and `is_authenticated` to check session validity.

**Dependencies:** `hashlib`, `json`, `datetime`, `timedelta`, `Optional`, `Dict`.

---
*Auto-generated documentation - Last updated: 2025-07-18 04:08:21*
