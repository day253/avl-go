class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def is_balanced(self):
        return self.__is_balanced(self.root)

    def __is_balanced(self, node):
        if node is None:
            return True
        balance = self.__get_balance(node)
        if balance > 1 or balance < -1:
            return False

        return self.__is_balanced(node.left) and self.__is_balanced(node.right)

    def insert(self, key):
        self.root = self.__insert(self.root, key)

    def __insert(self, node, key):
        if node is None:
            return AVLNode(key)
        elif key < node.key:
            node.left = self.__insert(node.left, key)
        else:
            node.right = self.__insert(node.right, key)

        node.height = 1 + max(self.__get_height(node.left),
                              self.__get_height(node.right))

        balance = self.__get_balance(node)

        if balance > 1 and key < node.left.key:
            return self.__right_rotate(node)

        if balance < -1 and key > node.right.key:
            return self.__left_rotate(node)

        if balance > 1 and key > node.left.key:
            node.left = self.__left_rotate(node.left)
            return self.__right_rotate(node)

        if balance < -1 and key < node.right.key:
            node.right = self.__right_rotate(node.right)
            return self.__left_rotate(node)

        return node

    def __left_rotate(self, node):
        right_child = node.right
        left_grandchild = right_child.left

        right_child.right = node
        node.right = left_grandchild

        node.height = 1 + max(self.__get_height(node.left),
                              self.__get_height(node.right))
        right_child.height = 1 + \
            max(self.__get_height(right_child.left),
                self.__get_height(right_child.right))
        return right_child

    def __right_rotate(self, node):
        left_child = node.left
        right_grandchild = left_child.right

        left_child.right = node
        node.left = right_grandchild

        node.height = 1 + max(self.__get_height(node.left),
                              self.__get_height(node.right))
        left_child.height = 1 + \
            max(self.__get_height(left_child.left),
                self.__get_height(left_child.right))

        return left_child

    def __get_balance(self, node):
        if node is None:
            return 0
        return self.__get_height(node.left) - self.__get_height(node.right)

    def __get_height(self, node):
        if node is None:
            return 0
        return node.height
