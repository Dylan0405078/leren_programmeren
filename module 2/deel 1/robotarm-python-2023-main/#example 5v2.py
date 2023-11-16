#example 5
from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

for _ in range(7):
    robotArm.moveRight()

for _ in range (8):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    if _ < 7:
        for _ in range (2):
            robotArm.moveLeft()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
