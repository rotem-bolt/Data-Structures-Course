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
            print(f"❌ Error: User {user_id} does not exist in the system")
            return
            
        if friend is None:
            print(f"❌ Error: User {friend_id} does not exist in the system")
            return
            
        if user_id == friend_id:
            print("❌ Error: Cannot add yourself as a friend")
            return
        
        # Check if they're already friends
        current_friends = friends_hash.get_friends(user_id)
        if friend_id in current_friends:
            print(f"❌ Users {user_id} and {friend_id} are already friends")
            return
        
        # Add friendship in both directions
        friends_hash.add_friend(user_id, friend_id)
        friends_hash.add_friend(friend_id, user_id)
        
        print(f"✅ Friendship added between {user.first_name} ({user_id}) and {friend.first_name} ({friend_id})")
        
    except ValueError:
        print("❌ Error: Please enter valid numbers for user IDs")
    except Exception as e:
        print(f"❌ Error adding friendship: {e}")

def test_add_friend():
    """Test function for add_friend"""
    from data_structures_starter import users_data, friends_data, load_users, load_friends
    
    # Create test data structures
    tree = AVLTree()
    load_users(tree, users_data[:10])  # Load first 10 users
    
    friends_hash = FriendsHashTable()
    load_friends(friends_hash, {k: v for k, v in friends_data.items() if k <= 10})
    
    print("Current friendships:")
    friends_hash.show_all()

if __name__ == "__main__":
    test_add_friend()
