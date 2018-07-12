
class Node:
    def __init__(self,  data = None,  next_node = None):
        self.data = data
        self.next = next_node
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return (head==None)
    
    def insertFirst(self, data):
        newNode = Node(data)
        newNode.next = self.head
        head = newNode
    
    def deleteFirst(self):
        oldHead = head
        head = head.next
        return oldHead
    
    def displayList(self):
        currentNode = self.head
        while (currentNode is not None):
            print(currentNode)
            currentNode = currentNode.next
    
    def find(self, key):
        currentNode = head
        while (currentNode.data != key):
            if (currentNode.next is not None):
                currentNode.next

#Enter linked list values "
aList = map(int, input().strip().split(' '))

LList1 = LinkedList()
for num in aList:
    LList1.insertFirst(num)

LList1.displayList()

def has_cycle_reverse(head):
    previousNode = None
    currentNode = head
    nextNode = None
    if(currentNode.next is None):
        return False
    while(currentNode.next is not None ):
        nextNode = currentNode.next
        currentNode.next = previousNode # Reverses the Linked List
        previousNode = currentNode
        currentNode = nextNode
        if(previousNode == head):
            return True
    return False

def has_cycle_floyd(head):
    fastNode = head
    slowNode = head
    while (fastNode and slowNode and fastNode.next):
        slowNode = fastNode.next
        fastNode = fastNode.next.next
        if (slowNode == fastNode):
            return True
    return False