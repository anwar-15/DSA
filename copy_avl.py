import binary_tree as bt


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1

# def __init__(self):
#     root_node = None

def get_height(root_node):
    if root_node is None:
        return 0
    return root_node.height

def get_balance(root_node):
    if root_node is None:
        return 0
    return get_height(root_node.left_child) - get_height(root_node.right_child)    

def left_rotate(disbalanced_node):
    new_root = disbalanced_node.right_child
    disbalanced_node.right_child = disbalanced_node.right_child.left_child
    new_root.left_child = disbalanced_node

    disbalanced_node.height = 1 + max(get_height(disbalanced_node.left_child), get_height(disbalanced_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child), get_height(new_root.right_child))

    return new_root

def right_rotate(disbalanced_node):

    new_root = disbalanced_node.left_child
    disbalanced_node.left_child = disbalanced_node.left_child.right_child
    new_root.right_child = disbalanced_node

    disbalanced_node.height = 1 + max(get_height(disbalanced_node.left_child), get_height(disbalanced_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child), get_height(new_root.right_child))

    return new_root

def insert_node(root_node, node_value):

    if root_node is None:
        return AVLNode(node_value)

    elif node_value < root_node.data:
        root_node.left_child = insert_node(root_node.left_child, node_value)

    else:
        root_node.right_child = insert_node(root_node.right_child, node_value)

    root_node.height = 1 + max(get_height(root_node.left_child), get_height(root_node.right_child))
    balance = get_balance(root_node)
    print(balance)

    if balance > 1 and node_value < root_node.left_child.data:
        return right_rotate(root_node)

    if balance > 1 and node_value > root_node.left_child.data:
        root_node.left_child = left_rotate(root_node.left_child)
        return right_rotate(root_node)

    if balance < -1 and node_value > root_node.right_child.data:
        return left_rotate(root_node)

    if balance < -1 and node_value < root_node.right_child.data:
        root_node.right_child = right_rotate(root_node.right_child)
        return left_rotate(root_node)
    return root_node                 



new_bt = bt.BinaryTree()
# node_values = list(map(int,input().split()))
# new_avl.root_node = AVLNode(node_values[0])
new_avl = AVLNode(8)
insert_node(new_avl.root_node, 5)
insert_node(new_avl.root_node, 3)
#new_avl.insert_node(new_avl.root_node, 8)


# for value in node_values[1:]:
#     new_avl.insert_node(new_avl.root_node, value)
#     #print(new_avl.root_node.data)

print(new_bt.level_order_traversal(new_avl.root_node))


