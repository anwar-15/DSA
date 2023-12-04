
class CircularQueue:
    def __init__(self,maxSize):
        self.items = maxSize*[None]
        self.maxSize = maxSize
        self.front = -1
        self.rear = -1

    def __str__(self):
        value = [str(x) for x in self.items]
        return ' '.join(value)

    def isFull(self):
        if self.front == 0 and self.rear + 1 == self.maxSize:
            return True
        elif self.rear + 1 == self.front:
            return True
        else:
            return False

    def isEmpty(self):
        if self.rear == -1:
            return True
        else:
            return False

    def enqueue(self,value):
        if self.isFull():
            return f'{value} rejected. The Queue is at capacity!'
        elif self.isEmpty():
            self.front = 0
            self.rear = 0    
        elif self.rear + 1 == self.maxSize:
            self.rear = 0
        else:
            self.rear += 1 

        self.items[self.rear] = value
        return f'value inserted --> {value}'

    def dequeue(self):
        if self.isEmpty():
            return 'Queue is empty'

        value = self.items[self.front]
        self.items[self.front] = None
        if self.front + 1 == self.maxSize:
            self.front = 0
        elif self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1

        return f'Value deleted --> {value}'

if __name__ == "__main__":

    custQueue = CircularQueue(5)
    custQueue.enqueue(1)
    custQueue.enqueue(2)
    custQueue.enqueue(3)
    custQueue.enqueue(4)
    custQueue.enqueue(5)
    print(custQueue)
    print(custQueue.enqueue(6))
    print(custQueue.dequeue())
    print(custQueue.dequeue())
    print(custQueue.enqueue(6))
    print(custQueue.dequeue())
    print(custQueue.dequeue())
    print(custQueue.dequeue())
    print(custQueue.dequeue())
    print(custQueue.dequeue())
    print(custQueue.enqueue(10))
    print(custQueue)
    

    


