from graphics import  *
from Cell import Cell
import random

def printMaze(cells, win):
    for i in range(len(cells)):
        b = cells[i].getWalls()
        for j in range(len(b)):
            b[j].draw(win)

#def createTribCells(row, col, win, w):
    
def createMap(row, col, win, w):
    cells = []
    midcells = []
    sizeRight = False
    while sizeRight == False:
        trib = eval(input("How many tributes will there be:"))
        if trib % 12 == 0:
            num  = (trib / 4) + 4 + ((trib / 4) - 2) # minus 2 instead of one to make the row line up correctly
            if row >= num and col >= num:
                if row % 2 == 0:
                    rowtophalf = ((row - num) // 2) 
                    rowbottomhalf = rowtophalf + num
                if col % 2 == 0:
                    collefthalf = ((col - num) // 2) 
                    colrighthalf = collefthalf + num
                if row % 2 == 1:
                    rowtophalf = ((row - num) // 2) 
                    rowbottomhalf = ((row - num) // 2) + num
                if col % 2 == 1:
                    collefthalf = ((col - num) // 2) 
                    colrighthalf = ((col - num) // 2) + num
                sizeRight = True
            else:
                print("Too many tributes for such a small board")
        else:
            print("Tribute number needs to be divisible by 12")
            
    for i in range(row):
        for j in range(col):
            cell = Cell(i, j, w, rowtophalf, rowbottomhalf, collefthalf, colrighthalf)
            a = cell.get_inMaze()
            if a == True:
                cells.append(cell)
            else:
                midcells.append(cell)
                
    for cell in midcells:
        x = cell.getx()
        y = cell.gety()
        if x == rowtophalf:
            cell.walls[0] = True
        else:
            cell.walls[0] = False
        if y == colrighthalf:
            cell.walls[1] = True
        else:
            cell.walls[1] = False
        if x == rowbottomhalf:
            cell.walls[2] = True
        else:
            cell.walls[2] = False
        if y == collefthalf:
            cell.walls[3] = True
        else:
            cell.walls[3] = False
        
        
    makeHoles(cells, rowtophalf, rowbottomhalf, collefthalf, colrighthalf, row, col)
    makeMidHoles(midcells, rowtophalf, rowbottomhalf, collefthalf, colrighthalf, row, col)
    pedestal = getPeds(rowtophalf, rowbottomhalf, collefthalf, colrighthalf, row, col)
    retval = []
    retval.append(cells)
    retval.append(trib)
    retval.append(pedestal)
    retval.append(midcells)
    return retval

def getPeds(rtop, rbot, cleft, cright, row, col):
    retval = []
    a = (rtop + 2, cleft + 1)
    retval.append(a)
    while (a[0] != rbot - 2):
        w = (a[0] + 2, a[1])
        retval.append(w)
        a = w
    b = (rbot - 1, cleft + 2)
    retval.append(b)
    while (b[1] != cright - 2):
        x = (b[0], b[1] + 2)
        retval.append(x)
        b = x
    c = (rbot - 2, cright - 1)
    retval.append(c)
    while(c[0] != rtop + 2):
        y = (c[0] - 2, c[1])
        retval.append(y)
        c = y
    d = (rtop + 1, cright - 2)
    retval.append(d)
    while(d[1] != cleft + 2):
        z = (d[0], d[1] - 2)
        retval.append(z)
        d = z
    return retval

def makeMidHoles(midcells, rtop, rbot, cleft, cright, row, col):
    rsecond = (rtop + rbot) // 2
    csecond = (cleft + cright) // 2
    rfirst = (rtop + rsecond) // 2
    rthird = ((rsecond + rbot) // 2) + 1
    cfirst = (cleft + csecond) // 2
    cthird = ((csecond + cright) // 2) + 1
    rowopenings = [rfirst, rsecond, rthird]
    colopenings = [cfirst, csecond, cthird]
    for cell in midcells:
        if cell.walls[0] == True:
            for r in range(len(rowopenings)):
                if cell.y == rowopenings[r]:
                    cell.walls[0] = False
        if cell.walls[1] == True:
            for r in range(len(rowopenings)):
                if cell.x == colopenings[r]:
                    cell.walls[1] = False
        if cell.walls[2] == True:
            for r in range(len(rowopenings)):
                if cell.y == rowopenings[r]:
                    cell.walls[2] = False
        if cell.walls[3] == True:
            for r in range(len(rowopenings)):
                if cell.x == colopenings[r]:
                    cell.walls[3] = False
def makeHoles(cells, rtop, rbot, cleft, cright, row, col):
    northHoles = []
    northTemp = []
    southHoles = []
    southTemp = []
    eastHoles = []
    eastTemp = []
    westHoles = []
    westTemp = []
    rsecond = (rtop + rbot) // 2
    csecond = (cleft + cright) // 2
    rfirst = (rtop + rsecond) // 2
    rthird = ((rsecond + rbot) // 2) + 1
    cfirst = (cleft + csecond) // 2
    cthird = ((csecond + cright) // 2) + 1
    
    n1 = (rfirst , cleft - 1)
    n2 = (rsecond, cleft - 1)
    n3 = (rthird, cleft - 1)
    northTemp.append(n1)
    northTemp.append(n2)
    northTemp.append(n3)
    for i in northTemp:
        for j in range(len(cells)):
            if issame(cells[j],i[0],i[1]) == True:
                northHoles.append(cells[j])

    s1 = (rfirst , cright + 1)
    s2 = (rsecond, cright + 1)
    s3 = (rthird, cright + 1)
    southTemp.append(s1)
    southTemp.append(s2)
    southTemp.append(s3)
    for i in southTemp:
        for j in range(len(cells)):
            if issame(cells[j],i[0],i[1]) == True:
                southHoles.append(cells[j])

    e1 = (rtop - 1, cfirst)
    e2 = (rtop - 1, csecond)
    e3 = (rtop - 1, cthird)
    eastTemp.append(e1)
    eastTemp.append(e2)
    eastTemp.append(e3)
    for i in eastTemp:
        for j in range(len(cells)):
            if issame(cells[j],i[0],i[1]) == True:
                eastHoles.append(cells[j])

    w1 = (rbot + 1, cfirst)
    w2 = (rbot + 1, csecond)
    w3 = (rbot + 1, cthird)
    westTemp.append(w1)
    westTemp.append(w2)
    westTemp.append(w3)
    for i in westTemp:
        for j in range(len(cells)):
            if issame(cells[j],i[0],i[1]) == True:
                westHoles.append(cells[j])
        
    for hole in southHoles:
        hole.walls[0] = False
    for hole in eastHoles:
        hole.walls[1] = False
    for hole in northHoles:
        hole.walls[2] = False
    for hole in westHoles:
        hole.walls[3] = False
        
    
             
def issame(cell, x, y):
    return cell.x == x and cell.y == y

def checkNeighbors(cell, cells):
    neighbors = []
    temp = []
    top = (cell.x, cell.y - 1)
    right = (cell.x + 1, cell.y)
    bottom = (cell.x , cell.y + 1)
    left = (cell.x - 1, cell.y)
    temp.append(top)
    temp.append(right)
    temp.append(bottom)
    temp.append(left)
    if cell.inMaze == True:
        for i in temp:
            for j in range(len(cells)):
                if cells[j].visited == False and issame(cells[j],i[0],i[1]) == True:
                    neighbors.append(cells[j])

    if len(neighbors) > 0:
        r = random.choice(neighbors)
        return r
    else:
        return 3

def removeWalls(a, b):
    one = a.x - b.x
    two = a.y - b.y
    if one == 1:
        a.walls[3] = False
        b.walls[1] = False
    elif one == -1:
        a.walls[1] = False
        b.walls[3] = False
    if two == 1:
        a.walls[0] = False
        b.walls[2] = False
    elif two == -1:
        a.walls[2] = False
        b.walls[0] = False

def createMaze(cells):
    stack = []
    current = random.choice(cells)
    current.visited = True
    second = checkNeighbors(current, cells)
    while second:
        if second != 3:
            second.visited = True
            stack.append(current)
            removeWalls(current, second)
            current = second
            second = checkNeighbors(current, cells)
            #print("!")
        elif len(stack) > 0:
            current = stack.pop()
            second = checkNeighbors(current, cells)
        elif second == 3:
            second = current
            second.visited = True
            stack.append(current)
            removeWalls(current, second)
            current = second
            second = checkNeighbors(current, cells)
            break
    return cells

