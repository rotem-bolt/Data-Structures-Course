from MessageHashTable import MessageHashTable
from AVLTree import AVLTree

def add_like(messages_hash: MessageHashTable, tree: AVLTree):
    """
    Add a like to a message
    Asks for user ID and message ID, then likes the message
    """
    print("\n=== Add Like ===")
    
    try:
        like_user_id = int(input("Enter like user ID: "))
        user_id = int(input("Enter user ID: "))

        if like_user_id == user_id:
            print("Error: You cannot like your own message")
            return
        
        # Check if user exists
        user = tree.search(user_id)
        if user is None:
            print(f"Error: User {user_id} does not exist in the system")
            return

        like_user = tree.search(like_user_id)
        if like_user is None:
            print(f"Error: User {like_user_id} does not exist in the system")
            return
        
        message_id = int(input("Enter message ID: "))
        
        # Find the message
        message = messages_hash.get_message(user_id, message_id)
        if message is None:
            print(f"Error: Message ID {message_id} not found for user {user_id}")
            return
        
        print(f"User: {user.first_name} {user.last_name} (ID: {user_id})")
        print(f"Message: {message.get_message_text()}")
        print(f"Current Likes: {message.get_likes()}")
        
        # Add like to the message
        message.get_likes().append(like_user_id)
        print("Message liked!")
        print(f"New like status: {message.get_likes()}")
        
        return
        
    except ValueError:
        print("Error: Please enter valid numbers for user ID and message ID")
        return
    except Exception as e:
        print(f"Error adding like: {e}")
        return