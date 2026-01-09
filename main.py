from simulator import robot, FORWARD, BACKWARD, STOP
x = 2
# TODO: Write your code here!
# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar() to sense 
rd =1
ld = 1
wd = 1
d = 1
def wall_check():
    ld =robot.left_sonar() 
    rd = robot.right_sonar() 
#to not hit walls
distance = 1
def lspin():
    robot.motors(left=BACKWARD, right=FORWARD, seconds= 1)
#makes robot spin left
def rspin():
    robot.motors(right=BACKWARD, left=FORWARD, seconds= 1)
#makes robot spin right
robot.motors(left=FORWARD, right= FORWARD,seconds=3)
robot.right_sonar
while x > 1:
    choose = int(input("input 1 if you want to move forawrd or backwards left or right. Input 2 if you want to donut or 3 if you want to spin forever 4 for following wall anything else to leave\n"))
    if choose == 1:
        fd = int(input("input 1 to go forward or backwards or input 2 for left or right"))

        if fd == 1:
            fb = int(input("1 for forward 2 for backwards"))
            if fb == 1:
                distance = distance // 1
                for loop in range ((int(input("input the distance you want to go in secconds"))//1) * 10):
                    wall_check()
                    robot.motors(left= FORWARD,right= FORWARD, seconds=0.1)
                    # print(robot.right_sonar())
                    if robot.right_sonar() < 5:
                        break
                    #go forward
            elif fb == 2:
                distance = distance // 1
                for loop in range ((int(input("input the distance you want to go in secconds"))//1) * 10):
                    wall_check()
                    robot.motors(left= BACKWARD,right= BACKWARD, seconds=0.1)
                    # print(robot.left_sonar())
                    if robot.left_sonar() < 5:
                        break
                    #go backwards
        elif fd == 2:
            d = int(input("input 1 for left 2 for right"))
            if d == 1:
                robot.motors(left =BACKWARD, right=FORWARD, seconds=int(input("input the secconds to move left")))
                
            #turn left
            if d == 2:
                robot.motors(left =FORWARD, right=BACKWARD, seconds=int(input("input the secconds to move right")))
        else:
            print("you did something wrong")
    elif choose == 2:
        donut = int(input("input 1 for left donut input 2 for right donut"))
        if donut == 1: 
            robot.motors(right=FORWARD, left= STOP, seconds=6)
             # print(robot.right_sonar())
            wall_check
            if robot.left_sonar() < 5:
                 break
            
        elif donut == 2:
            robot.motors(left= FORWARD, right= STOP, seconds= 6)
             # print(robot.right_sonar())
            wall_check
            if robot.right_sonar() < 5:
                 break
            
        else:
            print("you did something wrong")
    elif choose == 3:
        which = int(input("input 1 for left 2 for right"))
        if which == 1:
            # print("input 1 to break the function")
            wd = 1
            while wd < 2:

                lspin()

        elif which == 2:
            wd = 1
            # print("input 1 to break the function")
            while wd < 2:

                    # wd = 3
                rspin()
        else:
            print("you did something wrong")
    elif choose == 4:
        distance = distance // 1
        z = 2
        while z > 1:
            for loop in range(250):
                wall_check()
                robot.motors(left= FORWARD,right= FORWARD, seconds=0.1)
                # print(robot.left_sonar())
                if robot.right_sonar() < 10:
                    robot.motors(left = FORWARD, right = BACKWARD, seconds= 1.525)
            z = int(input("input 2 to keep going or 1 to stop"))

        

    


# When you're done, close the simulator
robot.exit()