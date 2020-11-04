import time
import random

creatures_list = ["grasshopper", "emu", "tarantula", "kangaroo"]
creature = random.choice(creatures_list)

items = []


def print_pause(message):
    print(message)
    time.sleep(4)


def intro(creature):
    print_pause("You awake to find yourself in a dark dungeon, with "
                "nothing but the\njeans and t-shirt that you're "
                "wearing.\n")
    print_pause("Your memory is fuzzy but you vaguely recall "
                f"being captured by\na giant ninja {creature} right "
                "before you passed out.\n")
    print_pause("As your vision comes into focus, you see a damp "
                "sewer tunnel across the room.\n")
    print_pause("You can see a dim light coming from the other end.\n")
    print_pause("You start toward the tunnel, when you faintly hear your "
                "son crying overhead.\n")
    print_pause("You look to your right and see a ladder that leads up "
                "to an opening.\n")
    print_pause("What do you do?\n")


def replay():
    play_again = input("Would you like to play again?\n"
                       "Please type 'yes' or 'no'.\n").lower()
    if play_again == "yes":
        print_pause("Excellent! Back into the dungeon you go...\n")
        main_gameplay()
    elif play_again == "no":
        print_pause("Thank you for playing.")
    else:
        print_pause("I'm not clear what you'd like to do.\n")
        replay()


def input_error():
    print("I don't recogize that choice.\n")


def fight_or_flee(creature, items):
    f_or_f = input(f"A. Try to fight the {creature}\nB. Flee back "
                   "down to the dungeon\n(Enter A or B)\n").lower()
    if f_or_f == "a":
        print_pause("You decide to put up a fight for your son.\n")
        print_pause(f"You are no match for the giant ninja {creature}.\n")
        print_pause("It easily overpowers and defeats you.\n")
        print_pause("GAME OVER!\n")
        replay()
    elif f_or_f == "b":
        items.append("ladder")
        print_pause("You smartly avoid this confrontation becuse you know "
                    "that you're\nill-equipped to defeat this beast.\n")
        print_pause("You make it back to the hole in the groung and "
                    f"down the ladder\nbefore the {creature} can get you\n")
        print_pause(f"Luckily the {creature} is too large to fit down "
                    "the hole.\n")
        print_pause("You need to rescue your son but must first "
                    "find a weapon\nto defeat the giant ninja "
                    f"{creature} with.\n")
        print_pause("What do you do next?\n")
        escape_dungeon(creature, items)
    else:
        input_error()
        fight_or_flee(creature, items)


def rescue_or_search(creature, items):
    r_or_s = input("A. Try to open the roll-up door\nB. Search "
                   "through the dumpster to see what's causing "
                   "the glow\n(Enter 'A' or'B')\n").lower()
    if r_or_s == "a":
        if "door" in items and "star" not in items:
            print_pause("You've already tried the door.\n")
            print_pause("You know that what lies on the other"
                        "side is\nan insurmountable obstacle for"
                        "you without a weapon.\n")
            print_pause("Your son needs you to think fast.\n")
            print_pause("What's your next move?\n")
            rescue_or_search(creature, items)
        items.append("door")
        print_pause("You begin to roll the door up and you see that the\n"
                    f"giant ninja {creature} is waiting to challenge you.\n")
        if "star" in items:
            print_pause("You've found the magic ninja star and you're\n"
                        "ready to face this evil creature!\n")
            print_pause(f"The giant ninja {creature} rushes toward you\n"
                        "but you're prepared!\n")
            print_pause("You throw the glowng green ninja star at the "
                        f"giant\nninja {creature} and hit it right "
                        "between the eyes.\n")
            print_pause("It lets out the loudest screech you've ever heard,\n"
                        "and vanishes in a burst of white light.\n")
            print_pause("You rush over to your son, untie him, and hug him "
                        "tight.\n")
            print_pause("He thanks you and tells you that he admires your "
                        "bravery.\n")
            print_pause("You assure him that you will always have is back.\n")
            print_pause("The two of you head home and tell your spouse of "
                        "the\nfantastic events of the day.\n")
            print_pause("Your spouse is impressed and showers you with "
                        "affection!\n")
            print_pause("You are the hero of your family forevermore!\n")
            print_pause("YOU WIN!\n")
            items.remove("door", "star", "ladder")
            replay()
        else:
            print_pause("It lunges toward you but you haven't found a \n"
                        "suitable weapon to fight with yet.\n")
            print_pause("You slam the door closed and ponder what to do "
                        "next.\n")
            rescue_or_search(creature, items)
    elif r_or_s == "b":
        if "star" in items:
            print_pause("It looks like some of the magic dust rubbed\n"
                        "off of your new ninja star.\n")
            print_pause("You already got the useful part.\n")
            print_pause("What's next?\n")
            rescue_or_search(creature, items)
        items.append("star")
        print_pause("You dig through the muck in the dumpster "
                    "until you find\na glowing green ninja star!\n")
        print_pause("Ever since you were a kid, you've always wanted "
                    "a ninja star!\n")
        print_pause("...and this one looks like it has magical powers!\n")
        print_pause("What do you do next?\n")
        rescue_or_search(creature, items)
    else:
        input_error()
        rescue_or_search(creature, items)


def escape_dungeon(creature, items):
    escape = input("A. Take the ladder up to find "
                   "your son\nB. Continue down the tunnel "
                   "to find a way out\n(Enter A or B)\n").lower()
    if escape == "a":
        if "ladder" in items:
            print_pause("You know that you don't have the tools "
                        f"to battle the giant ninja {creature}.\n")
            print_pause("You should find a way out of the dungeon.\n")
            print_pause("What would you like to do?\n")
            escape_dungeon(creature, items)
        print_pause("You climb up the ladder and push aside the "
                    "heavy wooden plank\nthat is covering "
                    "the opening.\n")
        print_pause("You're now standing in a big empty warehouse.\n")
        print_pause("You see your son tied to a chair near a "
                    "roll-up door on the opposite wall.\n")
        print_pause("You sprint over to save him, when a giant "
                    f"ninja {creature}\nsuddenly appears to stop you.\n")
        print_pause("You don't have any weapons or fighting skills.\n")
        print_pause("What do you do next?\n")
        fight_or_flee(creature, items)
    elif escape == "b":
        print_pause("You head down the damp tunnel until you "
                    "reach a ramp\nthat leads up to a sewage grate.\n")
        print_pause("You climb out of the sewer into a dark alley "
                    "in a\nquiet industrial complex.\n")
        print_pause("It looks like you're free from danger, but "
                    "you know your son\nis inside one of these buildings.\n")
        print_pause("You suddenly hear him screaming for you from behind "
                    "a\nroll-up door to the building to your left.\n")
        print_pause("Next to the roll up door is a dumpster that's filled "
                    "with gross garbage,\nbut there is also a bright green "
                    "glow coming from inside that dumpster.\n")
        print_pause("You know that your son is being held captive "
                    "behind that door,\nbut you also know that you "
                    "don't have the fighting skills to defeat the\ngiant "
                    f"ninja {creature}.\n")
        print_pause("What do you do next?\n")
        rescue_or_search(creature, items)
    else:
        input_error()
        escape_dungeon(creature, items)


def main_gameplay():
    intro(creature)
    escape_dungeon(creature, items)


main_gameplay()
