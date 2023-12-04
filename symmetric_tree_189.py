import binary_tree as bt


class Solution:

    def __init__(self):
        self.root_node = None

    def is_symmetric_tree(self, root_node) -> bool:

        ret = self.is_mirror(root_node, root_node )   
        return ret 

    def is_mirror(self, left_subtree, right_subtree):

        if left_subtree is None and right_subtree is None:
            return True

        elif left_subtree is None or right_subtree is None:
            return False

        else:
            return (left_subtree.data == right_subtree.data) and self.is_mirror(left_subtree.right_child, right_subtree.left_child) and self.is_mirror(left_subtree.left_child, right_subtree.right_child)


if __name__ == '__main__':

    custom_tree = bt.BinaryTree()
    sol = Solution()

    node_values = list(map(int,input().split()))

    for value in node_values:
        custom_tree.insert_bt_node(value)

    print(sol.is_symmetric_tree(custom_tree.root_node))



