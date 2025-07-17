# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication processes.

## Structure
The folder is organized to handle user authentication tasks efficiently. It consists of two key files: `validator.js` for client-side input validation written in JavaScript and `auth.py` for server-side authentication logic written in Python.

## Key Files
- **validator.js**: This file contains client-side validation logic to ensure that user input meets specified criteria before submission. It plays a crucial role in maintaining data integrity and security.
  
- **auth.py**: The `auth.py` file is responsible for handling server-side authentication processes. It manages user login, registration, and authentication, ensuring secure access to the application.

## Usage
To utilize the functionalities provided in this folder:
1. Modify the validation criteria in `validator.js` according to the project requirements.
2. Implement the authentication logic in `auth.py` to suit the specific authentication needs of the application.
3. Ensure that both client-side and server-side validations work seamlessly together to provide a secure and user-friendly authentication experience.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication. It provides methods to validate email addresses, passwords, and usernames, as well as determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username allowing only alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Determines the strength of a password based on its length and character composition.

**Usage:** To use this file, import `InputValidator` class in your code. For example:
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
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: Used for hashing passwords.
- `json`: Not used in this file but imported.
- `datetime`: Used for handling date and time operations.
- `timedelta`: Used for calculating time differences.
- `typing`: Used for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-17 20:27:25*
