"""
Simple user management system for testing AI analysis
"""

class UserManager:
    def __init__(self):
        self.users = []
        self.next_id = 1
    
    def add_user(self, name, email):
        """Add a new user to the system with email validation"""
        if not email or '@' not in email:
            raise ValueError("Invalid email address")
        
        user = {
            'id': self.next_id,
            'name': name,
            'email': email,
            'active': True
        }
        self.users.append(user)
        self.next_id += 1
        return user
    
    def get_user_by_id(self, user_id):
        """Find user by ID"""
        for user in self.users:
            if user['id'] == user_id:
                return user
        return None
    
    def find_user_by_email(self, email):
        """Find user by email address"""
        for user in self.users:
            if user['email'].lower() == email.lower():
                return user
        return None
    
    def get_active_users(self):
        """Get all active users"""
        return [user for user in self.users if user['active']]
    
    def deactivate_user(self, user_id):
        """Deactivate a user instead of deleting"""
        user = self.get_user_by_id(user_id)
        if user:
            user['active'] = False
            return True
        return False

# Example usage
if __name__ == "__main__":
    manager = UserManager()
    
    # Add some test users with validation
    try:
        user1 = manager.add_user("John Doe", "john@example.com")
        user2 = manager.add_user("Jane Smith", "jane@example.com")
        print(f"Created users: {len(manager.users)}")
    except ValueError as e:
        print(f"Error creating user: {e}")
    
    # Test email search
    found_user = manager.find_user_by_email("john@example.com")
    if found_user:
        print(f"Found user: {found_user['name']}")
    
    print(f"Active users: {len(manager.get_active_users())}")
    
    # Deactivate a user
    manager.deactivate_user(1)
    print(f"Active users after deactivation: {len(manager.get_active_users())}")