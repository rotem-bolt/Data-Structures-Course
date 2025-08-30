from MessageHashTable import MessageHashTable
from AVLTree import AVLTree

def add_like(messages_hash: MessageHashTable, tree: AVLTree, likes_data: list[int]) -> list[int]:
    """
    Add a like to a message
    Asks for user ID and message ID, then likes the message
    """
    print("\n=== Add Like ===")
    
    try:
        user_id = int(input("Enter user ID: "))
        
        # Check if user exists
        user = tree.search(user_id)
        if user is None:
            print(f"Error: User {user_id} does not exist in the system")
            return likes_data
        
        message_id = int(input("Enter message ID: "))
        
        # Find the message
        message = messages_hash.get_message(user_id, message_id)
        if message is None:
            print(f"Error: Message ID {message_id} not found for user {user_id}")
            return likes_data
        
        print(f"User: {user.first_name} {user.last_name} (ID: {user_id})")
        print(f"Message: {message.get_message_text()}")
        print(f"Current like status: {message.get_is_liked()}")
        
        # Check if already liked
        if message.get_is_liked():
            print("Message is already liked!")
            return likes_data
        
        # Add like to the message
        message.is_liked = True
        likes_data.append(message_id)  # Add to likes tracking list
        print("Message liked!")
        print(f"New like status: {message.get_is_liked()}")
        
        return likes_data
        
    except ValueError:
        print("Error: Please enter valid numbers for user ID and message ID")
        return likes_data
    except Exception as e:
        print(f"Error adding like: {e}")
        return likes_data