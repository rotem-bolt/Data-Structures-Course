from AVLTree import AVLTree
from MessageHashTable import MessageHashTable
from FriendsHashTable import FriendsHashTable
from data_structures_starter import friends_data, load_friends, load_messages, load_users, messages_data, users_data, likes_data

# Import the function files
from add_user import add_user
from find_user import find_user
from add_friend import add_friend
from find_friend import find_friend
from add_message import add_message
from find_message import find_message
from add_like import add_like

if __name__ == '__main__':
    # Start of the system - initialize data structures
    Tree = AVLTree()
    load_users(Tree, users_data)

    msg_counter = 0
    MessagesHash = MessageHashTable()
    MessagesHash, msg_counter = load_messages(MessagesHash, messages_data, msg_counter)

    FriendsHash = FriendsHashTable()
    load_friends(FriendsHash, friends_data)

    print("=== Social Media System ===")
    print("Data loaded successfully!")
    print(f"Message counter after loading: {msg_counter}")

    # Example function calls (commented out to avoid user input during testing)
    
    #1 function - Add new user
    add_user(Tree)

    #2 function of the system - Find user
    find_user(Tree)

    #3 function of the system - Add friend
    add_friend(FriendsHash, Tree)

    #4 function of the system - Find friends
    find_friend(FriendsHash, Tree)

    #5 function of the system - Add message
    msg_counter = add_message(MessagesHash, Tree, msg_counter)

    #6 function of the system - Find message
    find_message(MessagesHash, Tree)

    #7 function of the system - Add/remove like
    add_like(MessagesHash, Tree)
    