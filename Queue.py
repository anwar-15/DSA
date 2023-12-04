class Queue:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def enqueue(self,value):
        self.items.append(value)
        return f"The element {value} is inserted at the end of queue"
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    
    def dequeue(self):
        if self.isEmpty() == True:
            return "The queue is already empty"
        else:
            return f"{self.items.pop(0)} is popped"

    def peekaboo(self):
        if self.isEmpty():
            return "The queue is empty"
        return f"The first element : {self.items[0]}"

q = Queue()
q.enqueue(3)
print(q.enqueue(4))
q.enqueue(5)
print(q)
print(q.dequeue())
print(q)
print(q.peekaboo())

