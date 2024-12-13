import time as t
import random as r
import variables as g
import functions as f

f.makeMe()
# f.introStory()

g.gridMX = 5
g.gridMY = 5

f.makeEmptyGrid(g.gridMX, g.gridMY)
f.makeGrid(g.gridMX, g.gridMY)

while True:
    g.gridLoc = g.grid[g.yPos][g.xPos]
    print("Current Location: " + str(g.xPos) + " " + str(g.yPos))
    print("")

    # combat
    f.combat()

    if g.gridLoc[4] == "s" and g.gridLoc[6] == 1:
        pass

    f.moveMe()


