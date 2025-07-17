"""
User authentication system with login and registration functionality.
"""

import hashlib
import json
from datetime import datetime, timedelta
from typing import Optional, Dict

class UserAuth:
    def __init__(self):
        self.users = {}
        self.active_sessions = {}
    
    def hash_password(self, password: str) -> str:
        """Hash password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register_user(self, username: str, email: str, password: str) -> bool:
        """Register a new user."""
        if username in self.users:
            return False
        
        self.users[username] = {
            'email': email,
            'password': self.hash_password(password),
            'created_at': datetime.now().isoformat(),
            'last_login': None
        }
        return True
    
    def login(self, username: str, password: str) -> Optional[str]:
        """Authenticate user and return session token."""
        if username not in self.users:
            return None
        
        if self.users[username]['password'] != self.hash_password(password):
            return None
        
        # Generate session token
        session_token = hashlib.md5(f"{username}{datetime.now()}".encode()).hexdigest()
        
        self.active_sessions[session_token] = {
            'username': username,
            'expires': datetime.now() + timedelta(hours=24)
        }
        
        self.users[username]['last_login'] = datetime.now().isoformat()
        return session_token
    
    def logout(self, session_token: str) -> bool:
        """End user session."""
        if session_token in self.active_sessions:
            del self.active_sessions[session_token]
            return True
        return False
    
    def is_authenticated(self, session_token: str) -> bool:
        """Check if session is valid."""
        if session_token not in self.active_sessions:
            return False
        
        session = self.active_sessions[session_token]
        if datetime.now() > session['expires']:
            del self.active_sessions[session_token]
            return False
        
        return True