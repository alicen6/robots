from sys import exit
import random
from PIL import Image, ImageDraw


# make your robot character

bot_builder = Image.new("RGB", (150, 150), "white")


print "The first step to building your robot is to choose a body."
print "Is your robot plain, does it have buttons, or a screen?"
robot_body = raw_input("plain, buttons, or screen: ")


def bot_body():
    if robot_body == "plain":
        plain = Image.open('/Users/alicen/git/robots/bot_parts/body_plain.jpg')
        bot_builder.paste(plain, (50, 50))
        bot_builder.save("my_bot.jpeg")
        print "Now it's time to select a head."
        bot_head()
    elif robot_body == "buttons":
        buttons = Image.open('/Users/alicen/git/robots/bot_parts/body_buttons.jpg')
        bot_builder.paste(buttons, (50, 50))
        bot_builder.save("my_bot.jpeg")
        print "Now it's time to select a head."
        bot_head()
    elif robot_body == "screen":
        screen = Image.open('/Users/alicen/git/robots/bot_parts/body_screen.jpg')
        bot_builder.paste(screen, (50, 50))
        bot_builder.save("my_bot.jpeg")
        print "Now it's time to select a head."
        bot_head()
    else:
        print "That is not an option, please try again."
        # bot_body()
        exit(0)


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
        pass
    else:
        pass


bot_body()
