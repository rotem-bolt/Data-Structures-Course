from typing import Optional, Dict
from User import User

class AVLTree:
    """
    AVL Tree - A self-balancing binary search tree
    Uses dictionaries to store nodes (similar to MessageHashTable)
    """
    
    def __init__(self):
        # Dictionary to store all tree nodes: node_id -> node_information
        self.nodes: Dict[int, Dict] = {}
        self.root_id: Optional[int] = None  # ID of the root node (None if tree is empty)
        self.next_node_id = 1  # Counter to give each node a unique ID number
        self._n = 0  # Total number of users in the tree

    def __len__(self) -> int: 
        return self._n

    def _create_node(self, key: int, val: User, height: int = 1, left_id: Optional[int] = None, right_id: Optional[int] = None) -> int:
        """Create a new node and return its ID"""
        node_id = self.next_node_id
        self.next_node_id += 1
        self.nodes[node_id] = {
            'key': key,
            'val': val,
            'height': height,
            'left_id': left_id,
            'right_id': right_id
        }
        return node_id

    def _get_height(self, node_id: Optional[int]) -> int:
        """Get height of node by ID"""
        return self.nodes[node_id]['height'] if node_id else 0

    def _get_balance_factor(self, node_id: Optional[int]) -> int:
        """Calculate balance factor for node"""
        if not node_id:
            return 0
        node = self.nodes[node_id]
        return self._get_height(node['left_id']) - self._get_height(node['right_id'])

    def _fix_height(self, node_id: int) -> None:
        """Fix height for node"""
        node = self.nodes[node_id]
        left_height = self._get_height(node['left_id'])
        right_height = self._get_height(node['right_id'])
        node['height'] = max(left_height, right_height) + 1

    def _rotate_right(self, node_id: int) -> int:
        """Right rotation - returns new root ID"""
        node = self.nodes[node_id]
        left_id = node['left_id']
        left_node = self.nodes[left_id]
        
        # Perform rotation
        node['left_id'] = left_node['right_id']
        left_node['right_id'] = node_id
        
        # Fix heights
        self._fix_height(node_id)
        self._fix_height(left_id)
        
        return left_id

    def _rotate_left(self, node_id: int) -> int:
        """Left rotation - returns new root ID"""
        node = self.nodes[node_id]
        right_id = node['right_id']
        right_node = self.nodes[right_id]
        
        # Perform rotation
        node['right_id'] = right_node['left_id']
        right_node['left_id'] = node_id
        
        # Fix heights
        self._fix_height(node_id)
        self._fix_height(right_id)
        
        return right_id

    def _rebalance(self, node_id: int) -> int:
        """Rebalance node and return new root ID"""
        self._fix_height(node_id)
        balance = self._get_balance_factor(node_id)
        node = self.nodes[node_id]
        
        # Left heavy
        if balance > 1:
            if self._get_balance_factor(node['left_id']) < 0:
                node['left_id'] = self._rotate_left(node['left_id'])
            return self._rotate_right(node_id)
        
        # Right heavy
        if balance < -1:
            if self._get_balance_factor(node['right_id']) > 0:
                node['right_id'] = self._rotate_right(node['right_id'])
            return self._rotate_left(node_id)
        
        return node_id

    def _insert_node(self, node_id: Optional[int], key: int, val: User) -> int:
        """Insert into subtree rooted at node_id, return new root ID"""
        if not node_id:
            return self._create_node(key, val)
        
        node = self.nodes[node_id]
        if key < node['key']:
            node['left_id'] = self._insert_node(node['left_id'], key, val)
        elif key > node['key']:
            node['right_id'] = self._insert_node(node['right_id'], key, val)
        else:
            # Key exists: update value
            node['val'] = val
            return node_id
        
        return self._rebalance(node_id)

    def insert(self, key: int, val: User) -> None:
        """Insert key-value pair into the AVL tree"""
        existed = self.search(key) is not None
        self.root_id = self._insert_node(self.root_id, key, val)
        if not existed:
            self._n += 1

    def search(self, key: int) -> Optional[User]:
        """Search for key in the AVL tree"""
        node_id = self.root_id
        while node_id:
            node = self.nodes[node_id]
            if key < node['key']:
                node_id = node['left_id']
            elif key > node['key']:
                node_id = node['right_id']
            else:
                return node['val']
        return None

    def _inorder_traversal(self, node_id: Optional[int], result_list: list) -> None:
        """In-order traversal starting from node_id - adds users to result_list"""
        if node_id:  # If node exists
            node = self.nodes[node_id]
            # Step 1: Visit left subtree first
            self._inorder_traversal(node['left_id'], result_list)
            # Step 2: Add current node to result
            result_list.append(node['val'])
            # Step 3: Visit right subtree last
            self._inorder_traversal(node['right_id'], result_list)

    def inorder(self) -> list[User]:
        """Return all users in sorted order (by ID) as a list"""
        result = []  # Create empty list to store users
        self._inorder_traversal(self.root_id, result)  # Fill the list
        return result  # Return completed list
    
    def show_all_users(self) -> None:
        """Print all users in sorted order (by ID) - similar to MessageHashTable"""
        print(f"\nAVL Tree contains {len(self)} users:")
        print("-" * 40)
        users_list = self.inorder()  # Get all users as a list
        for user in users_list:
            user.show_profile()  # Use the User's show_profile method