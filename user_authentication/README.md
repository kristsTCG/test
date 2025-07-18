# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionality in the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks efficiently. It contains two key files: `validator.js` for client-side input validation in JavaScript and `auth.py` for server-side authentication logic in Python.

## Key Files
- `validator.js`: This file contains client-side validation logic for user input. It plays a crucial role in ensuring that user-provided data meets the required criteria before submission.
- `auth.py`: This file handles server-side authentication processes, such as verifying user credentials and managing user sessions. It is essential for securing user access to the application.

## Usage
1. To utilize the client-side validation functionality, refer to `validator.js`. Modify or extend the validation rules as needed to suit the project requirements.
2. For server-side authentication tasks, consult `auth.py`. Implement additional authentication methods or customize the existing logic to align with the project's authentication requirements.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates the strength of a password based on length, uppercase, lowercase, and numbers.
- `validateUsername(username)`: Validates the format of a username, allowing only alphanumeric characters and underscores within a specific length range.
- `getPasswordStrength(password)`: Calculates the strength of a password based on length and character types, returning a descriptive level.

**Usage:** To use this file, import `InputValidator` class and call the desired validation functions or password strength calculation function.

```javascript
const InputValidator = require('./validator.js');

const email = 'example@email.com';
const isEmailValid = InputValidator.validateEmail(email);

const password = 'SecurePassword123';
const isPasswordStrong = InputValidator.validatePassword(password);

const username = 'user123';
const isUsernameValid = InputValidator.validateUsername(username);

const passwordStrength = InputValidator.getPasswordStrength(password);
```

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user and generate a session token for active sessions.
- `logout`: Method to end a user session based on the session token.
- `is_authenticated`: Method to check if a session token is valid and still active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 09:25:02*
