import binary_tree as bt
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None

class BinarySearchTree:

    def __init__(self):
        self.root_node = TreeNode(None)

    def insert_node(self, root_node, node_value):

        if root_node.data == None:
            root_node.data = node_value

        elif node_value <= root_node.data:
            if root_node.left_child is None:
                root_node.left_child = TreeNode(node_value)
            else:
                self.insert_node(root_node.left_child, node_value)

        else:
            if root_node.right_child is None:
                root_node.right_child = TreeNode(node_value)
            else:
                self.insert_node(root_node.right_child, node_value)
        return

    def search_node(self, root_node, search_value, ret = False):

        if root_node.data == None:
            return False

        if search_value == root_node.data:
            ret = True

        elif search_value < root_node.data:
            if root_node.left_child is not None:
                if root_node.left_child.data == search_value:
                    ret = True
                else:
                    ret = self.search_node(root_node.left_child, search_value)

        else:
            if root_node.right_child is not None:
                if root_node.right_child.data == search_value:
                    ret = True
                else:
                    ret = self.search_node(root_node.right_child, search_value)       

        return ret

    def min_value_node(self, root_node):
        current_node = root_node

        while current_node.left_child is not None:
            current_node = current_node.left_child

        return current_node                         

    def delete_node(self, root_node, node_value):

        if root_node.data is None:
            return root_node

        if node_value < root_node.data:
            root_node.left_child = self.delete_node(root_node.left_child, node_value)

        elif node_value > root_node.data:
            root_node.right_child = self.delete_node(root_node.right_child, node_value)

        else:
            if root_node.left_child is None:
                temp_node = root_node.right_child
                root_node = None
                return temp_node

            if root_node.right_child is None:
                temp_node = root_node.left_child
                root_node = None
                return temp_node

            temp_node = self.min_value_node(root_node.right_child)
            root_node.data = temp_node.data
            root_node.right_child = self.delete_node(root_node.right_child, temp_node.data)
        return root_node

    def delete_bst(self):
        self.root_node.data = None
        self.root_node.left_child = None
        self.root_node.right_child = None           



# new_bst = BinarySearchTree()
# new_bst.insert_node(new_bst.root_node, 70)
# new_bst.insert_node(new_bst.root_node, 50)
# new_bst.insert_node(new_bst.root_node, 90)
# new_bst.insert_node(new_bst.root_node, 30)
# new_bst.insert_node(new_bst.root_node, 60)
# new_bst.insert_node(new_bst.root_node, 80)
# new_bst.insert_node(new_bst.root_node, 100)
# new_bst.insert_node(new_bst.root_node, 40)
# new_bst.insert_node(new_bst.root_node, 75)
# bt_obj = bt.BinaryTree()
# #bt_obj.level_order_traversal(new_bst.root_node)
# #print(new_bst.search_node(new_bst.root_node, 0))
# new_bst.delete_node(new_bst.root_node, 40)
# new_bst.delete_node(new_bst.root_node, 80)
# new_bst.delete_node(new_bst.root_node, 70)
# print("----------------")
# ret = new_bst.delete_bst()
# bt_obj.level_order_traversal(ret)
