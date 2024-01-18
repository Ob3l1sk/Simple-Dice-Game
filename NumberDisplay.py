from graphics import *
class NumberDisplay:

    def __init__(self,win,value,center,size,title):
            self.win=win
            self.center=center
            self.number=Text(center,value)
            
            self.background="white"
            center2=Point(center.getX(),center.getY()-.75*size)
            corner1=Point(center.getX()-size/2,center.getY()-size/2)
            corner2=Point(center.getX()+size/2,center.getY()+size/2)
            corner3=Point(center2.getX()-size/2,center2.getY()+size/4)
            self.square=Rectangle(corner1,corner2)
            self.titlebox=Rectangle(corner2,corner3)
            self.title=Text(center2,title)

    def changeNumber(self,value):
            self.number.undraw()
            self.number=Text(self.center,value)
            self.number.setSize(36)
            self.number.draw(self.win)

    def display(self,background):
            self.square.draw(self.win)
            self.titlebox.draw(self.win)
            self.title.draw(self.win)
            self.square.setFill(background)
            self.number.setSize(36)
            self.number.draw(self.win)
