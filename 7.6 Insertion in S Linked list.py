class Node:
    def __init__(self, value = None):
        self.value = None
        self.next = None



class sLinked:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.node
        while node:
            yield node
            node = node.next

    # insert in linked list 
     
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:

# singleLinkedList = sLinked()
# node1 = Node(1)
# node2 = Node(2)

# singleLinkedList.head = node1
# singleLinkedList.head.next = node2
# singleLinkedList.tail = node2

