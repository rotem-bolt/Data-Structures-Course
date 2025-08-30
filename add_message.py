from MessageHashTable import MessageHashTable
from Message import Message
from AVLTree import AVLTree

def add_message(messages_hash: MessageHashTable, tree: AVLTree) -> None:
    """
    Add a new message for a user
    Asks for user ID, message ID, and message text
    """
    print("\n=== Add Message ===")
    
    try:
        user_id = int(input("Enter user ID: "))
        
        # Check if user exists in the system
        user = tree.search(user_id)
        if user is None:
            print(f"❌ Error: User {user_id} does not exist in the system")
            return
        
        message_id = int(input("Enter message ID: "))
        
        # Check if message ID already exists for this user
        existing_message = messages_hash.get_message(user_id, message_id)
        if existing_message is not None:
            print(f"❌ Error: Message ID {message_id} already exists for user {user_id}")
            return
        
        message_text = input("Enter message text: ")
        
        # Ask about like status
        like_choice = input("Is this message liked? (y/n): ").lower().strip()
        is_liked = like_choice == 'y' or like_choice == 'yes'
        
        # Create new message
        new_message = Message(message_id, message_text, is_liked)
        
        # Add message to hash table
        messages_hash.add_message(user_id, new_message)
        
        print(f"✅ Message added successfully!")
        print(f"User: {user.first_name} {user.last_name} (ID: {user_id})")
        print(f"Message ID: {message_id}")
        print(f"Text: {message_text}")
        print(f"Liked: {is_liked}")
        
    except ValueError:
        print("❌ Error: Please enter valid numbers for user ID and message ID")
    except Exception as e:
        print(f"❌ Error adding message: {e}")

def test_add_message():
    """Test function for add_message"""
    from data_structures_starter import users_data, messages_data, load_users, load_messages
    
    # Create test data structures
    tree = AVLTree()
    load_users(tree, users_data[:15])  # Load first 15 users
    
    messages_hash = MessageHashTable()
    load_messages(messages_hash, messages_data)
    
    print("Current messages:")
    messages_hash.show_all()

if __name__ == "__main__":
    test_add_message()
