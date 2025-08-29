from typing import Dict, List

class FriendsHashTable:
    """Hash table: user_id -> list of friends ids"""

    def __init__(self):
        self.table: Dict[int, List[int]] = {}

    def add_friend(self, user_id: int, friend_id: int):
        """Add a friend to a user"""
        if user_id not in self.table:
            self.table[user_id] = []
        self.table[user_id].append(friend_id)

    def get_friends(self, user_id: int) -> List[int]:
        """Get all friends of a user"""
        return self.table.get(user_id, [])

    def show_all(self):
        """Print all users and their friends"""
        for user_id, friends in self.table.items():
            print(f"\nUser {user_id}: {friends}")
