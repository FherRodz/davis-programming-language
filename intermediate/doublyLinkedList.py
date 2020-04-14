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
        new_node = Node(data=element)
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

    def getSize(self) -> int:
        return self.size

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

    def draw(self):
        tut.setup(1500, 700)
        pen = tut.Pen()
        tut.hideturtle()

        print("pen positon: " + str(pen.pos()))
        print("canvaz dimensions: " + "(" + str(tut.window_width()) +
              "," + str(tut.window_height()) + ")")

        startingX = -len(str(self.getSize()))*470

        pen.penup()
        pen.goto(startingX, 20)
        pen.pendown()

        h = 40
        w = 100  # 60pi values, 20pi for prev & next

        # Head Node with the prev symbol of null

        # tracing node
        pen.right(90)
        pen.forward(h)
        pen.left(90)
        pen.forward(w)
        pen.left(90)
        pen.forward(h)
        pen.left(90)
        pen.forward(w)

        # tracing prev
        pen.backward(20)
        pen.left(90)
        pen.forward(h)
        pen.backward(h)

        # tracing next
        pen.right(90)
        pen.backward(60)
        pen.left(90)
        pen.forward(h)
        pen.backward(h)

        # tracing center data
        pen.right(90)
        pen.penup()
        pen.forward(30)
        pen.left(90)
        pen.forward(h/2+5)
        pen.write("Header", True, align='center')
        pen.backward(5)

        # tracing prev data
        pen.goto(startingX, 20)
        pen.left(90)
        pen.forward(10)
        pen.right(90)
        pen.forward(15)
        pen.write("P", False, align='center')
        pen.forward(8)
        pen.write("r", False, align='center')
        pen.forward(8)
        pen.write("e", False, align='center')
        pen.forward(8)
        pen.write("v", False, align='center')

        # tracing next data
        pen.goto(startingX, 20)
        pen.left(90)
        pen.forward(w-10)
        pen.right(90)
        pen.forward(14)
        pen.write("N", False, align='center')
        pen.forward(8)
        pen.write("e", False, align='center')
        pen.forward(8)
        pen.write("x", False, align='center')
        pen.forward(9)
        pen.write("t", False, align='center')

        # arrow
        pen.goto(startingX, 0)
        pen.pendown()
        pen.right(90)
        pen.forward(20)
        pen.left(90)
        pen.forward(15)

        # tracing ground symbol
        pen.right(90)
        pen.forward(5)
        pen.backward(10)
        pen.forward(5)
        pen.left(90)
        pen.penup()
        pen.forward(5)
        pen.down()
        pen.right(90)
        pen.forward(1)
        pen.backward(2)
        pen.forward(1)
        pen.up()

        # arrow prev
        pen.goto(startingX, 20)
        pen.backward(w)
        pen.left(90)
        pen.forward(11)
        pen.right(135)
        pen.down()
        pen.backward(8)
        pen.forward(8)
        pen.left(90)
        pen.backward(8)
        pen.forward(8)
        pen.right(45)
        pen.backward(30)
        pen.up()

        # arrow next
        pen.goto(startingX, 20)
        pen.backward(w)
        pen.left(90)
        pen.forward(h-11)
        pen.right(90)
        pen.down()
        pen.back(30)
        pen.right(45)
        pen.forward(8)
        pen.backward(8)
        pen.left(90)
        pen.forward(8)
        pen.backward(8)
        pen.up()
        pen.left(45)
        pen.backward(h-11)
        pen.left(90)
        pen.down()

        # rest of the nodes in the dll
        for i in range(0, self.getSize()+1):
            startingX += (w + 30)
            
            if len(str(self.getValue(i))) > 4:
                w += (len(str(self.getValue(i))) - 1) * 3
                
            # tracing node
            pen.right(90)
            pen.forward(h)
            pen.left(90)
            pen.forward(w)
            pen.left(90)
            pen.forward(h)
            pen.left(90)
            pen.forward(w)

            # tracing prev
            pen.backward(20)
            pen.left(90)
            pen.forward(h)
            pen.backward(h)

            # tracing next
            pen.right(90)
            pen.backward(60)
            pen.left(90)
            pen.forward(h)
            pen.backward(h)

            # tracing center data
            pen.right(90)
            pen.penup()
            pen.forward(30)
            pen.left(90)
            pen.forward(h/2+5)
            pen.write(str(self.getValue(i)), False, align='center')
            pen.backward(5)

            # tracing prev data
            pen.goto(startingX, 20)
            pen.left(90)
            pen.forward(10)
            pen.right(90)
            pen.forward(15)
            pen.write("P", False, align='center')
            pen.forward(8)
            pen.write("r", False, align='center')
            pen.forward(8)
            pen.write("e", False, align='center')
            pen.forward(8)
            pen.write("v", False, align='center')

            # tracing next data
            pen.goto(startingX, 20)
            pen.left(90)
            pen.forward(w-10)
            pen.right(90)
            pen.forward(14)
            pen.write("N", False, align='center')
            pen.forward(8)
            pen.write("e", False, align='center')
            pen.forward(8)
            pen.write("x", False, align='center')
            pen.forward(9)
            pen.write("t", False, align='center')

            if i == self.getSize():
                # arrow
                #esquina superior derecha
                pen.up()
                pen.goto(startingX, 20)
                pen.right(90) #mirando a la izquierda
                pen.backward(w)

                pen.pendown()
                pen.left(90)
                pen.forward(h/2)
                pen.left(90)
                pen.forward(15)
                
                pen.right(90)
                pen.forward(10)

                # tracing ground symbol
                pen.right(90)
                pen.forward(5)
                pen.backward(10)
                pen.forward(5)
                pen.left(90)
                pen.penup()
                pen.forward(5)
                pen.down()
                pen.right(90)
                pen.forward(1)
                pen.backward(2)
                pen.forward(1)
                pen.up()
                pen.goto(1400, 690)

            else:
                # arrow prev
                pen.goto(startingX, 20)
                pen.right(90)
                pen.backward(w)
                pen.left(90)
                pen.forward(11)
                pen.right(135)
                pen.down()
                pen.backward(8)
                pen.forward(8)
                pen.left(90)
                pen.backward(8)
                pen.forward(8)
                pen.right(45)
                pen.backward(30)
                pen.up()

                # arrow next
                pen.goto(startingX, 20)
                pen.backward(w)
                pen.left(90)
                pen.forward(h-11)
                pen.right(90)
                pen.down()
                pen.back(30)
                pen.right(45)
                pen.forward(8)
                pen.backward(8)
                pen.left(90)
                pen.forward(8)
                pen.backward(8)
                pen.up()
                pen.left(45)
                pen.backward(h-11)
                pen.left(90)
                pen.down()



if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    mydll = DoublyLinkedList()
    for i in data:
        mydll.add(i)
    
    animation = False
    
    if not animation:
        tut.tracer(0, 0)
    
    mydll.draw()

    tut.update()
    tut.exitonclick()

