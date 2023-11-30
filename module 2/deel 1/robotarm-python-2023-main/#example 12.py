from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
count_total = 10
count = 9
count_div = count - 1
# print(count_div)

for i in range(8):
    robotArm.moveRight()

for i in range(9):
    robotArm.grab()
    blokje_color = robotArm.scan()

    if blokje_color == 'red':
        for i in range(count_total - count):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(count_total - count_div):
            robotArm.moveLeft()
        count -= 1
        count_div -= 1
    else:
        robotArm.drop()
        if i < 8:
            robotArm.moveLeft()
        count -= 1
        count_div -= 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
