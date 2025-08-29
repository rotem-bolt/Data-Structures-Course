@dataclass
class _Node:
    key: int
    val: User
    h: int = 1
    left: Optional["_Node"] = None
    right: Optional["_Node"] = None

def _height(t: Optional[_Node]) -> int:
    return t.h if t else 0

def _fix(t: _Node) -> _Node:
    t.h = max(_height(t.left), _height(t.right)) + 1
    return t

def _bf(t: Optional[_Node]) -> int:
    return (_height(t.left) - _height(t.right)) if t else 0

def _rotR(y: _Node) -> _Node:
    x = y.left; T2 = x.right
    x.right = y; y.left = T2
    _fix(y); _fix(x); return x

def _rotL(x: _Node) -> _Node:
    y = x.right; T2 = y.left
    y.left = x; x.right = T2
    _fix(x); _fix(y); return y

def _rebalance(t: _Node) -> _Node:
    _fix(t)
    b = _bf(t)
    if b > 1:
        if _bf(t.left) < 0:
            t.left = _rotL(t.left)
        return _rotR(t)
    if b < -1:
        if _bf(t.right) > 0:
            t.right = _rotR(t.right)
        return _rotL(t)
    return t

def _insert(t: Optional[_Node], key: int, val: User) -> _Node:
    if not t:
        return _Node(key, val)
    if key < t.key:
        t.left = _insert(t.left, key, val)
    elif key > t.key:
        t.right = _insert(t.right, key, val)
    else:
        # key קיים: עדכון הערך
        t.val = val
        return t
    return _rebalance(t)

def _get(t: Optional[_Node], key: int) -> Optional[User]:
    while t:
        if key < t.key: t = t.left
        elif key > t.key: t = t.right
        else: return t.val
    return None

def _inorder(t: Optional[_Node]) -> Iterable[User]:
    if t:
        yield from _inorder(t.left)
        yield t.val
        yield from _inorder(t.right)

class AVLTree:
    def __init__(self):
        self._root: Optional[_Node] = None
        self._n = 0

    def __len__(self) -> int: return self._n

    def insert(self, key: int, val: User) -> None:
        existed = self.search(key) is not None
        self._root = _insert(self._root, key, val)
        if not existed: self._n += 1

    def search(self, key: int) -> Optional[User]:
        return _get(self._root, key)

    def inorder(self) -> Iterable[User]:
        return _inorder(self._root)