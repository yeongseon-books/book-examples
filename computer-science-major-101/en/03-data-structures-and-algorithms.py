class LinkedListNode:
    def __init__(self, value: int, nxt: "LinkedListNode | None" = None) -> None:
        self.value: int = value
        self.next: LinkedListNode | None = nxt


class LinkedList:
    def __init__(self) -> None:
        self.head: LinkedListNode | None = None

    def insert_front(self, value: int) -> None:
        self.head = LinkedListNode(value, self.head)

    def find(self, value: int) -> bool:
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
        return False

    def delete(self, value: int) -> bool:
        prev: LinkedListNode | None = None
        node = self.head
        while node:
            if node.value == value:
                if prev:
                    prev.next = node.next
                else:
                    self.head = node.next
                return True
            prev, node = node, node.next
        return False


class BSTNode:
    def __init__(self, key: int, value: str) -> None:
        self.key: int = key
        self.value: str = value
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: BSTNode | None = None

    def insert(self, key: int, value: str) -> None:
        self.root = self._insert(self.root, key, value)

    def _insert(self, node: BSTNode | None, key: int, value: str) -> BSTNode:
        if node is None:
            return BSTNode(key, value)
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value
        return node

    def find(self, key: int) -> str | None:
        node = self.root
        while node:
            if key == node.key:
                return node.value
            node = node.left if key < node.key else node.right
        return None

    def delete(self, key: int) -> None:
        self.root = self._delete(self.root, key)

    def _delete(self, node: BSTNode | None, key: int) -> BSTNode | None:
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
            return node
        if key > node.key:
            node.right = self._delete(node.right, key)
            return node
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        successor = node.right
        while successor.left:
            successor = successor.left
        node.key, node.value = successor.key, successor.value
        node.right = self._delete(node.right, successor.key)
        return node


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(2, "b")
    bst.insert(1, "a")
    bst.insert(3, "c")
    print(bst.find(3))
