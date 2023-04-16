class Node:
    def __init__(self, value = None):
        self.value = None
        self.next = None



class sLinked:
    def __init__(self):
        self.head = None
        self.tail = None

singleLinkedList = sLinked()
node1 = Node(1)
node2 = Node(2)

singleLinkedList.head = node1
singleLinkedList.head.next = node2
singleLinkedList.tail = node2

