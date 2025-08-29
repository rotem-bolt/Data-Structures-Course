from typing import Dict
from Messages import Message

class MessageHashTable:
    """Hash table: user_id -> hash table of messages"""

    def __init__(self):
        # טבלת גיבוב ראשית: לכל user_id יש טבלת גיבוב פנימית
        self.table: Dict[int, Dict[int, Message]] = {}

    def add_message(self, user_id: int, message: Message):
        """Add a message to a user (into inner hash table)"""
        if user_id not in self.table:
            self.table[user_id] = {}   # יצירת טבלת גיבוב פנימית
        self.table[user_id][message.get_id()] = message

    def get_messages(self, user_id: int) -> Dict[int, Message]:
        """Get all messages of a user (returns inner hash table)"""
        return self.table.get(user_id, {})

    def get_message(self, user_id: int, message_id: int) -> Message:
        """Find specific message by id from inner hash table"""
        return self.table.get(user_id, {}).get(message_id, None)

    def show_all(self):
        """Print all users and their messages"""
        for user_id, messages in self.table.items():
            print(f"\nUser {user_id}:")
            for msg_id, msg in messages.items():
                msg.show_message()