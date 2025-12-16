from simulator import robot, FORWARD, BACKWARD, STOP
x = 2
# TODO: Write your code here!
# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar() to sense 
rd =1
ld = 1
wd = 1
def wall_check():
    robot.left_sonar = ld
    robot.right_sonar = rd

def lspin():
    robot.motors(left=BACKWARD, right=FORWARD, seconds= 1)
def rspin():
    robot.motors(right=BACKWARD, left=FORWARD, seconds= 1)
robot.motors(left=FORWARD, right= FORWARD,seconds=3)
while x > 1:
    choose = int(input("input 1 if you want to move forawrd or backwards left or right. Input 2 if you want to donut or 3 if you want to spin forever\n"))
    if choose == 1:
        fd = int(input("input 1 to go forward or backwards or input 2 for left or right"))
        distance = int(input("input the distance you want to go in secconds"))
        if fd == 1:
            fb = int(input("1 for forward 2 for backwards"))
            if fb == 1:
                robot.motors(left= FORWARD,right= FORWARD, seconds=distance)
            elif fb == 2:
                robot.motors(left=BACKWARD,right=BACKWARD, seconds= distance)
        if fd == 2:
            d = int(input("input 1 for left and 2 for right"))
            if d == 1:
                wall_check()
                if distance < rd:
                    robot.motors(left=BACKWARD, right=FORWARD, seconds= distance)
                else:
                    print("we dont want to crash")
            if d == 2:
                robot.motors(left=BACKWARD, right=FORWARD, seconds= distance)

    if choose == 2:
        donut = int(input("input 1 for left donut input 2 for right donut"))
        if donut == 1: 
            robot.motors(right=FORWARD, left= STOP, seconds=6)
        if donut == 2:
            robot.motors(left= FORWARD, right= STOP, seconds= 6)
            #TODO i need to do this
    if choose == 3:
        which = int(input("input 1 for left 2 for right"))
        if which == 1:
            while wd < 2:
                lspin()
        if which == 2:
            while wd < 2:
                rspin()


# When you're done, close the simulator
robot.exit()