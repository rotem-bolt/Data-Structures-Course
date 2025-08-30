from FriendsHashTable import FriendsHashTable
from AVLTree import AVLTree

def add_friend(friends_hash: FriendsHashTable, tree: AVLTree) -> None:
    """
    Add a friendship between two users
    Asks for user IDs and creates friendship in both directions
    """
    print("\n=== Add Friend ===")
    
    try:
        user_id = int(input("Enter user ID: "))
        friend_id = int(input("Enter friend ID: "))
        
        # Check if both users exist in the system
        user = tree.search(user_id)
        friend = tree.search(friend_id)
        
        if user is None:
            print(f"Error: User {user_id} does not exist in the system")
            return
            
        if friend is None:
            print(f"Error: User {friend_id} does not exist in the system")
            return
            
        if user_id == friend_id:
            print("Error: Cannot add yourself as a friend")
            return
        
        # Check if they're already friends
        current_friends = friends_hash.get_friends(user_id)
        if friend_id in current_friends:
            print(f"Users {user_id} and {friend_id} are already friends")
            return
        
        # Add friendship in both directions
        friends_hash.add_friend(user_id, friend_id)
        friends_hash.add_friend(friend_id, user_id)
        
        print(f"Friendship added between {user.first_name} ({user_id}) and {friend.first_name} ({friend_id})")
        
    except ValueError:
        print("Error: Please enter valid numbers for user IDs")
    except Exception as e:
        print(f"Error adding friendship: {e}")
