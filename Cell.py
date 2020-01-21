from graphics import *
import random

class Cell:
    def __init__(self, x, y, w, rt, rb, cl, cr):
        self.x = x
        self.y = y
        self.w = w
        self.walls = [True, True, True, True]
        self.inMaze = True
        if (rt <= x and x <= rb) and (cl <= y and y <= cr) == True:
            self.inMaze = False
            
        self.visited = False

    def getx(self):
        return self.x
    def gety(self):
        return self.y

    def __str__(self):
        return '({},{})'.format(self.x,self.y)

    def getWalls2(self):
        return self.walls
    
    def getWalls(self):
        x = self.x * self.w
        y = self.y * self.w
        w = self.w
        lines = []
        if self.inMaze == True:
            if self.walls[0] == True:
                lines.append(Line(Point(x , y), Point(x + w , y)))
            if self.walls[1] == True:
                lines.append(Line(Point(x + w , y), Point(x + w , y + w)))
            if self.walls[2] == True:
                lines.append(Line(Point(x + w , y + w), Point(x , y + w)))
            if self.walls[3] == True:
                lines.append(Line(Point(x , y + w), Point(x , y)))
            return lines
    def setWalls(self, walls):
        self.walls = walls
    def get_inMaze(self):
        return self.inMaze
    
    def drawRect(self):
        x = self.x * self.w
        y = self.y * self.w
        w = self.w
        aRect = Rectangle(Point(x , y) , Point(x + w , y + w))
        aRect.setFill(color_rgb(34,233,111))
        aRect.setOutline("")
        return aRect
    
class Location:
    def __init__(self, x, y, w, walls):
        self.x = x
        self.y = y
        self.w = w
        self.walls = walls
        self.isOccupied = False
        self.occupiedBy = None
    def __eq__(self, location):
        if (self.x == location.x and self.y == location.y) == True:
            return True
        else:
            return False
    def __hash__(self):
        return hash(self.x)
    def getLocation(self, location):
        return (self.x,self.y)
    def filledIn(self, win, color, name):
        x = (self.x * self.w) + 1
        y = (self.y * self.w) +1
        w = self.w
        aRect = Rectangle(Point(x , y) , Point(x + w - 1 , y + w - 1))
        center = aRect.getCenter()
        aRect.setFill(color)
        t = Text(center, name)
        t.setSize(6)
        aRect.setOutline("")
        aRect.draw(win)
        t.draw(win)
        retval = []
        retval.append(aRect)
        retval.append(t)
        return retval
    def __str__(self):
        return '({},{})'.format(self.x,self.y)
    def getNeighbors(self, locList):
        retval = []
        if self.walls[0] == False:
            for loc in locList:
                if (self.x == loc.x and self.y - 1 == loc.y) == True:
                    retval.append(loc)
        if self.walls[1] == False:
            for loc in locList:
                if (self.x + 1 == loc.x and self.y == loc.y) == True:
                    retval.append(loc)
        if self.walls[2] == False:
            for loc in locList:
                if (self.x == loc.x and self.y + 1 == loc.y) == True:
                    retval.append(loc)
        if self.walls[3] == False:
            for loc in locList:
                if (self.x - 1 == loc.x and self.y == loc.y) == True:
                    retval.append(loc)
        return retval

class Tribute:
    def __init__(self, location, number):
        self.dict = {}
        self.location = location
        self.movespeed = random.random() * 10
        self.shapes = None
        self.isDead = False
        self.kills = 0
        alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if number % 12 == 1:
            num = number // 12
            self.name = "1" + alph[num]
            self.color = "cornflowerblue"
        elif number % 12 == 2:
            num = number // 12
            self.name = "2" + alph[num]
            self.color = "gray"
        elif number % 12 == 3:
            num = number // 12
            self.name = "3" + alph[num]
            self.color = "yellow"
        elif number % 12 == 4:
            num = number // 12
            self.name = "4" + alph[num]
            self.color = "darkgreen"
        elif number % 12 == 5:
            num = number // 12
            self.name = "5" + alph[num]
            self.color = "red"
        elif number % 12 == 6:
            num = number // 12
            self.name = "6" + alph[num]
            self.color = "orange"
        elif number % 12 == 7:
            num = number // 12
            self.name = "7" + alph[num]
            self.color = "blue"
        elif number % 12 == 8:
            num = number // 12
            self.name = "8" + alph[num]
            self.color = "purple"
        elif number % 12 == 9:
            num = number // 12
            self.name = "9" + alph[num]
            self.color = "pink"
        elif number % 12 == 10:
            num = number // 12
            self.name = "10" + alph[num]
            self.color = "tan"
        elif number % 12 == 11:
            num = number // 12
            self.name = "11" + alph[num]
            self.color = "brown"
        elif number % 12 == 0:
            num = number // 12
            self.name = "12" + alph[num]
            self.color = "beige"
    def addKills(self, kills):
        self.kills += kills
    def getColor(self):
        return self.color
    def getLoc(self):
        return self.location
    def getName(self):
        return self.name
    def countMove(self, move):
        if move not in self.dict:
            self.dict[move] = 1
        else:
            self.dict[move] += 1
    
