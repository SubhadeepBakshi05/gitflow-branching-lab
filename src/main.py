"""
Sample Application for GitFlow Demonstration
Simulates a simple web application with user management
"""

class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, email):
        """Add a new user to the system"""
        if username in self.users:
            raise ValueError(f"User {username} already exists")

        self.users[username] = {"email": email, "active": True}
        return f"User {username} added successfully"

    def get_user(self, username):
        """Retrieve user information"""
        return self.users.get(username, None)

    def list_users(self):
        """List all active users"""
        return [
            user for user, info in self.users.items()
            if info["active"]
        ]

if __name__ == "__main__":
    manager = UserManager()
    print("User Management System initialized")

# Integration with Authentication System
from auth import AuthenticationManager

class SecureUserManager(UserManager):
 def __init__(self):
 super().__init__()
 self.auth_manager = AuthenticationManager()
 
 def register_user(self, username, email, password):
 """Register user with authentication"""
 auth_result = self.auth_manager.register_user(username, password)
 result = self.add_user(username, email)
 return f"User {username} registered with authentication enabled"
 
 def login_user(self, username, password):
 """Authenticate and login user"""
 session_token = self.auth_manager.authenticate(username, password)
 return {
 "session_token": session_token,
 "user_data": self.get_user(username),
 "message": f"User {username} authenticated successfully"
 }
 
 def validate_user_session(self, session_token):
 """Validate user session for secure operations"""
 username = self.auth_manager.validate_session(session_token)
 if username:
 return {
 "valid": True,
 "username": username,
 "user_data": self.get_user(username)
 }
 return {"valid": False, "message": "Invalid or expired session"}

if __name__ == "__main__":
 secure_manager = SecureUserManager()
 print("Secure User Management System initialized")
 
 secure_manager.register_user("test_user", "test@example.com", "secure_password123")
 login_result = secure_manager.login_user("test_user", "secure_password123")
 print(f"Login successful: {login_result['message']}")
 
 validation = secure_manager.validate_user_session(login_result["session_token"])
 print(f"Session validation: {validation['valid']}")
