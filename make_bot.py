from sys import exit
import random
import PIL

# make your robot character

print "The first step to building your robot is to choose a body."
print "Is your robot plain, does it have buttons, or a screen?"
robot_body = raw_input("plain, buttons, or screen")


def bot_body():
    if robot_body == "plain":
        # append image?
        pass
        print "Now it's time to select a head."
        bot_head()
    elif robot_body == "buttons":
        pass
        print "Now it's time to select a head."
        bot_head()
    elif robot_body == "screen":
        pass
        print "Now it's time to select a head."
        bot_head()
    else:
        print "That is not an option, please try again."
        bot_body()


def bot_head():
    print "The options are as follows:"
    print "Dome, square, round, tube, or T-shaped"
    robot_head = raw_input("select one")

    if robot_head == "dome":
        bot_arms()
    elif robot_head == "square":
        bot_arms()
    elif robot_head == "round":
        bot_arms()
    elif robot_head == "tube":
        bot_arms()
    elif robot_head == "T-shaped":
        bot_arms()
    else:
        print "That is not an option, please try again."
        bot_head()


def bot_arms():
    print "Does your robot fight or help?"
    robot_use = raw_input("select one")

    if robot_use == "fight":
