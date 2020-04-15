class QueueInterface:
    def getSize(self) -> int:
        # returns the current size of the queue
        pass

    def isEmpty(self) -> bool:
        # returns true if the size of the queue is 0 and false otherwise
        pass

    def front(self) -> int:
        # return the front of the queue
        pass

    def enqueue(self, value) -> bool:
        # adds the value at the end of the queue
        pass

    def dequeue(self) -> bool:
        # removes the first value in the queue
        pass

    def clear(self) -> None:
        # removes all the values from the queue
        pass
