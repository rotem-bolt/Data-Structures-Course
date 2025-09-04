from AVLTree import AVLTree

def update_user(tree: AVLTree):
    """
    Update user information in the AVL tree
    Asks for user ID and allows updating user fields
    """
    print("\n=== Update User ===")
    
    try:
        user_id = int(input("Enter user ID to update: "))
        
        # Check if user exists
        user = tree.search(user_id)
        if user is None:
            print(f"Error: User {user_id} does not exist in the system")
            return
        
        print(f"Current user information:")
        user.show_profile()
        
        print("\nWhat would you like to update?")
        print("1. First name")
        print("2. Last name") 
        print("3. Gender")
        print("4. Birth year")
        print("5. Email")
        print("0. Cancel")
        
        choice = input("Enter your choice (0-5): ").strip()
        
        if choice == '0':
            print("Update cancelled")
            return
        
        # Update based on choice
        if choice == '1':
            new_first_name = input(f"Enter new first name (current: {user.first_name}): ").strip()
            if new_first_name:
                user.first_name = new_first_name
                
        elif choice == '2':
            new_last_name = input(f"Enter new last name (current: {user.last_name}): ").strip()
            if new_last_name:
                user.last_name = new_last_name
                
        elif choice == '3':
            new_gender = input(f"Enter new gender (current: {user.gender}): ").strip()
            if new_gender:
                user.gender = new_gender
                
        elif choice == '4':
            try:
                new_birth_year = int(input(f"Enter new birth year (current: {user.birth_year}): "))
                user.birth_year = new_birth_year
            except ValueError:
                print("Invalid birth year entered, keeping original value")
                return
                
        elif choice == '5':
            new_email = input(f"Enter new email (current: {user.email}): ").strip()
            if new_email:
                user.email = new_email
            
        else:
            print("Invalid choice")
            return
        
        # Show updated information
        print(f"\nUpdated user information:")
        user.show_profile()
        
    except ValueError:
        print("Error: Please enter valid numbers for user ID and birth year")
    except Exception as e:
        print(f"Error updating user: {e}")
