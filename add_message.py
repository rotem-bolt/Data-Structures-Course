from MessageHashTable import MessageHashTable
from Message import Message
from AVLTree import AVLTree

def add_message(messages_hash: MessageHashTable, tree: AVLTree, msg_counter: int):
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
            print(f"Error: User {user_id} does not exist in the system")
            return msg_counter  # Return original counter on error

        msg_counter += 1
        message_id = msg_counter
        
        message_text = input("Enter message text: ")
        
        # Ask about like status
        likes_input = input("Who likes this message? Enter users with comma: ").lower().strip()
        likes = likes_input.split(',')
        likes = [int(like) for like in likes]
        
        # Create new message
        new_message = Message(message_id, message_text, likes)
        
        # Add message to hash table
        messages_hash.add_message(user_id, new_message)
        
        print(f"Message added successfully!")
        print(f"User: {user.first_name} {user.last_name} (ID: {user_id})")
        print(f"Message ID: {message_id}")
        print(f"Text: {message_text}")
        print(f"Likes: {likes}")
        
        return msg_counter  # Return updated counter on success
        
    except ValueError:
        print("Error: Please enter valid numbers for user ID and message ID")
        return msg_counter  # Return original counter on error
    except Exception as e:
        print(f"Error adding message: {e}")
        return msg_counter  # Return original counter on error
