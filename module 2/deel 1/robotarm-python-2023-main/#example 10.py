from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

COUNT_1 = 9
COUNT_2 = 8
for _ in range(6, 2, -1):
    robotArm.grab()
    for _ in range(COUNT_1):robotArm.moveRight()
    robotArm.drop()
    for _ in range(COUNT_2):robotArm.moveLeft()
    COUNT_1 -= 2
    COUNT_2 -= 2

    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

