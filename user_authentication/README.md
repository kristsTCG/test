# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities within the project. This includes validation of user input and authentication logic.

## Structure
The folder is organized to handle user authentication tasks. It contains two key files: `validator.js` written in JavaScript and `auth.py` written in Python.

## Key Files
- **validator.js**: This file contains functions for validating user input data. It plays a crucial role in ensuring that user-provided information meets the required criteria for authentication.
- **auth.py**: This Python file handles the authentication logic for users. It is responsible for verifying user credentials and granting access to authenticated users.

## Usage
To utilize the functionalities provided in this folder:
1. Review the `validator.js` file to understand the validation rules applied to user input.
2. Explore the `auth.py` file to understand the authentication process and how user credentials are verified.
3. Integrate these files into your project to enable user authentication features.

---

# Files Documentation

## validator.js

**Purpose:** This file contains input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine the strength of a password.

**Key Components:**
- `validateEmail(email)`: Validates the format of an email address using a regular expression.
- `validatePassword(password)`: Validates a password based on specific criteria (at least 8 characters with uppercase, lowercase, and number).
- `validateUsername(username)`: Validates a username for length (3-20 characters) and allowed characters (alphanumeric and underscores only).
- `getPasswordStrength(password)`: Determines the strength of a password based on length and character types.

**Usage:** To use this file, import `InputValidator` class where input validation is needed.

```javascript
const InputValidator = require('./validator.js');

// Example usage
if (InputValidator.validateEmail('test@example.com')) {
    console.log('Valid email address');
}

const passwordStrength = InputValidator.getPasswordStrength('SecurePassword123');
console.log(`Password strength: ${passwordStrength}`);
```

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

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:** 
- `hashlib` for hashing functions.
- `json` for JSON serialization and deserialization.
- `datetime` for working with dates and times.
- `typing` for type hints.

---
*Auto-generated documentation - Last updated: 2025-07-18 00:27:33*
