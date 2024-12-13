import random as r
import time as t
import variables as g


def stringToList(string):
    tempList = string.split(",")
    return tempList

def listToString(list):
    tempString = ""
    l = len(list)
    for e in list:
        tempString += str(e)
        l -= 1
        if l > 0:
            tempString += ","
    return tempString

def makeEmptyGrid(gridMX, gridMY):
    temp = []
    for i in range(0, gridMY):
        for j in range(0, gridMX):
            temp.append("E")
        g.grid.append(temp)
        temp = []

def makeGrid(gridMX, gridMY):
    foundPlayer = False
    for y in range(gridMY):
        rowFull = False
        temp = 0
        while rowFull == False:
            for x in range(gridMX):
                if foundPlayer == False:
                    if y == g.yPos and x == g.xPos:
                        foundPlayer = True
                        g.grid[y][x] = str(g.xPos) + "," + str(g.yPos) + ",e,0,d,1"
                else:
                    if g.grid[y][x] == "E":
                        #check left
                        if x - 1 >= 0 and g.grid[y][x - 1] != "E":
                            g.grid[y][x] = str(x) + "," + str(y) + ",e,1,d," + fillGridLoc(x, y)
                        #check right
                        elif x + 1 < gridMX and g.grid[y][x + 1] != "E":
                            g.grid[y][x] = str(x) + "," + str(y) + ",e,1,d," + fillGridLoc(x, y)
                        #check down
                        elif y - 1 >= 0 and g.grid[y - 1][x] != "E":
                            g.grid[y][x] = str(x) + "," + str(y) + ",e,1,d," + fillGridLoc(x, y)
                        #check up
                        elif y + 1 < gridMY and g.grid[y + 1][x] != "E":
                            g.grid[y][x] = str(x) + "," + str(y) + ",e,1,d," + fillGridLoc(x, y)
                    else:
                        temp += 1
            if temp == gridMX:
                rowFull = True
            else:
                temp = 0


def fillGridLoc(x, y):
    tempDist = 99999
    #check left
    if x - 1 >= 0 and g.grid[y][x - 1] != "E":
        temp = g.grid[y][x - 1]
        temp = stringToList(temp)
        tempD = int(temp[-1])
        if tempD < tempDist:
            tempDist = tempD
    #check right
    if x + 1 < g.gridMX and g.grid[y][x + 1] != "E":
        temp = g.grid[y][x + 1]
        temp = stringToList(temp)
        tempD = int(temp[-1])
        if tempD < tempDist:
            tempDist = tempD
    #check down
    if y - 1 >= 0 and g.grid[y - 1][x] != "E":
        temp = g.grid[y - 1][x]
        temp = stringToList(temp)
        tempD = int(temp[-1])
        if tempD < tempDist:
            tempDist = tempD
    #check up
    if y + 1 < g.gridMY and g.grid[y + 1][x] != "E":
        temp = g.grid[y + 1][x]
        temp = stringToList(temp)
        tempD = int(temp[-1])
        if tempD < tempDist:
            tempDist = tempD

    return str(tempDist + 1)


def moveMe():
    keepGoing = True

    while keepGoing == True:
        moveDir = input("Which direction do you want to go... (North, South, East, West) ")
        moveDir = moveDir.lower()
        gridLoc = g.grid[g.yPos][g.xPos]

        keepGoing = False

        if moveDir == "north" and int(gridLoc[2]) < g.gridMY - 1:
            g.yPos += 1
        elif moveDir == "south" and int(gridLoc[2]) > 0:
            g.yPos -= 1
        elif moveDir == "east" and int(gridLoc[0]) < g.gridMX - 1:
            g.xPos += 1
        elif moveDir == "west" and int(gridLoc[0]) > 0:
            g.xPos -= 1
        else:
            print("You walk into a wall... ouch!")
            keepGoing = True


