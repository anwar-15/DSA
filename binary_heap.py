


class HeapNode:
    def __init__(self, size):
        self.custom_list = [None]*(size+1)
        self.heap_size = 0
        self.max_size = size
        

class BinaryHeap:
    def __init__(self, size, heap_type):
        self.root_node = HeapNode(size)
        self.heap_type = heap_type

    def peak_heap(self):
        if self.root_node is None:
            return 
        return self.root_node.custom_list[1]

    def get_heap_size(self):
        if self.root_node is None:
            return 
        return self.root_node.heap_size

    def level_order_traversal(self):
        if not self.root_node:
            return None
        for val in self.root_node.custom_list[1:self.root_node.heap_size + 1]:
            print(val)


    def heapify_insert(self, index):
        parent_index = int(index/2)
        if index <=1 :
            return 
        if self.heap_type == "min":
            if self.root_node.custom_list[index] < self.root_node.custom_list[parent_index]:
                temp = self.root_node.custom_list[parent_index]
                self.root_node.custom_list[parent_index] = self.root_node.custom_list[index]
                self.root_node.custom_list[index] = temp
            self.heapify_insert(parent_index)

        elif self.heap_type == "max":
            if self.root_node.custom_list[index] > self.root_node.custom_list[parent_index]:
                temp = self.root_node.custom_list[parent_index]
                self.root_node.custom_list[parent_index] = self.root_node.custom_list[index]
                self.root_node.custom_list[index] = temp
            self.heapify_insert(parent_index)

    def insert(self, node_value):

        if self.root_node.heap_size == self.root_node.max_size:
            return 'Binary heap is full!'

        self.root_node.custom_list[self.root_node.heap_size + 1] = node_value
        self.root_node.heap_size += 1

        self.heapify_insert(self.root_node.heap_size)

    def heapify_extract(self, index):
        left_index = 2*index
        right_index = 2*index + 1
        swap_index = 0

        if self.root_node.heap_size < left_index:
            return

        elif self.root_node.heap_size == left_index:
            if self.heap_type == 'min':
                if self.root_node.custom_list[index] > self.root_node.custom_list[left_index]:
                    temp = self.root_node.custom_list[index]    
                    self.root_node.custom_list[index] = self.root_node.custom_list[left_index]
                    self.root_node.custom_list[left_index] = temp
                return

            elif self.heap_type == 'max':
                if self.root_node.custom_list[index] < self.root_node.custom_list[left_index]:
                    temp = self.root_node.custom_list[index]    
                    self.root_node.custom_list[index] = self.root_node.custom_list[left_index]
                    self.root_node.custom_list[left_index] = temp
                return
        else:
            if self.heap_type == 'min':
                if self.root_node.custom_list[left_index] < self.root_node.custom_list[right_index]:
                    swap_index = left_index
                else:
                    swap_index = right_index

                if self.root_node.custom_list[index] > self.root_node.custom_list[swap_index]:
                    temp = self.root_node.custom_list[index]    
                    self.root_node.custom_list[index] = self.root_node.custom_list[swap_index]
                    self.root_node.custom_list[swap_index] = temp   

            elif self.heap_type == 'max':
                if self.root_node.custom_list[left_index] > self.root_node.custom_list[right_index]:
                    swap_index = left_index
                else:
                    swap_index = right_index

                if self.root_node.custom_list[index] < self.root_node.custom_list[swap_index]:
                    temp = self.root_node.custom_list[index]    
                    self.root_node.custom_list[index] = self.root_node.custom_list[swap_index]
                    self.root_node.custom_list[swap_index] = temp

        self.heapify_extract(swap_index)

    def extract(self):
        if not self.root_node:
            return 'Binary Heap tree is not valid!'

        extract = self.root_node.custom_list[1]
        self.root_node.custom_list[1] = self.root_node.custom_list[self.root_node.heap_size] 
        self.root_node.custom_list[self.root_node.heap_size] = None

        self.root_node.heap_size -= 1
        self.heapify_extract(1)
        return extract

# if __name__ == "__main__":

#     new_heap = BinaryHeap(8, 'max')
    # heap = list(map(int,input().split()))

#     for value in heap:
#         new_heap.insert(value)

#     new_heap.level_order_traversal()
#     print(new_heap.extract())
#     print('-------------->')
#     new_heap.level_order_traversal()
















