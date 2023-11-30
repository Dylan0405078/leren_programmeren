from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')
count = 0

for _ in range(5):
    for _ in range(6): robotArm.moveRight(); robotArm.grab(); robotArm.moveLeft(); robotArm.drop()
    if count < 4: robotArm.moveRight(); robotArm.moveRight()
    count += 1

robotArm.wait()

