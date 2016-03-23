from sys import exit
import random
from PIL import Image, ImageDraw


# make your robot character

bot_builder = Image.new("RGB", (150, 150), "white")


def bot_body():
    print "The first step to building your robot is to choose a body."
    print "Is your robot plain, does it have buttons, or a screen?"
    body_input = raw_input("plain, buttons, or screen: ")
    robot_body = body_input.lower()

    if robot_body == "plain":
        plain = Image.open('/Users/alicen/git/robots/bot_parts/body_plain.jpg')
        bot_builder.paste(plain, (50, 50))
        bot_builder.save("my_bot.jpeg")
        print "Now it's time to select a head."
        bot_head()
    elif robot_body == "buttons":
        buttons = Image.open(
            '/Users/alicen/git/robots/bot_parts/body_buttons.jpg')
        bot_builder.paste(buttons, (50, 50))
        bot_builder.save("my_bot.jpeg")
        print "Now it's time to select a head."
        bot_head()
    elif robot_body == "screen":
        screen = Image.open(
            '/Users/alicen/git/robots/bot_parts/body_screen.jpg')
        bot_builder.paste(screen, (50, 50))
        bot_builder.save("my_bot.jpeg")
        print "Now it's time to select a head."
        bot_head()
    else:
        print "That is not an option, please try again."
        # bot_body()
        exit(0)


def bot_head():
    add_head = Image.open('/Users/alicen/git/robots/my_bot.jpeg')
    print "The options are as follows:"
    print "Dome, square, round, or tube"
    head_input = raw_input("select one: ")
    robot_head = head_input.lower()

    if robot_head == "dome":
        dome = Image.open('/Users/alicen/git/robots/bot_parts/head_dome.jpg')
        add_head.paste(dome, (50, 0))
        add_head.save("my_bot.jpeg")
        bot_arms()
    elif robot_head == "square":
        square = Image.open(
            '/Users/alicen/git/robots/bot_parts/head_square.jpg')
        add_head.paste(square, (50, 0))
        add_head.save("my_bot.jpeg")
        bot_arms()
    elif robot_head == "round":
        round = Image.open('/Users/alicen/git/robots/bot_parts/head_round.jpg')
        add_head.paste(round, (50, 0))
        add_head.save("my_bot.jpeg")
        bot_arms()
    elif robot_head == "tube":
        tube = Image.open('/Users/alicen/git/robots/bot_parts/head_tube.jpg')
        add_head.paste(tube, (50, 0))
        add_head.save("my_bot.jpeg")
        bot_arms()
    else:
        print "That is not an option, please try again."
        bot_head()


