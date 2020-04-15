import turtle as tut


class myStack:
    def __init__(self, data=None):
        self.data = data
        self.currentSize = 0
        
    def push(self, value):
        if self.data is None:
            self.data = []
        self.data.append(value)
        self.currentSize += 1

    def pop(self) -> int:  # Returns value popped
        self.currentSize -=1
        return self.data.pop()

    def size(self) -> int:
        return self.currentSize

    def isEmpty(self) -> bool:
        return self.size() == 0

    def printStack(self):
        for i in self.data:
            print(i)
        print("\n")
        
    def draw(self):
        tut.setup(1500, 700)
        pen = tut.Pen()
        tut.hideturtle()

        print("pen positon: " + str(pen.pos()))

        pen.penup()
        pen.goto(-len(str(self.data))*7, 20)
        pen.pendown()

        for i in range(0, len(self.data)):

            startingX = pen.xcor()
            #width of the square and height
            w = 40
            h = 40
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
            print("drawing element: " +
                  str(self.data[i])+" at positon: "+str(pen.pos()))

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

        
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    
    myStack = myStack()
    # print("The stack should be empty and returned "+str(myStack.isEmpty())+" and shouldve returned True \n")
    for i in data:
        myStack.push(i)
        tut.clearscreen()
        myStack.draw()
    # print("Stack after added numbers 1 through 5: \n size: "+str(myStack.size()))    
    #myStack.printStack()
    #print("Stack after popping "+str(myStack.pop()) +
          #" from the stack: \n size: "+str(myStack.size()))
    #myStack.printStack()
    #print("Stack after popping "+str(myStack.pop()) +
          #" from the stack: \n size: "+str(myStack.size()))
    #myStack.printStack()
    
    tut.exitonclick()
    