import turtle as tut

class Queue:
    def __init__(self, data, animation, dimensions, bgColor, penColor, penSize, position):
        super().__init__()
        self._queue = []
        self.data = data
        self.animation = animation
        self.dimensions = dimensions
        self.bgColor = bgColor
        self.penColor = penColor
        self.penSize = penSize
        self.position = position

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
            self._queue.remove(self.front())
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
    
    def fillFromArr(self, data):
        for val in data:
            self.enqueue(val)

    def setAnimation(self, ani):
        if not ani:
            tut.tracer(20, 0)
        else:
            tut.tracer(1, 5)

    def draw(self):
        tut.bgcolor(self.bgColor)
        tut.setup(self.dimensions[0], self.dimensions[1], self.position[0], self.position[1])
        pen = tut.Pen()
        tut.hideturtle()
        pen.color(self.penColor)
        pen.pensize(self.penSize[0])
        self.setAnimation(self.animation)
        
        pen.penup()
        pen.goto(-self.getSize()*7,20)
        pen.pendown()
        
        self.fillFromArr(self.data)
        for i in range(0,self.getSize()):
            
            startingX = pen.xcor()
            #width of the square and height
            w = 40 + self.penSize[0]
            h = 40 + self.penSize[0]
            if len(str(self._queue[i])) > 1:
                w += (len(str(self._queue[i])) - 1) * 3
                
            #tracing square, ending at top left corner of current square facing left
            
            pen.right(90)
            pen.forward(h)
            pen.left(90)
            pen.forward(w)
            if i != self.getSize()-1:  
                pen.left(90)
                pen.forward(h)
            else:
                pen.penup()
                pen.left(90)
                pen.forward(w)
                pen.down()
            pen.left(90)
            pen.forward(w)
            
            
            #drawing data into square
            pen.penup()
            pen.backward(w/2)
            pen.left(90)
            pen.forward(h/2 + 5)
            pen.write(str(self._queue[i]), False, align='center', font=['Arial', 8, 'bold'])
            pen.backward(h/2 + 5)
            pen.right(90)
            pen.forward(w/2)
            
            #repositioning to top right corner of current square
            pen.penup()
            pen.right(180)
            pen.goto(startingX + w, pen.ycor())
            pen.pendown()

        pen.up()
        pen.goto(self.dimensions[0], self.dimensions[1])
        tut.exitonclick()

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    myQueue = Queue()
    for i in data:
        myQueue.enqueue(i)
        tut.clearscreen()
        myQueue.draw()

    animation = True
    
    if not animation:
        tut.tracer(0, 0)
    
    tut.update()
    tut.exitonclick()
