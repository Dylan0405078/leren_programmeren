#example 5

#example 5
from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

for _ in range(7):
    robotArm.moveRight()

for _ in range (8):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    for _ in range (2):
        robotArm.moveLeft()






# Wait for the window to close after your code
robotArm.wait()
