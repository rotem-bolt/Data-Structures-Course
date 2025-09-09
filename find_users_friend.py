from FriendsHashTable import FriendsHashTable
from AVLTree import AVLTree

def find_users_friend(friends_hash: FriendsHashTable, tree: AVLTree):
    """
    Find a user's friends, show their names, then allow viewing details of a selected friend
    """
    print("\n=== Find Users & Friends ===")
    
    try:
        # Step 1: Ask for user ID
        user_id = int(input("Enter user ID to see their friends: "))
        
        # Check if user exists
        user = tree.search(user_id)
        if user is None:
            print(f"Error: User {user_id} does not exist in the system")
            return
        
        # Step 2: Get and show all friends names
        friends_ids = friends_hash.get_friends(user_id)
        
        print(f"\nUser: {user.first_name} {user.last_name} (ID: {user_id})")
        
        if not friends_ids:
            print(f"{user.first_name} has no friends yet")
            return
        
        print(f"\n{user.first_name}'s Friends:")
        friends_list = {}
        for friend_id in friends_ids:
            friend = tree.search(friend_id)
            if friend:
                friends_list[friend_id] = friend
                print(f"{friend_id}. {friend.first_name} {friend.last_name}")
            else:
                print(f"ID {friend_id} - User not found")
        
        if not friends_list:
            print("No valid friends found")
            return
        
        # Step 3: Ask which friend to see details for
        print(f"\nEnter the id of the friend whose details you want to see:")
        choice = int(input("Choice: "))
        
        selected_friend = friends_list[choice]
        
        if selected_friend:
            # Step 4: Show selected friend's details
            print(f"\n=== Friend Details ===")
            selected_friend.show_profile()
        else:
            print("Invalid choice")
            
    except ValueError:
        print("Error: Please enter valid numbers")
    except Exception as e:
        print(f"Error in find users friend: {e}")
