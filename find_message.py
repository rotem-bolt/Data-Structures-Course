from MessageHashTable import MessageHashTable
from AVLTree import AVLTree

def find_message(messages_hash: MessageHashTable, tree: AVLTree) -> None:
    """
    Find and display a specific message for a user
    Asks for user ID and message ID, then shows the message
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
        
        # Find specific message
        message_id = int(input("Enter message ID: "))
        
        message = messages_hash.get_message(user_id, message_id)
        
        if message is None:
            print(f"Message ID {message_id} not found for user {user_id}")
            return
        
        print(f"Found message:")
        message.show_message()
            
    except ValueError:
        print("Error: Please enter valid numbers for user ID and message ID")
    except Exception as e:
        print(f"Error finding message: {e}")
