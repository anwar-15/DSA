class BinaryTree:
    def __init__(self, max_size):
        self.max_size = max_size
        self.custom_list = max_size*[None]
        self.last_used_index = 0

    def insert_node(self, value):

        if len(self.custom_list) + 1 == self.max_size:
            return 'Binary Tree is Full!'
        else:
            self.custom_list[self.last_used_index + 1] = value
            self.last_used_index += 1
            return 'successfully inserted valu!'     

    def pre_order_traversal(self, index = 1):
        if index > self.last_used_index:
            return 
        print(self.custom_list[index])
        self.pre_order_traversal(index*2)
        self.pre_order_traversal(index*2 + 1)

    def in_order_traversal(self, index = 1):
        if index > self.last_used_index:
            return
        self.pre_order_traversal(index*2)
        print(self.custom_list[index])
        self.pre_order_traversal(index*2 + 1)

    def post_order_traversal(self, index = 1):
        if index > self.last_used_index:
            return
        self.pre_order_traversal(index*2)
        self.pre_order_traversal(index*2 + 1)
        print(self.custom_list[index])
           
new_bt = BinaryTree(8)
for val in range(1,8):
    new_bt.insert_node(val)

new_bt.pre_order_traversal()
