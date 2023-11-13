#example 5
from RobotArm import RobotArm
i= 1
robotArm = RobotArm('exercise 4')

robotArm.grab()
for i in range (8):
    robotArm.moveRight()
robotArm.drop()
for i in range (8):
    robotArm.moveLeft()
robotArm.grab()
for i in range (7):
    robotArm.moveRight()
robotArm.drop()
for i in range (7):
    robotArm.moveLeft()
robotArm.grab()
for i in range (5):
    robotArm.moveRight()
robotArm.drop()
for i in range (5):
    robotArm.moveLeft()
robotArm.grab()
for i in range (4):
    robotArm.moveRight()
robotArm.drop()
for i in range (4):
    robotArm.moveLeft()
robotArm.grab()
for i in range (6):
    robotArm.moveRight()
robotArm.drop()
for i in range (6):
    robotArm.moveLeft()

    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()