class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while True:
                if cur.last is None:
                    new_node.first = cur
                    cur.last = new_node
                    break
                else:
                    cur = cur.last

    def add_athead(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.last = self.head.first
            self.head.first = new_node.last
            self.head = new_node

    def deleteathead(self):
        if self.head is None:
            return "cannot delete an empty list"
        elif self.head.last is None:
            self.head = None
            return "The list is empty after deletion"
        else:
            self.head.last = self.head

    def delete_at_position(self, position):
        #first check if that position is empty
        cur = self.head
        for i in range(1, position+1):
            if cur.last is None:
                return "position is not valid"
            else:
                cur = cur.last
        cur.last = cur.last.last
        n = cur.last
        n.head = cur.last


class Node:
    def __init__(self, data):
        self.first = None
        self.data = data
        self.last = None


dlinked = DoubleLinkedList()
dlinked.add(10)