def bot_arms():
    print "Does your robot fight or help?"
    use_input = raw_input("select one: ")
    robot_arms = Image.open('/Users/alicen/git/robots/my_bot.jpeg')
    robot_use = use_input.lower()

    if robot_use == "fight":
        print "What weapon does your bot use?"
        weapon_input = raw_input("Gun, knife, chainsaw, mace, or lasers: ")
        weapon = weapon_input.lower()

        if weapon == "gun":
            gun = Image.open(
                '/Users/alicen/git/robots/bot_parts/weapon_gun.jpg')
            gun_left = Image.open(
                '/Users/alicen/git/robots/bot_parts/weapon_gun_left.jpg')
            robot_arms.paste(gun, (0, 0))
            robot_arms.paste(gun_left, (100, 0))
            robot_arms.save("my_bot.jpeg")
            bot_legs()
        elif weapon == "knife":
            knife = Image.open(
                '/Users/alicen/git/robots/bot_parts/weapon_knife.jpg')
            robot_arms.paste(knife, (0, 0))
            robot_arms.save("my_bot.jpeg")
            bot_legs()
        elif weapon == "chainsaw":
            chainsaw = Image.open(
                '/Users/alicen/git/robots/bot_parts/weapon_chainsaw.jpg')
            chainsaw_left = Image.open(
                '/Users/alicen/git/robots/bot_parts/weapon_chainsaw_left.jpg')
            robot_arms.paste(chainsaw, (0, 0))
            robot_arms.paste(chainsaw_left, (100, 0))
            robot_arms.save("my_bot.jpeg")
            bot_legs()
        elif weapon == "mace":
            mace = Image.open(
                '/Users/alicen/git/robots/bot_parts/weapon_mace.jpg')
            robot_arms.paste(mace, (0, 0))
            robot_arms.save("my_bot.jpeg")
            bot_legs()
        elif weapon == "lasers":
            lasers = Image.open(
                '/Users/alicen/git/robots/bot_parts/weapon_lasers.jpg')
            robot_arms.paste(lasers, (0, 0))
            robot_arms.save("mybot.jpeg")
            bot_legs()
        else:
            print "That is not an option, please try again."
            bot_arms()
    elif robot_use == "help":
        print "How does your robot help?"
        help_input = raw_input("Disastor relief, medicine, or protection: ")
        bot_help = help_input.lower()
        if bot_help == "disastor relief":
            disastor = Image.open(
                '/Users/alicen/git/robots/bot_parts/help_disastor.jpg')
            robot_arms.paste(disastor, (0, 0))
            robot_arms.save("my_bot.jpeg")
            bot_legs()
        elif bot_help == "medicine":
            medic = Image.open(
                '/Users/alicen/git/robots/bot_parts/weapon_medicine.jpg')
            robot_arms.paste(medic, (0, 0))
            robot_arms.save("my_bot.jpeg")
            bot_legs()
        elif bot_help == "protection":
            protect = Image.open(
                '/Users/alicen/git/robots/bot_parts/weapon_protection.jpg')
            robot_arms.paste(protect, (0, 0))
            robot_arms.save("my_bot.jpeg")
            bot_legs()
        else:
            print "That is not an option, please try again."
            bot_arms()
    else:
        print "That is not an option, please try again."
        bot_arms()


def bot_legs():
    print "How does your robot get around?"
    move = raw_input("Wheels, tank treads, floating, or legs: ")
    legs_input = Image.open('/Users/alicen/git/robots/my_bot.jpeg')
    bot_legs = legs_input.lower()

    if move == "wheels":
        wheels = Image.open(
            '/Users/alicen/git/robots/bot_parts/legs_wheels.jpg')
        bot_legs.paste(wheels, (50, 100))
        bot_legs.save("my_bot.jpeg")
    elif move == "tank treads":
        tank = Image.open('/Users/alicen/git/robots/bot_parts/legs_tank.jpg')
        bot_legs.paste(tank, (50, 100))
        bot_legs.save("my_bot.jpeg")
    elif move == "floating":
        floating = Image.open('/Users/alicen/git/robots/bot_parts/legs_float.jpg')
        bot_legs.paste(floating, (50, 100))
        bot_legs.save("my_bot.jpeg")
    elif move == "legs":
        legs = Image.open('/Users/alicen/git/robots/bot_parts/legs_legs.jpg')
        bot_legs.paste(legs, (50, 100))
        bot_legs.save("my_bot.jpeg")
    else:
        print "That is not an option, please try again."
        bot_legs()


def show_bot():
    print "You have finished building your bot."
    print "Would you like to see it?"
    show_input = raw_input("yes or no: ")
    display_bot = show_input.lower()
    final_bot = Image.open('/Users/alicen/git/robots/my_bot.jpeg')

    if display_bot == "yes":
        final_bot.show()
        final_confirmation()
    elif display_bot == "no":
        print "Would you like to start over?"
        restart_input = raw_input("yes or no: ")
        restart_choice = restart_input.lower()

        if restart_choice == "yes":
            bot_body()
        elif restart_choice == "no":
            final_confirmation()
        else:
            print "That is not an option, please try again."
            show_bot()
    else:
        print "That is not an option, please try again."
        show_bot()


def final_confirmation():
    print "Are you happy with your robot?"
    conf_input = raw_input("yes or no?: ")
    confirmation = conf_input.lower()

    if confirmation == "yes":
        # exit to main game thing or stat builder?
        pass
    elif confirmation == "no":
        print "Okay, you can start over."
        bot_body()
    else:
        print "That is not an option, please try again."
        final_confirmation()


bot_body()
