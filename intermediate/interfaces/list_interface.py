# LIST OBJECT INTERFACE #

class ListInterface:
    def add(self, element) -> int:
        # this will add the element at the end of list
        pass
    
    def size(self) -> int:
        # returns the current size of the list
        pass
    
    def isEmpty(self) -> bool:
        # returns true if the size of the list is 0 and false otherwise
        pass
    
    def getPosition(self, value) -> int:
        # find the position of the value to be find
        pass
    
    def getValue(self, index) -> float:
        # given the index find the value of the element
        pass
    
    def removePosition(self, index) -> bool:
        # deletes the element on the given index
        pass
    
    def removeValue(self, value) -> bool:
        # deletes the element on the given value
        pass
    
    def isMember(self, value) -> bool:
        # tell you if the element belongs to that list
        pass
    
    def replace(self, index, value) -> None:
        # replaces the value on the given position
        pass
    
    def clear(self) -> None:
        # deletes every element in the list and sets the size to 0
        pass
