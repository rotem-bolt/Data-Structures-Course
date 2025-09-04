from FriendsHashTable import FriendsHashTable
from AVLTree import AVLTree

def add_friend(friends_hash: FriendsHashTable, tree: AVLTree):
    """
    Add a friendship between two users
    Asks for user IDs and creates friendship in both directions
    """

    print("\n=== Add Friend ===")
    
    try:
        # Ask user to enter the first user ID
        user_id = int(input("Enter user ID: "))

        # Search if this user exists in the AVL tree
        user = tree.search(user_id)


        # If user not found, show error and stop
        if user is None:
            print(f"Error: User {user_id} does not exist in the system")
            return

        # Ask for the friend's user ID
        friend_id = int(input("Enter friend ID: "))

        # Search if this friend exists in the AVL tree
        friend = tree.search(friend_id)

        # If friend not found, show error and stop
        if friend is None:
            print(f"Error: User {friend_id} does not exist in the system")
            return

        # Prevent adding yourself as your own friend
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

        # Print success message with both users' names and IDs
        print(f"Friendship added between {user.first_name} ({user_id}) and {friend.first_name} ({friend_id})")

    # This error happens if the input is not a number
    except ValueError:
        print("Error: Please enter valid numbers for user IDs")

    # Any other unexpected error
    except Exception as e:
        print(f"Error adding friendship: {e}")
