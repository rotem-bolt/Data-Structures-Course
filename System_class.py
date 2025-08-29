from data_types import user_type, message_type, friends_type, likes_type
from data_structures_starte import messages_data_structure, users_data_structure, friends_data_structure, likes_data_structure

class System:
    def __init__(self):
        self.users = users_data_structure
        self.messages = messages_data_structure
        self.friends = friends_data_structure
        self.likes = likes_data_structure
        
    def add_user(self, user):
        self.users.append(user)
        return user