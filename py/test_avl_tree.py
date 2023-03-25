import unittest
from avl_tree import AVLTree
import random


def generate_test_cases_insert(num_cases):
    test_cases = []
    for i in range(num_cases):
        # 生成随机整数作为插入值
        value = random.randint(0, 100)
        # 将插入值加入测试用例中
        test_cases.append(value)
    return test_cases


class TestAVLTree(unittest.TestCase):

    def test_insert(self):
        avl = AVLTree()
        test_cases = generate_test_cases_insert(100)

        for value in test_cases:
            avl.insert(value)
            # 检查 AVL 树是否满足 AVL 树的定义
            self.assertEqual(avl.is_balanced(), True)


if __name__ == '__main__':
    unittest.main()
