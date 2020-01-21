import mazegen as g
from Cell import Location
from Cell import Tribute
import random

def mergeLists(tributeList, locList):
    for trib in tributeList:
        for loc in locList:
            if trib.location == loc:
                loc.isOccupied = True
                loc.occupiedBy = trib
                
def getMove(trib, locList):
    l = trib.location
    neighbors = l.getNeighbors(locList)
    possibleMoves = {}
    t = trib.dict
    newtribs = []
    for n in neighbors:
        possibleMoves[n] = t.get(n, 0)
    vals = list(possibleMoves.values())
    keys = list(possibleMoves.keys())
    valsmin = min(vals)
    tempMoves = []
    actualMoves = []
    for val in range(len(vals)):
        if vals[val] == valsmin:
            tempMoves.append(keys[val])
    for move in tempMoves:
        if move.isOccupied == False:
            actualMoves.append(move)
    if len(actualMoves) != 0:        
        randval = int(random.random() * len(actualMoves))
        move = actualMoves[randval]
    else:
        move = tempMoves[0]
    if type(move) == type(l):
        l.isOccupied = False
        l.occupiedBy = None
        trib.location = move
        move.isOccupied = True
        move.occupiedBy = trib
        trib.countMove(move)
    return locList

def fight(tribA, tribB, locList):
    retval = []
    print("first tribute:", tribA.name, " killcount: ", tribA.kills)
    print("second tribute:", tribB.name, " killcount: ", tribB.kills)
    a = eval(input("input 0 for first tribute, or 1 for second tribue:"))
    if a == 0:
        ayy = kills(tribA, tribB, locList)
        bee = dies(tribB, ayy)
        retval.append(tribA)
        retval.append(bee)
        print(tribB.name, " KILLED BY ", tribA.name)
        print(tribA.name, " killcount: ", tribA.kills)
    else:
        ayy = kills(tribB, tribA, locList)
        bee = dies(tribA, ayy)
        retval.append(tribB)
        retval.append(bee)
        print(tribA.name, " KILLED BY ", tribB.name)
        print(tribB.name, " killcount: ", tribB.kills)
    return retval
    
def kills(killer, victim, locList):
    g.eraseTribute(killer)
    killer.location = victim.location
    for loc in locList:
        if loc.occupiedBy == killer:
            loc.occupiedBy = None
        if loc.occupiedBy == victim:
            loc.occupiedBy = killer
            
    killer.addKills(1)
    g.printTribute(killer)
    return locList
    
def dies(trib, locList):
    g.eraseTribute(trib)
    trib.isDead = True
    l = trib.location
    for loc in locList:
        if l == loc:
            loc.isOccupied == False
            loc.occupiedBy == None
    return locList

def checkifNeighborOccupied(loc, locList):
    neighbors = loc.getNeighbors(locList)
    for n in neighbors:
        if n.isOccupied == True:
            return n.occupiedBy
    return None

def moveTrib(trib, locList):
    g.eraseTribute(trib)
    a = getMove(trib, locList)
    g.printTribute(trib)
    return a 
def moveTribsOnce(tributeList, locList):
    newtribs = []
    for trib in range(len(tributeList)):
        t = tributeList[trib]
        if t.isDead == False:
            a = moveTrib(t, locList)
            b = checkifNeighborOccupied(t.location, locList)
            if b != None:
                winner = fight(t, b, a)
                newtribs.append(winner[0])
                locList = winner[1]
            else:
                newtribs.append(t)
    for trib in newtribs:
        if trib.isDead == True:
            newtribs.remove(trib)
    tributeList = newtribs
    retval = []
    retval.append(list(set(newtribs)))
    retval.append(locList)
    return retval


def moveTribs(tributeList, locList):
    a = moveTribsOnce(tributeList, locList)
    tributeList = a[0]
    locList = a[1]
    retval = []
    retval.append(tributeList)
    retval.append(locList)
    return retval
    
def play():
    a = g.setup()
    tributeList = a[0]
    locList = a[1]
    mergeLists(tributeList, locList)
    inProgress = True
    days = 1
    while inProgress:
        print("--------------DAY ", days,"-------------------")
        print(len(tributeList), " TRIBUTES REMAINING")
        b = moveTribs(tributeList, locList)
        tributeList = b[0]
        locList = b[1]
        if len(tributeList) == 1:
            inProgress = False
        days +=1
    print(tributeList[0].name, "won in", str(days),"days")
play()
