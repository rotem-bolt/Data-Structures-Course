from FriendsHashTable import FriendsHashTable
from AVLTree import AVLTree

def find_friend(friends_hash: FriendsHashTable, tree: AVLTree) -> None:
    """
    Find and display all friends of a user
    Asks for user ID and shows list of friends with their details
    """
    print("\n=== Find Friends ===")
    
    try:
        user_id = int(input("Enter user ID to find their friends: "))
        
        # Check if user exists
        user = tree.search(user_id)
        if user is None:
            print(f"❌ Error: User {user_id} does not exist in the system")
            return
        
        # Get friends list
        friends_ids = friends_hash.get_friends(user_id)
        
        if not friends_ids:
            print(f"User {user.first_name} {user.last_name} (ID: {user_id}) has no friends")
            return
        
        print(f"✅ Friends of {user.first_name} {user.last_name} (ID: {user_id}):")
        print("-" * 50)
        
        for friend_id in friends_ids:
            friend = tree.search(friend_id)
            if friend:
                print(f"  • ID {friend_id}: {friend.first_name} {friend.last_name}")
            else:
                print(f"  • ID {friend_id}: (User not found in system)")
        
        print(f"\nTotal friends: {len(friends_ids)}")
        
    except ValueError:
        print("❌ Error: Please enter a valid number for user ID")
    except Exception as e:
        print(f"❌ Error finding friends: {e}")

def get_friends_list(friends_hash: FriendsHashTable, user_id: int) -> list:
    """
    Helper function to get friends list for a user
    Returns list of friend IDs
    """
    return friends_hash.get_friends(user_id)

def test_find_friend():
    """Test function for find_friend"""
    from data_structures_starter import users_data, friends_data, load_users, load_friends
    
    # Create test data structures
    tree = AVLTree()
    load_users(tree, users_data)
    
    friends_hash = FriendsHashTable()
    load_friends(friends_hash, friends_data)
    
    print("Testing find_friend function...")
    
    # Test finding friends of user 1
    friends = get_friends_list(friends_hash, 1)
    print(f"User 1 has friends: {friends}")
    
    # Test user with no friends (user 10)
    friends = get_friends_list(friends_hash, 10)
    print(f"User 10 has friends: {friends}")

if __name__ == "__main__":
    test_find_friend()
