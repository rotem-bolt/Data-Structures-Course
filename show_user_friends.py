from FriendsHashTable import FriendsHashTable
from AVLTree import AVLTree

def show_user_friends(friends_hash: FriendsHashTable, tree: AVLTree) -> None:
    """
    Show all friends of a specific user with detailed information
    Similar to find_friend but with enhanced display
    """
    print("\n=== Show User Friends ===")
    
    try:
        user_id = int(input("Enter user ID to show their friends: "))
        
        # Check if user exists
        user = tree.search(user_id)
        if user is None:
            print(f"Error: User {user_id} does not exist in the system")
            return
        
        # Get friends list
        friends_ids = friends_hash.get_friends(user_id)
        
        print(f"\nUser: {user.first_name} {user.last_name} (ID: {user_id})")
        print(f" Email: {user.email}")
        print("=" * 60)
        
        if not friends_ids:
            print(f"{user.first_name} has no friends yet")
            return
        
        print(f"Friends List ({len(friends_ids)} friends):")
        
        # Sort friends by ID for consistent display
        friends_ids.sort()
        
        for friend_id in friends_ids:
            print(friend_id)
        
        print("=" * 60)
        
        # Show some statistics
        if friends_ids:
            valid_friends = [tree.search(fid) for fid in friends_ids if tree.search(fid)]
            if valid_friends:
                avg_birth_year = sum(f.birth_year for f in valid_friends) / len(valid_friends)
                genders = [f.gender for f in valid_friends]
                gender_count = {}
                for g in genders:
                    gender_count[g] = gender_count.get(g, 0) + 1
                
                print(f"Average birth year of friends: {avg_birth_year:.1f}")
                print(f"Gender distribution: {dict(gender_count)}")
        
    except ValueError:
        print("Error: Please enter a valid number for user ID")
    except Exception as e:
        print(f"Error showing user friends: {e}")
