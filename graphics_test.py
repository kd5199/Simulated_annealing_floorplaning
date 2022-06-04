from curses.textpad import rectangle
from graphics import *
from Cost_function import *



win = GraphWin("Win",200, 200)
win.setCoords(0,0,5,5)

def drawModule(m1,m2,operator):
    win = GraphWin("Win",1000, 1000)
    win.setCoords(0,0,5,5)
    if(operator=='H'):
        point1 = Point(0,0)
        point2 = Point(m1.width, m1.height)
        point3 = Point(0, m1.height)
        point4 = Point(m2.width,m1.height+m2.height)

    else:
        point1 = Point(0,0)
        point2 = Point(m1.width, m1.height)
        point3 = Point(m1.width, 0)
        point4 = Point(m2.width+m1.width,m2.height)

    Rectangle(point1,point2).draw(win)
    Rectangle(point3,point4).draw(win)
    win.getMouse()


for i in range(50):
    Rectangle(Point(0,0),Point(i, i+1)).draw(win)
    
    m1 = Text(Point(i, i+1),("HI"))
    m2 = Text(Point(i, i+1),"HI")
    m1.draw(win)
    m2.draw(win)
win.getMouse()
# mysquare1=Rectangle()

# mysquare1 = Rectangle(Point(1,1),Point(50,50))
# mysquare2 = Rectangle(Point(20,20),Point(60,60))
# mysquare1.draw(win)
# mysquare2.draw(win)
