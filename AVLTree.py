from typing import Optional, Dict
from User import User

class AVLTree:
    """
    AVL Tree - A self-balancing binary search tree
    """
    
    def __init__(self):
        # Dictionary to store all tree nodes: node_id -> node_information
        self.nodes: Dict[int, Dict] = {}
        self.root_id: Optional[int] = None  # ID of the root node (None if tree is empty)
        self.next_node_id = 1  # Counter to give each node a unique ID number
        self._n = 0  # Total number of users in the tree

    def __len__(self): 
        return self._n

    def _create_node(self, key: int, val: User, height: int = 1, left_id: Optional[int] = None, right_id: Optional[int] = None):
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

    def _get_height(self, node_id: Optional[int]):
        """Get height of node by ID"""
        return self.nodes[node_id]['height'] if node_id else 0

    def _get_balance_factor(self, node_id: Optional[int]):
        """Calculate balance factor for node"""
        if not node_id:
            return 0
        node = self.nodes[node_id]
        return self._get_height(node['left_id']) - self._get_height(node['right_id'])

    def _fix_height(self, node_id: int):
        """Fix height for node"""
        node = self.nodes[node_id]
        left_height = self._get_height(node['left_id'])
        right_height = self._get_height(node['right_id'])
        node['height'] = max(left_height, right_height) + 1

    def _rotate_right(self, node_id: int):
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

    def _rotate_left(self, node_id: int):
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

    def _rebalance(self, node_id: int):
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

    def _insert_node(self, node_id: Optional[int], key: int, val: User):
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

    def insert(self, key: int, val: User):
        """Insert key-value pair into the AVL tree"""
        existed = self.search(key) is not None
        self.root_id = self._insert_node(self.root_id, key, val)
        if not existed:
            self._n += 1

    def search(self, key: int):
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

    def _inorder_traversal(self, node_id: Optional[int], result_list: list):
        """In-order traversal starting from node_id - adds users to result_list"""
        if node_id:  # If node exists
            node = self.nodes[node_id]
            # Step 1: Visit left subtree first
            self._inorder_traversal(node['left_id'], result_list)
            # Step 2: Add current node to result
            result_list.append(node['val'])
            # Step 3: Visit right subtree last
            self._inorder_traversal(node['right_id'], result_list)

    def inorder(self):
        """Return all users in sorted order (by ID) as a list"""
        result = []  # Create empty list to store users
        self._inorder_traversal(self.root_id, result)  # Fill the list
        return result  # Return completed list
    
    def show_all_users(self):
        """Print all users in sorted order (by ID)"""
        print(f"\nAVL Tree contains {len(self)} users:")
        print("-" * 40)
        users_list = self.inorder()  # Get all users as a list
        for user in users_list:
            user.show_profile()  # Use the User's show_profile method

    def _find_min_node(self, node_id: int):
        """Find the minimum node in subtree rooted at node_id"""
        while self.nodes[node_id]['left_id'] is not None:
            node_id = self.nodes[node_id]['left_id']
        return node_id

    def _delete_node(self, node_id: Optional[int], key: int):
        """Delete node with given key from subtree rooted at node_id, return new root ID"""
        if not node_id:
            return None
        
        node = self.nodes[node_id]
        
        # Standard BST deletion
        if key < node['key']:
            node['left_id'] = self._delete_node(node['left_id'], key)
        elif key > node['key']:
            node['right_id'] = self._delete_node(node['right_id'], key)
        else:
            # Node to be deleted found
            # Case 1: Node with only right child or no child
            if node['left_id'] is None:
                right_id = node['right_id']
                del self.nodes[node_id]  # Remove node from dictionary
                return right_id
            
            # Case 2: Node with only left child
            elif node['right_id'] is None:
                left_id = node['left_id']
                del self.nodes[node_id]  # Remove node from dictionary
                return left_id
            
            # Case 3: Node with two children
            # Get the inorder successor (smallest in the right subtree)
            successor_id = self._find_min_node(node['right_id'])
            successor_node = self.nodes[successor_id]
            
            # Copy the successor's key and value to this node
            node['key'] = successor_node['key']
            node['val'] = successor_node['val']
            
            # Delete the successor
            node['right_id'] = self._delete_node(node['right_id'], successor_node['key'])
        
        # Rebalance the tree
        return self._rebalance(node_id)

    def delete(self, key: int):
        """Delete key from the AVL tree"""
        if self.search(key) is not None:
            self.root_id = self._delete_node(self.root_id, key)
            self._n -= 1
            return True
        return False