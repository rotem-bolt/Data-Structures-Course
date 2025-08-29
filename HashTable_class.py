from typing import Optional, Iterable, List
from Messages import Message

class _Node:
    """Node for chaining in hash table - represents a linked list node"""
    
    def __init__(self, key: int, val: Message, next_node: Optional["_Node"] = None):
        self.key = key
        self.val = val
        self.next = next_node
    
    def insert(self, key: int, val: Message) -> "_Node":
        """Insert into the chain (linked list). Returns the head of the chain."""
        if self.key == key:
            # Key exists: update value
            self.val = val
            return self
        elif self.next is None:
            # End of chain: add new node
            self.next = _Node(key, val)
            return self
        else:
            # Continue down the chain
            self.next = self.next.insert(key, val)
            return self
    
    def search(self, key: int) -> Optional[Message]:
        """Search for key in the chain"""
        current = self
        while current:
            if current.key == key:
                return current.val
            current = current.next
        return None
    
    def get_all_values(self) -> Iterable[Message]:
        """Get all values in this chain"""
        current = self
        while current:
            yield current.val
            current = current.next
    
    def remove(self, key: int) -> Optional["_Node"]:
        """Remove key from chain. Returns new head of chain."""
        if self.key == key:
            # Remove head
            return self.next
        elif self.next:
            # Continue down the chain
            self.next = self.next.remove(key)
            return self
        else:
            # Key not found
            return self


class HashTable:
    """Hash Table implementation using separate chaining for collision resolution"""
    
    def __init__(self, initial_capacity: int = 16):
        self._capacity = initial_capacity
        self._buckets: List[Optional[_Node]] = [None] * self._capacity
        self._size = 0
        self._load_factor_threshold = 0.75
    
    def __len__(self) -> int:
        return self._size
    
    def _hash(self, key: int) -> int:
        """Simple hash function for integer keys"""
        return key % self._capacity
    
    def _needs_resize(self) -> bool:
        """Check if hash table needs to be resized"""
        return (self._size / self._capacity) > self._load_factor_threshold
    
    def _resize(self) -> None:
        """Resize hash table when load factor gets too high"""
        old_buckets = self._buckets
        old_capacity = self._capacity
        
        # Double the capacity
        self._capacity *= 2
        self._buckets = [None] * self._capacity
        old_size = self._size
        self._size = 0
        
        # Rehash all existing elements
        for i in range(old_capacity):
            current = old_buckets[i]
            while current:
                self.insert(current.key, current.val)
                current = current.next
        
        # Restore correct size (since insert increments it)
        self._size = old_size
    
    def insert(self, key: int, val: Message) -> None:
        """Insert key-value pair into hash table"""
        if self._needs_resize():
            self._resize()
        
        bucket_index = self._hash(key)
        
        if self._buckets[bucket_index] is None:
            # Empty bucket: create new chain
            self._buckets[bucket_index] = _Node(key, val)
            self._size += 1
        else:
            # Bucket has chain: insert into existing chain
            old_size = self._size
            self._buckets[bucket_index] = self._buckets[bucket_index].insert(key, val)
            # Check if it was a new insertion (not an update)
            if self.search(key) == val and old_size == self._size:
                self._size += 1
    
    def search(self, key: int) -> Optional[Message]:
        """Search for key in hash table"""
        bucket_index = self._hash(key)
        
        if self._buckets[bucket_index] is None:
            return None
        else:
            return self._buckets[bucket_index].search(key)
    
    def remove(self, key: int) -> bool:
        """Remove key from hash table. Returns True if key was found and removed."""
        bucket_index = self._hash(key)
        
        if self._buckets[bucket_index] is None:
            return False
        
        # Check if key exists before removal
        if self._buckets[bucket_index].search(key) is None:
            return False
        
        # Remove from chain
        self._buckets[bucket_index] = self._buckets[bucket_index].remove(key)
        self._size -= 1
        return True
    
    def get_all_messages(self) -> Iterable[Message]:
        """Iterate through all messages in hash table (no guaranteed order)"""
        for bucket in self._buckets:
            if bucket is not None:
                yield from bucket.get_all_values()
    
    def get_load_factor(self) -> float:
        """Get current load factor"""
        return self._size / self._capacity
    
    def get_stats(self) -> dict:
        """Get hash table statistics for debugging"""
        non_empty_buckets = sum(1 for bucket in self._buckets if bucket is not None)
        
        # Calculate chain lengths
        chain_lengths = []
        for bucket in self._buckets:
            if bucket is not None:
                length = 0
                current = bucket
                while current:
                    length += 1
                    current = current.next
                chain_lengths.append(length)
        
        max_chain_length = max(chain_lengths) if chain_lengths else 0
        avg_chain_length = sum(chain_lengths) / len(chain_lengths) if chain_lengths else 0
        
        return {
            "capacity": self._capacity,
            "size": self._size,
            "load_factor": self.get_load_factor(),
            "non_empty_buckets": non_empty_buckets,
            "max_chain_length": max_chain_length,
            "avg_chain_length": avg_chain_length
        }


def load_messages_into_hash_table(hash_table: HashTable, messages_data: List[tuple]) -> None:
    """
    Load message data from list of tuples into hash table
    Each tuple should be: (message_id, message_text, is_liked)
    """
    for message_tuple in messages_data:
        if len(message_tuple) == 3:
            message_id, message_text, is_liked = message_tuple
            message = Message(message_id, message_text, is_liked)
            hash_table.insert(message_id, message)
        else:
            print(f"Warning: Invalid message data tuple (needs message_id, message_text, is_liked): {message_tuple}")
