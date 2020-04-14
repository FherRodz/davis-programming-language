import turtle as tut


class Node:
    def __init__(self, next=None, prev=None, data=None): 
        self.next = next 
        self.prev = prev
        self.data = data 
        
    def getNext(self):
        return self.next
    def getPrev(self):
        return self.prev
    def getData(self):
        return self.data
    
    def setNext(self, next):
        self.next = next
    def setPrev(self, prev):
        self.prev = prev
    def setData(self, value):
        self.data = value
        
    def clear(self):
        self.setData(None)
        self.setNext(None)
        self.setPrev(None)
        

class DoublyLinkedList:
    def __init__(self):
        super().__init__()
        self.head = Node()
        self.size = 0

    def add(self, element) -> int: 
        new_node = Node(data = element) 
        last = self.head.getNext()

        new_node.setNext(None)

        if self.head.getNext() is None: 
            new_node.setPrev(self.head)
            self.head.setNext(new_node)
            return

        while (last.getNext() is not None): 
            last = last.getNext()

        last.setNext(new_node)  

        new_node.setPrev(last)
        self.size += 1
    
    def size(self) -> str:
        return str(self.size)

    def isEmpty(self) -> bool:
        return self.size == 0

    def getPosition(self, value) -> int:
        index = 0
        currNode = self.head.getNext()

        while currNode is not None:
            if currNode.getData() == value:
                return index

            index += 1
            currNode = currNode.getNext()

        return -1
    
    def getValue(self, index) -> int:
        local_index = 0
        currNode = self.head.getNext()

        while currNode is not None:
            if local_index == index:
                return currNode.getData()
            
            local_index += 1
            currNode = currNode.getNext()

        return -1
    
    def remove(self, node):
        prev = Node.getPrev(node)
        next = Node.getNext(node)
        prev.setNext(next)
        next.setPrev(prev) 
        
        Node.clear(node)
    
    def removePosition(self, index) -> bool:
        local_index = 0

        currNode = self.head.getNext()

        while currNode is not None:
            if local_index == index:
                self.remove(currNode)
                return True

            local_index += 1
            currNode = currNode.getNext()

        return False

    def removeValue(self, value) -> bool:
        currNode = self.head.getNext()

        while currNode is not None:
            if currNode.getData() == value:
                self.remove(currNode)
                return True
            
            currNode = currNode.getNext()
        
        return False

    def isMember(self, value) -> bool:
        currNode = self.head.getNext()

        while currNode is not None:
            if(currNode.getData() == value):
                return True
            
            currNode = currNode.getNext()
        
        return False

    def replace(self, index, value) -> int:
        local_index = 0

        currNode = self.head.getNext()

        while currNode is not None:
            if local_index == index:
                etr = currNode.getData()
                currNode.setData(value)
                return etr

            local_index += 1
            currNode = currNode.getNext()

        return None

    def clear(self):
        currNode = self.head.getNext()

        while currNode is not None:
            self.remove(currNode)
            currNode = currNode.getNext()
    
    def toArray(self):
        atr = []
        currNode = self.head.getNext()
        
        while currNode is not None:
            atr.append(currNode.getData())
            currNode = currNode.getNext()
            
        return atr

if __name__ == "__main__":
    data = [1,2,3,4,5]
    mydll = DoublyLinkedList()
    for i in data:
        mydll.add(i)
    print(mydll.toArray())
    print(mydll.removeValue(3))
    print(str(mydll.getPosition(4)))
    print(mydll.size)
    mydll.replace(2, 8)
    print(mydll.toArray())
    
