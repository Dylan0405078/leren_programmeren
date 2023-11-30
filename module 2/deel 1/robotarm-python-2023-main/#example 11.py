from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')


for i in range(8):
    robotArm.moveRight()
for i in range (9):   
    robotArm.grab()

    blokje_color = robotArm.scan()

    if blokje_color == 'white':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.moveLeft()
    else:
        robotArm.drop()
        if i < 8:
            robotArm.moveLeft()
        


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
