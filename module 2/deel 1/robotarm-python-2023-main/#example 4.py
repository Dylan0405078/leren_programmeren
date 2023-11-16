#example 4
from RobotArm import RobotArm
i= 1
aantal = 2
robotArm = RobotArm('exercise 4')
robotArm.speed = 

for i in range (5):
    if i == 4:
        aantal = 1
    robotArm.grab()
    for _ in range (aantal):
        robotArm.moveRight()
    robotArm.drop()
    if i < 4:
        for _ in range (2):
             robotArm.moveLeft()

robotArm.moveRight()

for _ in range (4):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()

    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()