import turtle as tut

class Queue:
    def __init__(self):
        super().__init__()
        self._queue = []

    def getSize(self) -> int:
        return len(self._queue)

    def isEmpty(self) -> bool:
        return len(self._queue) == 0

    def front(self) -> int:
        if len(self._queue) >= 1:
            return self._queue[0]
        else:
            return -1

    def enqueue(self, value) -> bool:
        try:
            self._queue.append(value)
            return True
        except:
            return False

    def dequeue(self) -> bool:
        try:
            self._queue.pop()
            return True
        except:
            return False

    def clear(self) -> None:
        while(len(self._queue) > 0):
            self.dequeue()

    def toArray(self):
        arr = []
        for i in self._queue:
            arr.append(i)

        return arr

    def draw(self):
        tut.setup(1500,700)
        pen = tut.Pen()
        
        pen.penup()
        pen.goto(-self.getSize()*7,20)
        pen.pendown()
        
        for i in range(0,self.getSize()):
            
            startingX = pen.xcor()
            #width of the square and height
            w = 40
            h = 40
            if len(str(self._queue[i])) > 1:
                w += (len(str(self._queue[i])) - 1) * 3
                
            #tracing square, ending at top left corner of current square facing left
            pen.right(90)
            pen.forward(h)
            pen.left(90)
            pen.forward(w)
            pen.left(90)
            pen.forward(h)
            pen.left(90)
            pen.forward(w)
            
            #drawing data into square
            pen.penup()
            pen.backward(w/2)
            pen.left(90)
            pen.forward(h/2 + 5)
            pen.write(str(self._queue[i]), False, align='center')
            pen.backward(h/2 + 5)
            pen.right(90)
            pen.forward(w/2)
            
            #repositioning to top right corner of current square
            pen.penup()
            pen.right(180)
            pen.goto(startingX + w, pen.ycor())
            pen.pendown()


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    myQueue = Queue()
    for i in data:
        myQueue.enqueue(i)

    animation = False
    
    if not animation:
        tut.tracer(0, 0)
    
    myQueue.draw()

    tut.update()
    tut.exitonclick()






