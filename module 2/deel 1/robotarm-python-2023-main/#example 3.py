#example 3
from RobotArm import RobotArm
i= 1
robotArm = RobotArm('exercise 3')

for i in range (4):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()