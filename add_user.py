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
        
        print(f"User {user_id} ({first_name} {last_name}) added successfully!")
        print(f"Total users in system: {len(tree)}")
        
    except ValueError:
        print("Error: Please enter valid numbers for user ID and birth year")
    except Exception as e:
        print(f"Error adding user: {e}")
