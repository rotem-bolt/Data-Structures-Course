from AVLTree import AVLTree
from User import User

def find_user(tree: AVLTree) -> None:
    """
    Find and display a user from the AVL tree
    Asks for user ID and shows user profile if found
    """
    print("\n=== Find User ===")
    
    try:
        user_id = int(input("Enter user ID to search: "))
        
        # Search for user in tree
        user = tree.search(user_id)
        
        if user is not None:
            print(f"✅ User found!")
            user.show_profile()
        else:
            print(f"❌ User with ID {user_id} not found")
            
    except ValueError:
        print("❌ Error: Please enter a valid number for user ID")
    except Exception as e:
        print(f"❌ Error searching for user: {e}")

def find_user_by_id(tree: AVLTree, user_id: int) -> User:
    """
    Helper function to find user by ID (returns User object or None)
    Used by other functions that need to find users
    """
    return tree.search(user_id)

def test_find_user():
    """Test function for find_user"""
    from data_structures_starter import users_data, load_users
    
    # Create test tree
    tree = AVLTree()
    load_users(tree, users_data[:10])  # Load first 10 users
    
    print("Testing find_user function...")
    print(f"Tree contains {len(tree)} users")
    
    # Test finding existing user
    user = find_user_by_id(tree, 5)
    if user:
        print(f"Found user 5: {user.first_name} {user.last_name}")
    
    # Test finding non-existing user
    user = find_user_by_id(tree, 99)
    if user is None:
        print("User 99 not found (as expected)")

if __name__ == "__main__":
    test_find_user()
