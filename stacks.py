class Stack():
    
    def __init__(self):
        self.dstack = []
        self.size = -1

    def isEmpty(self):
        return self.dstack == []

    def push(self, ele):
        self.size += 1
        self.dstack[self.size] == ele

    def pop(self):
        self.dstack[self.size] = ''
        self.size -= 1

    def peek(self):
        return self.dstack[self.size]

    def size(self):
        return self.size + 1



