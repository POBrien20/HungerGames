import mazefuncs as m 
from graphics import *
from Cell import Cell
from Cell import Location
from Cell import Tribute
import random

row = eval(input("How many rows will the map be:"))
col = eval(input("How many columns will the map be:"))
w = 16
winx = row * w
winy = col * w
win = GraphWin("My Window", winx, winy)
win.setBackground('white')

def createMaze(row, col, win, w):
    a = m.createMap(row, col, win, w)
    b = m.createMaze(a[0])
    m.printMaze(b, win)
    return a

def createField(row, col, win, w, cells, midcells):
    newcells = []
    for cell in cells:
        loc = Location(cell.x, cell.y, w, cell.walls)
        newcells.append(loc)
    for cell in midcells:
        loc = Location(cell.x, cell.y, w, cell.walls)
        newcells.append(loc)
    return newcells

def printTributes(tributeList):
    retval = []
    for t in tributeList:
        a = t.getColor()
        b = t.getLoc()
        c = t.getName()
        d = b.filledIn(win, a, c)
        t.shapes = d
        retval.append(d)
    return retval

def printTribute(trib):
    shapes = []
    a = trib.getColor()
    b = trib.getLoc()
    c = trib.getName()
    d = b.filledIn(win, a, c)
    shapes.append(d)
    trib.shapes = d

def eraseTribute(trib):
    for s in trib.shapes:
        s.undraw()
    trib.shapes = None
        
def setup():
    b = createMaze(row,col,win,w)
    a = createField(row,col,win,w,b[0],b[3])
    loclist = a
    tribnum = b[1]
    pedtemp = b[2]
    pedestals = []
    for i in pedtemp:
        for j in range(len(a)):
            if m.issame(a[j], i[0], i[1]) == True:
                pedestals.append(a[j])
##    random.shuffle(pedestals)
    tributeList = []
    newloclist = []
    for i in range(tribnum):
        t = Tribute(pedestals[i], i)
        tributeList.append(t)
        for loc in loclist:
            if loc == t.location:
                loc.occupiedBy = t
                
    printTributes(tributeList)

    retval = []
    retval.append(tributeList)
    retval.append(loclist)
    return retval
