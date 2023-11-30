#example 7

from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

count_blauw = 0
count_groen = 0
count_wit = 0
count_rood = 0
# blauw
robotArm.grab()
for i in range(5):
    robotArm.moveRight()
robotArm.drop()
for i in range(4):
    robotArm.moveLeft()



#groen
while count_groen < 2:
    robotArm.grab()
    for i in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(5):
        robotArm.moveLeft()
    count_groen += 1
for i in range(5):
    robotArm.moveRight()
for i in range(4):
        robotArm.moveLeft()
#wit
while count_wit <3:
    robotArm.grab()
    for i in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(5):
        robotArm.moveLeft()
    count_wit += 1
for i in range(5):
    robotArm.moveRight()
for i in range(4):
        robotArm.moveLeft()

#rood
while count_rood < 4:
    robotArm.grab()
    for i in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(5):
        robotArm.moveLeft()
count_rood += 1
robotArm.moveLeft()





# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()