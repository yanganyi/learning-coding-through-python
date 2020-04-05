class BinaryTreeNode:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right

    def __str__(self):
        return "[root: " + self.root + " left: " + str(self.left) + " right: " + str(self.right) + ']'

    def calculate(self):

        if type(self.left) != int:
            left_value = self.left.calculate()
        else:
            left_value = self.left

        if type(self.right) != int:
            right_value = self.right.calculate()
        else:
            right_value = self.right

        if self.root == '+':
            return left_value + right_value
        elif self.root == '*':
            return left_value * right_value


# Constructing a Family Tree
# node_xyz = BinaryTreeNode("xyz", None, "ax2")
# print(node_xyz)
#
# node_abc = BinaryTreeNode("abc", "ax1", None)
# print(node_abc)
#
# node_yay = BinaryTreeNode("yay", node_abc, node_xyz)
# print(node_yay)
#
# node_ycm = BinaryTreeNode("ycm", node_yay, "yaz")
# print(node_ycm)

# Construct a Expression Tree
node_times = BinaryTreeNode("*", 3, 5)
print(node_times)
print(node_times.calculate())

node_plus = BinaryTreeNode("+", node_times, 4)
print(node_plus)
print(node_plus.calculate())


