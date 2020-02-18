# Вывести содержимое в бинарном дереве включая информацию о всех узлах.
# Реализовать поиск элемента в бинарном дереве.


class TreeNode:

    def __init__(self, value):
        self.data = value
        self.right = None
        self.left = None


class Tree:

    def __init__(self):
        self.root = None

    def add_node(self, node, value):
        if node is None:
            self.root = TreeNode(value)
        else:
            if value < node.data:
                if node.left is None:
                    node.left = TreeNode(value)
                else:
                    self.add_node(node.left, value)
            else:
                if node.right is None:
                    node.right = TreeNode(value)
                else:
                    self.add_node(node.right, value)

    def print_in_order(self, node):
        if node is not None:
            self.print_in_order(node.left)
            print(node.data)
            self.print_in_order(node.right)

    def find(self, data):
        temp = self.root
        while temp.data != data:
            if temp.data > data:
                temp = temp.left
            else:
                temp = temp.right
        return temp


if __name__ == '__main__':

    my_tree = Tree()

    my_tree.add_node(my_tree.root, 200)
    my_tree.add_node(my_tree.root, 300)
    my_tree.add_node(my_tree.root, 100)
    my_tree.add_node(my_tree.root, 30)

    my_tree.add_node(my_tree.root, 250)

    my_tree.print_in_order(my_tree.root)

    print()
    print(my_tree.find(250))