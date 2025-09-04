from AVLTree import AVLTree
from FriendsHashTable import FriendsHashTable

def delete_user(tree: AVLTree, friends_hash: FriendsHashTable):
    """
    Delete a user from the system
    Removes user from AVL tree and also removes them from all friends lists
    """
    print("\n=== Delete User ===")
    
    try:
        user_id = int(input("Enter user ID to delete: "))
        
        # Check if user exists
        user = tree.search(user_id)
        if user is None:
            print(f"Error: User {user_id} does not exist in the system")
            return
        
        # Show user info and confirm deletion
        print(f"Found user to delete:")
        user.show_profile()
        
        confirm = input("Are you sure you want to delete this user? (yes/no): ").lower().strip()
        if confirm not in ['yes', 'y', 'Yes', 'Y', 'Yes', 'YES']:
            print("User deletion cancelled")
            return
        
        # Get user's friends list before deletion
        user_friends = friends_hash.get_friends(user_id)
        
        # Remove this user from all their friends' friend lists
        for friend_id in user_friends:
            friend_friends = friends_hash.get_friends(friend_id)
            if user_id in friend_friends:
                friend_friends.remove(user_id)
        
        # Remove user's own friend list
        if user_id in friends_hash.table:
            del friends_hash.table[user_id]
        
        # Remove user from AVL tree
        if tree.delete(user_id):
            print(f"User {user.first_name} {user.last_name} (ID: {user_id}) has been successfully deleted from the system")
        else:
            print(f"Error: Could not remove user {user_id} from AVL tree")
        
        print(f"Removed user from {len(user_friends)} friend lists")
        
    except ValueError:
        print("Error: Please enter a valid number for user ID")
    except Exception as e:
        print(f"Error deleting user: {e}")

def remove_user_from_friends(friends_hash: FriendsHashTable, user_id: int) -> int:
    """
    Helper function to remove a user from all friends lists
    Returns the number of friend lists the user was removed from
    """
    removed_count = 0
    
    # Go through all users in the friends table
    for current_user_id, friends_list in friends_hash.table.items():
        if user_id in friends_list:
            friends_list.remove(user_id)
            removed_count += 1
    
    # Remove the user's own friend list if it exists
    if user_id in friends_hash.table:
        del friends_hash.table[user_id]
    
    return removed_count
