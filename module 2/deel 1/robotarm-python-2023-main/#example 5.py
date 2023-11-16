#example 5
#example 5
from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

i = 8
position = i - 1
current_position = position  

for _ in range(4):
    current_position = position  
    
    robotArm.grab()
    
    for _ in range(current_position):
        robotArm.moveRight()
    
    robotArm.drop()
    
    for _ in range(current_position):
        robotArm.moveLeft()


# Wait for the window to close after your code
robotArm.wait()
