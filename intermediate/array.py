import turtle as tut


class myArray:
    def __init__(self, data):
        self.data = data
        
    def printElements(self):
        print(self.data)

    def draw(self):
        tut.setup(1500,700)
        pen = tut.Pen()
        tut.hideturtle()
        
        print("pen positon: " + str(pen.pos()))
        print("canvaz dimensions: " + "("+ str(tut.window_width()) + "," + str(tut.window_height()) +")")
        
        pen.penup()
        pen.goto(-len(str(self.data))*7,20)
        pen.pendown()
        
        for i in range(0,len(self.data)):
            
            startingX = pen.xcor()
            #width of the square and height
            w = 40
            h = 40
            if len(str(self.data[i])) > 1:
                w += (len(str(self.data[i])) - 1) * 3
                
            print("width: "+str(w))
            #tracing square, ending at top left corner of current square facing left
            pen.right(90)
            pen.forward(h)
            pen.left(90)
            pen.forward(w)
            pen.left(90)
            pen.forward(h)
            pen.left(90)
            pen.forward(w)
            print("drawing element: "+str(self.data[i])+" at positon: "+str(pen.pos()))
            
            #drawing data into square
            pen.penup()
            pen.backward(w/2)
            print("width/2 = "+str(w/2))
            pen.left(90)
            pen.forward(h/2)
            pen.write(str(self.data[i]), True, align='center')
            pen.backward(h/2)
            pen.right(90)
            pen.forward(w/2)
            
            #repositioning to top right corner of current square
            pen.penup()
            pen.right(180)
            pen.goto(startingX+w, pen.ycor())
            pen.pendown()


if __name__ == "__main__":
    data = [10,2.5,3,4,5]  #TODO data must be given by user# 
    myList = myArray(data)
    
    animation = False

    if not animation:
        tut.tracer(0, 0)
    
    myList.printElements()
    myList.draw()
    tut.update()
    tut.exitonclick()
