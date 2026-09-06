class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        count = 0
        curr = self.head
        while curr != None:
            if count == index:
                return curr.val
            count += 1
            curr = curr.next
        
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = node(val)
        
        if self.head == None or self.tail == None:
            self.head = newNode
            self.tail = newNode
            return

        newNode.next = self.head
        self.head = newNode
        return

    def addAtTail(self, val: int) -> None:
        newNode = node(val)
        newNode.next = None
        if self.head == None or self.tail == None:
            self.head = newNode
            self.tail = newNode
            return
        else:
            self.tail.next = newNode
            self.tail = newNode
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        
        newNode = node(val)
        count = 0
        curr = self.head

        while curr != None:
            if count == index - 1:
                break
            count += 1
            curr = curr.next

        if curr == None:
            return
        elif curr.next == None:
            curr.next = newNode
            self.tail = newNode
        else:
            nextNode = curr.next
            curr.next = newNode
            newNode.next = nextNode


    def deleteAtIndex(self, index: int) -> None:
        if self.head == None:
            return
        if index == 0:
            self.head = self.head.next
            if self.head == None:
                self.tail = None
            return
        
        curr = self.head
        count = 0
        while curr != None:
            if count == index - 1:
                break
            count += 1
            curr = curr.next
        
        if curr == None or curr.next == None:
            return
        if curr.next == self.tail:
            self.tail = curr
            curr.next = None
            return
        curr.next = curr.next.next
        return

class node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
    

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)