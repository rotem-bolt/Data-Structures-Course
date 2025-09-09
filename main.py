from AVLTree import AVLTree
from MessageHashTable import MessageHashTable
from FriendsHashTable import FriendsHashTable
from data_structures_starter import friends_data, load_friends, load_messages, load_users, messages_data, users_data

# Import the function files
from add_user import add_user
from find_user import find_user
from add_friend import add_friend
from find_friend import find_friend
from add_message import add_message
from find_message import find_message
from add_like import add_like
from delete_user import delete_user
from update_user import update_user
from show_user_friends import show_user_friends
from find_users_friend import find_users_friend

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

    # Menu system with do-while loop
    while True:
        print("\n" + "="*50)
        print("           SOCIAL MEDIA SYSTEM MENU")
        print("="*50)
        print("1. Add new user")
        print("2. Find user")
        print("3. Update user")
        print("4. Delete user")
        print("5. Add friend")
        print("6. Find friends")
        print("7. Show user friends")
        print("8. Find user's friends")
        print("9. Add message")
        print("10. Find message")
        print("11. Add like")
        print("E. Exit")
        print("="*50)
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_user(Tree)
        elif choice == '2':
            find_user(Tree)
        elif choice == '3':
            update_user(Tree)
        elif choice == '4':
            delete_user(Tree, FriendsHash)
        elif choice == '5':
            add_friend(FriendsHash, Tree)
        elif choice == '6':
            find_friend(FriendsHash, Tree)
        elif choice == '7':
            show_user_friends(FriendsHash, Tree)
        elif choice == '8':
            find_users_friend(FriendsHash, Tree)
        elif choice == '9':
            msg_counter = add_message(MessagesHash, Tree, msg_counter)
        elif choice == '10':
            find_message(MessagesHash, Tree)
        elif choice == '11':
            add_like(MessagesHash, Tree)
        elif choice.lower() == 'e':
            print("\nThank you for using Social Media System!")
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice! Please enter 1-11 or E to exit.")
    