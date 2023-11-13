#example 4
from RobotArm import RobotArm
i= 1
robotArm = RobotArm('exercise 4')

for i in range (5):
    robotArm.grab()
    for i in range (2):
        robotArm.moveRight()
    robotArm.drop()
    for i in range (2):
        robotArm.moveLeft()
for i in range (2):
        robotArm.moveRight()
for i in range (5):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()

    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()