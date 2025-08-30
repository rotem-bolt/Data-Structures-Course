from MessageHashTable import MessageHashTable
from AVLTree import AVLTree

def add_like(messages_hash: MessageHashTable, tree: AVLTree) -> None:
    """
    Add or remove a like from a message
    Asks for user ID and message ID, then toggles the like status
    """
    print("\n=== Add/Remove Like ===")
    
    try:
        user_id = int(input("Enter user ID: "))
        
        # Check if user exists
        user = tree.search(user_id)
        if user is None:
            print(f"❌ Error: User {user_id} does not exist in the system")
            return
        
        message_id = int(input("Enter message ID: "))
        
        # Find the message
        message = messages_hash.get_message(user_id, message_id)
        if message is None:
            print(f"❌ Error: Message ID {message_id} not found for user {user_id}")
            return
        
        print(f"User: {user.first_name} {user.last_name} (ID: {user_id})")
        print(f"Message: {message.get_message_text()}")
        print(f"Current like status: {message.get_is_liked()}")
        
        # Ask what to do
        choice = input("(L)ike, (U)nlike, or (T)oggle? (l/u/t): ").lower().strip()
        
        if choice == 'l' or choice == 'like':
            message.is_liked = True
            print("✅ Message liked!")
        elif choice == 'u' or choice == 'unlike':
            message.is_liked = False
            print("✅ Message unliked!")
        elif choice == 't' or choice == 'toggle':
            message.is_liked = not message.is_liked
            status = "liked" if message.is_liked else "unliked"
            print(f"✅ Message {status}!")
        else:
            print("❌ Invalid choice. Please enter 'l' for like, 'u' for unlike, or 't' for toggle")
            return
        
        print(f"New like status: {message.get_is_liked()}")
        
    except ValueError:
        print("❌ Error: Please enter valid numbers for user ID and message ID")
    except Exception as e:
        print(f"❌ Error updating like: {e}")

def toggle_message_like(messages_hash: MessageHashTable, user_id: int, message_id: int) -> bool:
    """
    Helper function to toggle like status of a message
    Returns True if successful, False if message not found
    """
    message = messages_hash.get_message(user_id, message_id)
    if message is None:
        return False
    
    message.is_liked = not message.is_liked
    return True

def set_message_like(messages_hash: MessageHashTable, user_id: int, message_id: int, like_status: bool) -> bool:
    """
    Helper function to set like status of a message
    Returns True if successful, False if message not found
    """
    message = messages_hash.get_message(user_id, message_id)
    if message is None:
        return False
    
    message.is_liked = like_status
    return True

def test_add_like():
    """Test function for add_like"""
    from data_structures_starter import users_data, messages_data, load_users, load_messages
    
    # Create test data structures
    tree = AVLTree()
    load_users(tree, users_data)
    
    messages_hash = MessageHashTable()
    load_messages(messages_hash, messages_data)
    
    print("Testing add_like function...")
    
    # Test toggling like for user 7, message 1
    message = messages_hash.get_message(7, 1)
    if message:
        original_status = message.get_is_liked()
        print(f"Message 1 for user 7 - Original like status: {original_status}")
        
        # Toggle like
        success = toggle_message_like(messages_hash, 7, 1)
        if success:
            new_status = message.get_is_liked()
            print(f"After toggle - New like status: {new_status}")

if __name__ == "__main__":
    test_add_like()
