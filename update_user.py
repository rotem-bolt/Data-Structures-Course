from AVLTree import AVLTree
from User import User

def update_user(tree: AVLTree) -> None:
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
        
        # Store original values for confirmation
        original_first = user.first_name
        original_last = user.last_name
        original_gender = user.gender
        original_birth = user.birth_year
        original_email = user.email
        
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
        
        # Show what changed
        changes_made = []
        if user.first_name != original_first:
            changes_made.append(f"First name: {original_first} → {user.first_name}")
        if user.last_name != original_last:
            changes_made.append(f"Last name: {original_last} → {user.last_name}")
        if user.gender != original_gender:
            changes_made.append(f"Gender: {original_gender} → {user.gender}")
        if user.birth_year != original_birth:
            changes_made.append(f"Birth year: {original_birth} → {user.birth_year}")
        if user.email != original_email:
            changes_made.append(f"Email: {original_email} → {user.email}")
        
        if changes_made:
            print("Changes made:")
            for change in changes_made:
                print(f"  • {change}")
            print("User updated successfully!")
        else:
            print("No changes were made")
        
    except ValueError:
        print("Error: Please enter valid numbers for user ID and birth year")
    except Exception as e:
        print(f"Error updating user: {e}")
