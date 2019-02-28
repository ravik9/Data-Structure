class queuewithstack:
    def __init__(self):
        self.a = []
        self.b = []

    def insert_right(self, elem):
        self.b.append(elem)

    def insert_left(self,elem):
        self.a.append(elem)

    def remove_left(self):
        self.b.pop()

    def remove_right(self):
        self.a.pop()
