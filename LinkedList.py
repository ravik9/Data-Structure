class Node:
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, d):
        new_node = Node(d)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while True:
                if cur.next_node is None:
                    break
                cur = cur.next_node
            cur.next_node = new_node

    def addatfirst(self, fd):
        if self.head is not None:
            new_node = Node(fd)
            cur = self.head
            self.head = new_node
            self.head.next_node = cur
        else:
            print('There is no element to add first')

    def deletehead(self):
        #first check if the head has some data
        if self.head is not None:
            # check if there is more data other than head
            if self.head.next_node is not None:
                self.head = self.head.next_node
                return "changed the head to next element in the list"
            else:
                self.head = self.head.next_node
                return "changed the head to next element and this is the only element present in the list"
        else:
            print('Cannot delete from an empty linked list')

    def find(self, da):
        #check if the list is not empty
        if self.head is not None:
            cur = self.head
            while True:
                if cur.data == da:
                    return True
                    break
                if cur.next_node is None:
                    break
                cur = cur.next_node
            return False
        else:
            return False

    def PrintList(self):
        finalop = 'element:'
        cur = self.head
        while True:
            finalop = finalop + ":" + str(cur.data)
            if cur.next_node is None:
                break

        print(finalop)
        return finalop

linkedlist = LinkedList()
linkedlist.add("ravi")
linkedlist.add("Rahul")
linkedlist.add("Rammi")
linkedlist.addatfirst("Seetha")
linkedlist.add("DAD")
linkedlist.addatfirst("Sudha")
print(linkedlist.find("Rammi"))
print(linkedlist.find("DAD"))
