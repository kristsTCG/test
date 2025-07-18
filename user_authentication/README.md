# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and handling user authentication using JavaScript and Python.

## Structure
The folder is organized to handle user authentication tasks. It contains two key files: `validator.js` for client-side input validation using JavaScript and `auth.py` for server-side authentication logic using Python.

## Key Files
1. `validator.js`: This JavaScript file is responsible for client-side input validation in the user authentication process. It contains functions to validate user input such as email addresses, passwords, and other form fields.
   
2. `auth.py`: The Python file `auth.py` handles server-side authentication tasks. It includes functions for user login, registration, password hashing, and authentication checks.

## Usage
To utilize the code in this folder:
- Use `validator.js` functions to validate user input on the client-side before submitting forms.
- Integrate `auth.py` functions into the server-side logic to handle user authentication processes such as login, registration, and password management.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address.
- `validatePassword(password)`: Validates the strength of a password based on specific criteria.
- `validateUsername(username)`: Validates the format of a username.
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character requirements.

**Usage:** To use this file, import `InputValidator` class in your code and call the validation functions as needed.

```javascript
const InputValidator = require('./validator.js');

console.log(InputValidator.validateEmail('example@email.com')); // true
console.log(InputValidator.validatePassword('StrongP@ssw0rd')); // true
console.log(InputValidator.validateUsername('user123')); // true
console.log(InputValidator.getPasswordStrength('WeakPwd')); // 'Weak'
```

**Dependencies:** This file does not have any external dependencies.

## auth.py

**Purpose:** This file implements a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with a username and password and generate a session token.
- `logout`: Method to end a user session based on the session token.
- `is_authenticated`: Method to check if a session token is valid and active.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For handling JSON data.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-18 05:31:20*
