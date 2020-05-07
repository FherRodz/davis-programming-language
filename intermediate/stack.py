import turtle as tut


class myStack:
    def __init__(self, data, animation, dimensions, bgColor, penColor, penSize, position):
        self.data = data                #A list
        self.stack = None               #The stack structure (a list)
        self.currentSize = 0            #The stack size (an integer)
        self.animation = animation      #A boolean
        self.dimensions = dimensions    #A tuple (x,y)
        self.bgColor = bgColor          #A string 'BLACK'|'WHITE|etc.
        self.penColor = penColor        #A string 'BLACK' |'WHITE |etc.
        self.penSize = penSize          # A tuple (int, str)->(10,'px')
        self.position = position
        
    def push(self, value):
        if self.stack is None:
            self.stack = []
        self.stack.append(value)
        self.currentSize += 1

    def pop(self) -> int:  # Returns value popped
        self.currentSize -=1
        return self.stack.pop()

    def size(self) -> int:
        return self.currentSize

    def isEmpty(self) -> bool:
        return self.size() == 0

    def printStack(self):
        for i in self.stack:
            print(i)
        print("\n")
    
    def fillFromArr(self, data):
        for val in data:
            self.push(val)
        
    def setAnimation(self, ani):
        if not ani:
            tut.tracer(20, 0)
        else:
            tut.tracer(1,5)
        
    def draw(self):
        tut.bgcolor(self.bgColor)
        tut.setup(self.dimensions[0], self.dimensions[1], self.position[0], self.position[1])
        pen = tut.Pen()
        tut.hideturtle()
        pen.pencolor(self.penColor)
        pen.pensize(self.penSize[0])
        self.setAnimation(self.animation)

        pen.penup()
        pen.goto(-len(str(self.data))*7, 20)
        pen.pendown()

        self.fillFromArr(self.data)
        for i in range(0, len(self.data)):

            startingX = pen.xcor()
            #width of the square and height
            w = 40 + self.penSize[0]
            h = 40 + self.penSize[0]
            if len(str(self.data[i])) > 1:
                w += (len(str(self.data[i])) - 1) * 3

            #tracing square, ending at top left corner of current square facing left
            if i != 0:
                pen.right(90)
                pen.forward(h)
            else:
                pen.penup()
                pen.right(90)
                pen.forward(h)
                pen.pendown()
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
            pen.forward(h/2+5)
            pen.write(str(self.data[(len(self.data)-1)-i]), False, align='center', font=['Arial', 8, 'bold'])
            pen.backward(h/2+5)
            pen.right(90)
            pen.forward(w/2)

            #repositioning to top right corner of current square
            pen.penup()
            pen.right(180)
            pen.goto(startingX+w, pen.ycor())
            pen.pendown()

        pen.up()
        pen.goto(self.dimensions[0], self.dimensions[1])
        tut.exitonclick()
        
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    
    myStack = myStack()
    for i in data:
        myStack.push(i)
        tut.clearscreen()
        myStack.draw()

    tut.exitonclick()
    
