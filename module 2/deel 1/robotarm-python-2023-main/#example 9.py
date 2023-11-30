
from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')
# blauw, groen, wit, rood
for color in range(4):
    for _ in range(color + 1):
        robotArm.grab()
        for i in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(5):
            robotArm.moveLeft()

            if _ < 4:

                for i in range(5):
                    robotArm.moveRight()
                for i in range(4):
                    robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van het venster:
robotArm.wait()