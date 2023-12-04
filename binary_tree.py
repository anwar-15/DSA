#Binary Tree
#TODO : add main()
import queue_linked_list as queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

class BinaryTree:
    def __init__(self):
        self.root_node = None

    def print_bt(self, root_node, level = 0):
        
        ret = " -" * level + str(root_node.data) + "\n"

        if root_node.left_child is not None:
            ret+= self.print_bt(root_node.left_child, level+1)

        if root_node.right_child is not None:
            ret+= self.print_bt(root_node.right_child, level+1) 

        return ret       


    def pre_order_traversal(self, root_node):
        if not root_node:
            return
        print(root_node.data)
        self.pre_order_traversal(root_node.left_child)
        self.pre_order_traversal(root_node.right_child)

    def in_order_traversal(self,root_node):
        if not root_node:
            return
        self.in_order_traversal(root_node.left_child)
        print(root_node.data)
        self.in_order_traversal(root_node.right_child)

    def post_order_traversal(self,root_node):
        if not root_node:
            return
        self.post_order_traversal(root_node.left_child)
        self.post_order_traversal(root_node.right_child)
        print(root_node.data)

    def level_order_traversal(self,root_node):
        if not root_node:
            return
        else:
            custom_queue = queue.Queue()
            custom_queue.enqueue(root_node)
            #print(custom_queue)
            while not custom_queue.is_empty():
                root = custom_queue.dequeue()
                print(root.data.data)

                if root.data.left_child is not None:
                    custom_queue.enqueue(root.data.left_child)

                if root.data.right_child is not None:
                    custom_queue.enqueue(root.data.right_child)

    def search_bt(self,root_node,search_value):
        if not root_node:
            return "BT doesn't Exist!"
        else:
            custom_queue = queue.Queue()
            custom_queue.enqueue(root_node)
            while not custom_queue.is_empty():
                root = custom_queue.dequeue()
                if root.data.data == search_value:
                    return 'Success!'

                if root.data.left_child is not None:
                    custom_queue.enqueue(root.data.left_child)

                if root.data.right_child is not None:
                    custom_queue.enqueue(root.data.right_child)                
        return "Failure!" 

    def insert_bt_node(self, node):
        new_node = TreeNode(node)
        #print(new_node)
        if not self.root_node:
            self.root_node = new_node
        else:
            custom_queue = queue.Queue()
            custom_queue.enqueue(self.root_node)
            while not custom_queue.is_empty():
                #print(custom_queue)
                root = custom_queue.dequeue()

                if root.data.left_child is not None:
                    custom_queue.enqueue(root.data.left_child)
                else:
                    root.data.left_child = new_node
                    return 'Node insertion Success!'

                if root.data.right_child is not None:
                    custom_queue.enqueue(root.data.right_child)
                else:
                    root.data.right_child = new_node
                    return 'Node insertion Success!'    

    def get_delete_deepest_node(self,root_node):
        if not root_node:
            return
        else:
            child_type = None
            custom_queue = queue.Queue()
            custom_queue.enqueue(root_node)
            while not custom_queue.is_empty():

                root = custom_queue.dequeue()
                if root.data.left_child is not None:
                    custom_queue.enqueue(root.data.left_child)
                    parent_root = root
                    child_type = 'left_child'

                if root.data.right_child is not None:
                    custom_queue.enqueue(root.data.right_child)
                    parent_root = root
                    child_type = 'right_child'

            d_node = root.data
            if child_type == 'left_child':
                parent_root.data.left_child = None
            elif child_type == 'right_child':
                parent_root.data.right_child = None
            else:
                root_node.data = None

            return d_node                       

    def delete_bt_node(self, root_node, node_value):
        if not root_node:
            return "BT dosen't Exist!"
        else:
            custom_queue = queue.Queue()
            custom_queue.enqueue(root_node)
            while not custom_queue.is_empty():

                root = custom_queue.dequeue()
                if root.data.data == node_value:
                    d_node = self.get_delete_deepest_node(root_node)
                    root.data.data = d_node.data
                    return
                if root.data.left_child is not None:
                    custom_queue.enqueue(root.data.left_child)

                if root.data.right_child is not None:
                    custom_queue.enqueue(root.data.right_child)


