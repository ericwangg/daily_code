# This problem was asked by Microsoft.
#
# Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.
#
# Given the root to such a tree, write a function to evaluate it.
#
# For example, given the following tree:
#
#     *
#    / \
#   +    +
#  / \  / \
# 3  2  4  5
# You should return 45, as it is (3 + 2) * (4 + 5)

class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

# # '(3 + 2) * (4 + 5)'
# def build_arithmetic_tree(string):

def eval_arithmetic_tree(root):
    if root.value.isnumeric():
        return root.value # pass back up
    else:
        return eval("{} {} {}".format(eval_arithmetic_tree(root.left), root.value, eval_arithmetic_tree(root.right)))

if __name__ == '__main__':
    # Creating the example tree.
    root = Node('*')
    root.left = Node('+')
    root.left.left = Node('3')
    root.left.right = Node('2')
    root.right = Node('+')
    root.right.left = Node('4')
    root.right.right = Node('5')
    print(eval_arithmetic_tree(root)) # and evaluate
