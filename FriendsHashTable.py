from typing import Dict, List

class FriendsHashTable:
    """Hash table: each user_id points to a list of their friends"""

    # Create an empty dictionary (hash table)
    # Keys = user IDs (int), Values = list of friend IDs (List[int])
    def __init__(self):
        self.table: Dict[int, List[int]] = {}

    def add_friend(self, user_id: int, friend_id: int):
        """Add a friend to a user"""
        # Check if the user_id already exists
        if user_id not in self.table:
            self.table[user_id] = []
        self.table[user_id].append(friend_id)

    def get_friends(self, user_id: int):
        """Get all friends of a user"""
        return self.table.get(user_id, [])

    def show_all(self):
        """Print all users and their friends"""
        for user_id, friends in self.table.items():
            print(f"\nUser {user_id}: {friends}")
