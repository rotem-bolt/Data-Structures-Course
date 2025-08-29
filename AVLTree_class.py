from typing import Optional, Iterable
from Users import User

class _Node:
    def __init__(self, key: int, val: User, h: int = 1, left: Optional["_Node"] = None, right: Optional["_Node"] = None):
        self.key = key
        self.val = val
        self.h = h
        self.left = left
        self.right = right

    @staticmethod
    def _height(t: Optional["_Node"]) -> int:
        return t.h if t else 0

    def _fix(self) -> "_Node":
        self.h = max(_Node._height(self.left), _Node._height(self.right)) + 1
        return self

    @staticmethod
    def _bf(t: Optional["_Node"]) -> int:
        return (_Node._height(t.left) - _Node._height(t.right)) if t else 0

    def _rotR(self) -> "_Node":
        x = self.left
        T2 = x.right
        x.right = self
        self.left = T2
        self._fix()
        x._fix()
        return x

    def _rotL(self) -> "_Node":
        y = self.right
        T2 = y.left
        y.left = self
        self.right = T2
        self._fix()
        y._fix()
        return y

    def _rebalance(self) -> "_Node":
        self._fix()
        b = _Node._bf(self)
        if b > 1:
            if _Node._bf(self.left) < 0:
                self.left = self.left._rotL()
            return self._rotR()
        if b < -1:
            if _Node._bf(self.right) > 0:
                self.right = self.right._rotR()
            return self._rotL()
        return self

    @staticmethod
    def _insert(t: Optional["_Node"], key: int, val: User) -> "_Node":
        if not t:
            return _Node(key, val)
        if key < t.key:
            t.left = _Node._insert(t.left, key, val)
        elif key > t.key:
            t.right = _Node._insert(t.right, key, val)
        else:
            # key קיים: עדכון הערך
            t.val = val
            return t
        return t._rebalance()

    @staticmethod
    def _get(t: Optional["_Node"], key: int) -> Optional[User]:
        while t:
            if key < t.key: 
                t = t.left
            elif key > t.key: 
                t = t.right
            else: 
                return t.val
        return None

    @staticmethod
    def _inorder(t: Optional["_Node"]) -> Iterable[User]:
        if t:
            yield from _Node._inorder(t.left)
            yield t.val
            yield from _Node._inorder(t.right)

class AVLTree:
    def __init__(self):
        self._root: Optional[_Node] = None
        self._n = 0

    def __len__(self) -> int: return self._n

    def insert(self, key: int, val: User) -> None:
        existed = self.search(key) is not None
        self._root = _Node._insert(self._root, key, val)
        if not existed: self._n += 1

    def search(self, key: int) -> Optional[User]:
        return _Node._get(self._root, key)

    def inorder(self) -> Iterable[User]:
        return _Node._inorder(self._root)


def load_users_into_tree(tree: AVLTree, users_data: list[tuple]) -> None:
    """
    Load user data from list of tuples into AVL tree
    Each tuple should be: (user_id, first_name, last_name, gender, birth_year, description)
    """
    for user_tuple in users_data:
        if len(user_tuple) == 6:
            user_id, first_name, last_name, gender, birth_year, description = user_tuple
            user = User(user_id, first_name, last_name, gender, birth_year, description)
            tree.insert(user_id, user)
        else:
            print(f"Warning: Invalid user data tuple: {user_tuple}")