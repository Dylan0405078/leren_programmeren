from RobotArm import RobotArm

robotArm = RobotArm('exercise 1')

robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()