from MessageHashTable import MessageHashTable
from AVLTree import AVLTree

def find_message(messages_hash: MessageHashTable, tree: AVLTree) -> None:
    """
    Find and display messages for a user
    Can find all messages for a user or a specific message
    """
    print("\n=== Find Message ===")
    
    try:
        user_id = int(input("Enter user ID: "))
        
        # Check if user exists
        user = tree.search(user_id)
        if user is None:
            print(f"Error: User {user_id} does not exist in the system")
            return
        
        print(f"User: {user.first_name} {user.last_name} (ID: {user_id})")
        
        # Ask what type of search
        choice = input("Find (a)ll messages or (s)pecific message? (a/s): ").lower().strip()
        
        if choice == 'a' or choice == 'all':
            # Find all messages for user
            user_messages = messages_hash.get_messages(user_id)
            
            if not user_messages:
                print(f"No messages found for user {user_id}")
                return
            
            print(f"Found {len(user_messages)} messages for {user.first_name}:")
            print("-" * 50)
            
            for msg_id, message in user_messages.items():
                print(f"Message ID {msg_id}:")
                print(f"  Text: {message.get_message_text()}")
                print(f"  Liked: {message.get_is_liked()}")
                print()
                
        elif choice == 's' or choice == 'specific':
            # Find specific message
            message_id = int(input("Enter message ID: "))
            
            message = messages_hash.get_message(user_id, message_id)
            
            if message is None:
                print(f"Message ID {message_id} not found for user {user_id}")
                return
            
            print(f"Found message:")
            message.show_message()
            
        else:
            print("Invalid choice. Please enter 'a' for all or 's' for specific")
            
    except ValueError:
        print("Error: Please enter valid numbers for IDs")
    except Exception as e:
        print(f"Error finding message: {e}")

def get_user_messages(messages_hash: MessageHashTable, user_id: int) -> dict:
    """
    Helper function to get all messages for a user
    Returns dictionary of message_id -> Message objects
    """
    return messages_hash.get_messages(user_id)

def get_specific_message(messages_hash: MessageHashTable, user_id: int, message_id: int):
    """
    Helper function to get a specific message
    Returns Message object or None
    """
    return messages_hash.get_message(user_id, message_id)

def test_find_message():
    """Test function for find_message"""
    from data_structures_starter import users_data, messages_data, load_users, load_messages
    
    # Create test data structures
    tree = AVLTree()
    load_users(tree, users_data)
    
    messages_hash = MessageHashTable()
    load_messages(messages_hash, messages_data)
    
    print("Testing find_message function...")
    
    # Test finding all messages for user 7
    messages = get_user_messages(messages_hash, 7)
    print(f"User 7 has {len(messages)} messages")
    
    # Test finding specific message
    message = get_specific_message(messages_hash, 7, 1)
    if message:
        print(f"Found message 1 for user 7: {message.get_message_text()}")

if __name__ == "__main__":
    test_find_message()
