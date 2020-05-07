import turtle as tut


class myArray:
    def __init__(self, data, animation, dimensions, bgColor, penColor, penSize, position):
        self.data = data                #A list
        self.animation = animation      #A boolean
        self.dimensions = dimensions    #A tuple (x,y)
        self.penColor = penColor        #A string 'BLACK'|'WHITE|etc.
        self.penSize = penSize          #A tuple (int, str)->(10,'px')
        self.bgColor = bgColor          #A string 'BLACK'|'WHITE|etc.
        self.position = position        #A tuple (x,y)
        
    def printElements(self):
        print(self.data)


    def setAnimation(self, ani):
        if not ani:
            tut.tracer(20,0)
        else:
            tut.tracer(1,5)

    def draw(self):
        tut.bgcolor(self.bgColor) #changes the bg color
        tut.setup(self.dimensions[0], self.dimensions[1], self.position[0], self.position[1]) #dimension of screen
        pen = tut.Pen()                                     ########################
        tut.hideturtle()                                    ##PEN AND CANVAS SETUP##
        pen.color(self.penColor)                            ######################## 
        pen.pensize(self.penSize[0]) #only get the number                   
        self.setAnimation(self.animation)                   
        
        pen.penup()
        pen.goto(-len(str(self.data))*7,20)
        pen.pendown()

        for i in range(0,len(self.data)):
            startingX = pen.xcor()
            #width of the square and height
            w = 40 + self.penSize[0]
            h = 40 + self.penSize[0]
            if len(str(self.data[i])) > 1:
                w += (len(str(self.data[i])) - 1) * 3
                
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
            pen.forward(h/2+7)
            pen.write(str(self.data[i]), True, align='center')
            pen.backward(h/2+7)
            pen.right(90)
            pen.forward(w/2)
            
            #repositioning to top right corner of current square
            pen.penup()
            pen.right(180)
            pen.goto(startingX+w, pen.ycor())
            pen.pendown()
        
        pen.up()
        pen.goto(self.dimensions[0],self.dimensions[1])
        tut.exitonclick()

if __name__ == "__main__":
    data = [10,2.5,3,4,5]  
    myList = myArray(data)
    
    animation = False

    if not animation:
        tut.tracer(0, 0)
    
    myList.printElements()
    myList.draw()
    tut.update()
    tut.exitonclick()
