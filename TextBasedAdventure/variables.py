#game variables

xPos = 1
yPos = 0

#grid key
#distance == d + n(theDistance)
#enemy == e + n(eLevel) + n(type)
#boss == b + n(floor)
#shop == s + n(type)
#sampGrid = [["0,0,s,1","1,0,e,0","2,0,b,1"],
           #["0,1,e,1","1,1,e,1","2,1,e,1"],
           #["0,2,e,1","1,2,e,0","2,2,e,1"]]
grid = []
gridStuff = []
gridLoc = 0
gridMX = 1
gridMY = 1
#enemy variables
enemyHP = 0

#player variables
playerName = "yarmen"
charCode = ""

playerClass = ""
playerRace = ""
playerGame = ""
playerChar = ""
playerHP = 0
playerMaxHP = 100

strength = 10
strengthMod = 0
intelligence = 10
intelligenceMod = 0
speed = 10
speedMod = 0
vitality = 10
vitalityMod = 0

#shop variables
money = 0
fruit = 0
axe = False
sword = False

#potion stat buffs
intSp = 0
speSp = 0
strSp = 0
vitSp = 0
