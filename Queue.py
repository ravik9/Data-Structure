class Queue():
    def __init__(self):
        self.que = []
        self.head = -1
        self.tail = -1

    def enqueue(self, ele):
        if self.head == -1:
            self.head += 1
        self.tail += 1
        self.que[self.tail] = ele

    def dequeue(self):
        if self.tail <= self.head:
            self.que[self.tail] = ''
            self.tail += 1
        else:
            return 'Cannot deque an empty queue'

    def printq(self):
        if self.tail <= self.head:
            for i in range(self.tail, self.head+1):
                print(str(i) + ' ')
        else:
            print('The queue is empty')

    def size(self):
        return self.head - self.tail


