from bdb import effective
import binary_tree as bt


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root_node = None

    def get_height(self, root_node):
        if root_node is None:
            return 0
        return root_node.height

    def get_balance(self, root_node):
        if root_node is None:
            return 0
        return self.get_height(root_node.left_child) - self.get_height(root_node.right_child)    

    def min_value_node(self, root_node):
        curr_node  = root_node
        while curr_node.left_child is not None:
            curr_node = curr_node.left_child
        return curr_node    

    def left_rotate(self, disbalanced_node):
        new_root = disbalanced_node.right_child
        disbalanced_node.right_child = disbalanced_node.right_child.left_child
        new_root.left_child = disbalanced_node

        disbalanced_node.height = 1 + max(self.get_height(disbalanced_node.left_child), self.get_height(disbalanced_node.right_child))
        new_root.height = 1 + max(self.get_height(new_root.left_child), self.get_height(new_root.right_child))

        return new_root

    def right_rotate(self, disbalanced_node):

        new_root = disbalanced_node.left_child
        disbalanced_node.left_child = disbalanced_node.left_child.right_child
        new_root.right_child = disbalanced_node

        disbalanced_node.height = 1 + max(self.get_height(disbalanced_node.left_child), self.get_height(disbalanced_node.right_child))
        new_root.height = 1 + max(self.get_height(new_root.left_child), self.get_height(new_root.right_child))

        return new_root
   
    def insert_node(self, root_node, node_value):

        if root_node is None:
            return AVLNode(node_value)

        elif node_value < root_node.data:
            root_node.left_child = self.insert_node(root_node.left_child, node_value)

        else:
            root_node.right_child = self.insert_node(root_node.right_child, node_value)

        root_node.height = 1 + max(self.get_height(root_node.left_child), self.get_height(root_node.right_child))
        balance = self.get_balance(root_node)

        if balance > 1 and node_value < root_node.left_child.data:
            return self.right_rotate(root_node)

        if balance > 1 and node_value > root_node.left_child.data:
            root_node.left_child = self.left_rotate(root_node.left_child)
            return self.right_rotate(root_node)

        if balance < -1 and node_value > root_node.right_child.data:
            return self.left_rotate(root_node)

        if balance < -1 and node_value < root_node.right_child.data:
            root_node.right_child = self.right_rotate(root_node.right_child)
            return self.left_rotate(root_node)
        return root_node

    def delete_node(self, root_node, node_value):
        if root_node is None:
            return root_node

        elif node_value < root_node.data:
            root_node.left_child = self.delete_node(root_node.left_child, node_value)

        elif node_value > root_node.data:
            root_node.right_child = self.delete_node(root_node.right_child, node_value)

        else:
            if root_node.left_child is None:
                temp_node = root_node.right_child
                root_node = None
                return temp_node

            elif root_node.right_child is None:
                temp_node = root_node.left_child
                root_node = None
                return temp_node

            temp_node = self.min_value_node(root_node.right_child)
            root_node.data = temp_node.data
            root_node.right_child = self.delete_node(root_node.right_child, temp_node.data)
        
        root_node.height = 1 + max(self.get_height(root_node.left_child), self.get_height(root_node.right_child))
        balance = self.get_balance(root_node)

        if balance > 1 and self.get_balance(root_node.left_child) >= 0 :
            return self.right_rotate(root_node)

        if balance > 1 and self.get_balance(root_node.left_child) < 0:
            root_node.left_child = self.left_rotate(root_node.left_child)
            return self.right_rotate(root_node)

        if balance < -1 and self.get_balance(root_node.right_child) <= 0:
            return self.left_rotate(root_node)

        if balance < -1 and self.get_balance(root_node.right_child) > 0:
            root_node.right_child = self.right_rotate(root_node.right_child)
            return self.left_rotate(root_node)

        return root_node                     


if __name__ == "__main__":

    new_avl = AVLTree()
    new_bt = bt.BinaryTree()
    node_values = list(map(int,input().split()))

    for value in node_values:
        new_avl.root_node = new_avl.insert_node(new_avl.root_node, value)

    new_bt.level_order_traversal(new_avl.root_node)
    print("-------------------")
    new_avl.root_node = new_avl.delete_node(new_avl.root_node, 110)
    new_bt.level_order_traversal(new_avl.root_node)
