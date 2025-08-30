from AVLTree import AVLTree
from User import User

def add_user(tree: AVLTree) -> None:
    """
    Add a new user to the AVL tree
    Asks for user input and creates a new User object
    """
    print("\n=== Add New User ===")
    
    try:
        # Get user input
        user_id = int(input("Enter user ID: "))
        
        # Check if user already exists
        if tree.search(user_id) is not None:
            print(f"Error: User with ID {user_id} already exists!")
            return
        
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        gender = input("Enter gender: ")
        birth_year = int(input("Enter birth year: "))
        description = input("Enter description: ")
        
        # Create new user object
        new_user = User(user_id, first_name, last_name, gender, birth_year, description)
        
        # Add user to tree
        tree.insert(user_id, new_user)
        
        print(f"✅ User {user_id} ({first_name} {last_name}) added successfully!")
        print(f"Total users in system: {len(tree)}")
        
    except ValueError:
        print("❌ Error: Please enter valid numbers for user ID and birth year")
    except Exception as e:
        print(f"❌ Error adding user: {e}")

def test_add_user():
    """Test function for add_user"""
    from data_structures_starter import users_data, load_users
    
    # Create test tree with some existing users
    tree = AVLTree()
    load_users(tree, users_data[:5])  # Load first 5 users
    
    print("Current users in tree:")
    tree.show_all_users()
    
    # Test adding a user
    print("\nTesting add_user function...")
    # Simulate user input (in real usage, user would type these)
    # add_user(tree)  # Commented out to avoid input prompt in test

if __name__ == "__main__":
    test_add_user()
