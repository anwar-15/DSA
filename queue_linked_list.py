

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curr_node = self.head

        while curr_node:
            yield curr_node
            curr_node = curr_node.next

class Queue:
    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        value = [str(x.data) for x in self.linked_list]
        return ' '.join(value)

    def is_empty(self):
        if self.linked_list.head == None:
            return True
        else:
            return False        

    def enqueue(self,data):
        new_node = Node(data)
        if self.linked_list.head == None:
            self.linked_list.head = new_node
            self.linked_list.tail = new_node
        else:
            self.linked_list.tail.next = new_node
            self.linked_list.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return 'Queue is Empty!'
        else:
            temp_node = self.linked_list.head
            if self.linked_list.head == self.linked_list.tail:
                self.linked_list.head = None
                self.linked_list.tail = None
            else:
                self.linked_list.head = self.linked_list.head.next
        return temp_node

    def peek(self):
        if self.is_empty():
            return 'The Queue is empty'
        else:
            return self.linked_list.head.data  

    def delete(self):
        self.linked_list.head = None
        self.linked_list.tail = None              

    
# cust_queue = Queue()
# cust_queue.enqueue(1)
# cust_queue.enqueue(2)
# cust_queue.enqueue(3)
# cust_queue.enqueue(4)
# print(cust_queue)
# print(cust_queue.dequeue().data)
# print(cust_queue)