def makeMe():
    g.playerName = input("What's your name? ")

    if g.playerName == "dev1":
        g.playerClass = "Warrior"
        g.strength += 2
        g.vitality += 1
        g.intelligence -= 2
        g.speed -= 1

        g.playerRace = "Orc"
        g.strength += 2
        g.vitality += 2
        g.intelligence -= 2
        g.speed -= 2

        updatePlayerMods()

    else:

        print("CLASSES")
        print("Warrior")
        print("Archer")
        print("Wizard")

        finish = False
        while finish == False:

            finish = True

            pick = input("Which class are you? ")
            pick = pick.lower()

            if pick == "warrior":
                print("Oh, so you're a warrior. That explains the tree trunk arms.")
                g.playerClass = "Warrior"
                g.strength += 2
                g.vitality += 1
                g.intelligence -= 2
                g.speed -= 1
            elif pick == "archer":
                print("Oh, an archer I see. I guess the bow and quiver should have given me a clue.")
                g.playerClass = "Archer"
                g.speed += 2
                g.vitality += 1
                g.strength -= 1

            elif pick == "wizard":
                print("Oh... a wizard huh? Well try not to cast any spells inside houses please.")
                g.intelligence += 2
                g.strength -= 2
                g.vitality -= 1
                g.speed -= 1
            else:
                finish = False

        if finish == True:
            print("LOADING")
            t.sleep(0.6)

        print("RACES")
        print("Human")
        print("Elf")
        print("Orc")

        finish = True
        while finish == True:

            finish = False
            pick = input("I make mistakes all the time, so I'll just ask, what race are you? ")
            pick = pick.lower()

            if pick == "human":
                print("Nice, a fellow human. Good luck dungeon diving!")
                g.playerRace = "Human"
                g.strength += 1
                g.vitality += 1
                g.intelligence += 1
                g.speed += 1
            elif pick == "elf":
                print("Sigh... another elf huh? Always flaunting your awesomeness, well good luck dungeon diving.")
                g.playerRace = "Elf"
                g.strength -= 2
                g.vitality -= 1
                g.intelligence += 2
                g.speed += 2
            elif pick == "orc":
                print("Wow, an orc! You guys sure are big! Good luck dungeon diving, I almost feel bad for the zombies.")
                g.playerRace = "Orc"
                g.strength += 2
                g.vitality += 2
                g.intelligence -= 2
                g.speed -= 2
            else:
                finish = True

        print("LOADING")
        t.sleep(0.6)

    g.charCode = g.playerClass + g.playerRace
    g.charCode = g.charCode.lower()

    updatePlayerMods()

    g.playerMaxHP = 20 + g.vitalityMod * 3
    g.playerHP = g.playerMaxHP

    showPlayerInfo()

def showPlayerInfo():
    print("")
    print("PLAYER INFO")
    print("Class: " + g.playerClass)
    print("Race: " + g.playerRace)
    print("Health: " + str(g.playerHP))
    print("")
    print("PLAYER STATS")
    print("Strength: " + str(g.strength))
    print("Intelligence: " + str(g.intelligence))
    print("Vitality: " + str(g.vitality))
    print("Speed: " + str(g.speed))
    print("")


def updatePlayerMods():
    g.strengthMod = (g.strength + g.strSp - 10) // 2
    g.intelligenceMod = (g.intelligence + g.intSp - 10) // 2
    g.vitalityMod = (g.vitality + g.vitSp - 10) // 2
    g.speedMod = (g.speed + g.speSp - 10) // 2


def introStory():
    print("It all started when...")
    t.sleep(2)



def combat():
    tempL = stringToList(g.gridLoc)
    print(tempL)
    if tempL[2] == "e":
        if tempL[3] == "0":
            print("This enemy has already been defeated.")
            print("")
        elif tempL[3] >= "1":
            print("Get ready for battle!")
            print("")
            g.enemyHP = 20
    while g.enemyHP > 0:
        updatePlayerMods()

        dmg = r.randint(1, 6) + g.strengthMod
        dmg *= g.strengthMod
        g.enemyHP -= dmg
        print("You deal " + str(dmg) + " damage.")
        print("The enemy has " + str(g.enemyHP) + "health left.")
        print("")
        t.sleep(0.6)

        if g.enemyHP > 0:
            dmg = r.randint(1, 6)
            dmg /= g.vitalityMod
            g.playerHP -= dmg
            print("The enemy deals " + str(dmg) + " damage.")
            print("You have " + str(g.playerHP) + "health left.")
            print("")
            t.sleep(0.6)

        if g.enemyHP <= 0:
            print("YOU DID IT!!!")
            #Set enemy to defeated
            tempL[3] = 0
            tempS = listToString(tempL)
            g.grid[g.yPos][g.xPos] = tempS
            print("")
            #g.money += int(g.gridLoc[6]) * 10
            #print("You got " + str(g.gridLoc[6] * 10) + " moneys for some reason.")
            #print("You have " + g.money + " money for some reason.")
            # gridLoc[6] = 0
            # g.grid[g.yPos][g.xPos] = gridLoc
