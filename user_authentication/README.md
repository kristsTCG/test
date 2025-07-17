# user_authentication

## Overview
The `user_authentication` folder contains files related to user authentication functionalities in the project. These files handle user validation and authentication processes.

## Structure
The folder consists of two key files:
- `validator.js`: A JavaScript file with 1212 characters responsible for user input validation.
- `auth.py`: A Python file with 2198 characters handling user authentication logic.

## Key Files
### validator.js
This file contains functions to validate user input data, ensuring that it meets the required criteria before processing.

### auth.py
The `auth.py` file manages user authentication processes, such as login, registration, and authentication checks.

## Usage
1. To utilize the validation functions in `validator.js`, import the necessary functions into your JavaScript files and call them to validate user input data.

Example:
```javascript
import { validateUsername, validatePassword } from './validator.js';

if (validateUsername(username) && validatePassword(password)) {
    // Proceed with processing user input
} else {
    // Display error messages to the user
}
```

2. In Python scripts, import the `auth.py` file to access user authentication functionalities.

Example:
```python
from auth import login, register, authenticate

# Use the functions like login(username, password) or register(username, password) as needed
```

Ensure to follow the specific function signatures and guidelines within each file for proper usage.

---

# Files Documentation

## validator.js

**Purpose:** This file provides input validation utilities for user authentication, including email, password, and username validation, as well as a function to determine password strength.

**Key Components:**
- `validateEmail(email)`: Validates if the input email is in a valid format.
- `validatePassword(password)`: Validates if the input password meets the criteria of at least 8 characters with uppercase, lowercase, and number.
- `validateUsername(username)`: Validates if the input username is between 3-20 characters and contains only alphanumeric characters and underscores.
- `getPasswordStrength(password)`: Determines the strength of the input password based on length and character types.

**Usage:** Import the `InputValidator` class from this file to use the validation functions in your authentication logic.

**Dependencies:** No external dependencies.

## auth.py

**Purpose:** This file contains a user authentication system with login and registration functionality.

**Key Components:**
- `UserAuth`: Class that manages user registration, login, session handling, and authentication.
- `hash_password`: Method to hash a password using SHA-256.
- `register_user`: Method to register a new user with a unique username, email, and password.
- `login`: Method to authenticate a user with username and password and generate a session token.
- `logout`: Method to end a user session based on the session token.
- `is_authenticated`: Method to check if a session token is valid and the user is authenticated.

**Usage:** Instantiate the `UserAuth` class to utilize the user authentication functionalities provided in this file.

**Dependencies:**
- `hashlib`: For hashing passwords using SHA-256.
- `json`: For JSON serialization and deserialization.
- `datetime`: For working with dates and times.
- `timedelta`: For calculating time differences.
- `typing`: For type hints and annotations.

---
*Auto-generated documentation - Last updated: 2025-07-17 18:38:34*
