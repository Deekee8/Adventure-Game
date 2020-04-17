import time
import random

creatures_list = ["grasshopper", "emu", "tarantula", "kangaroo"]
creature = random.choice(creatures_list)

def main():
    intro()
    escape_dungeon(creature)

def print_pause():
    print(message)
    time.sleep(4)

def intro():
    print_pause("You awake to find yourself in a dark dungeon with "
                "nothing but the jeans and t-shirt that you're "
                "wearing.")
    print_pause("As your vision comes into focus, you see a damp "
                "sewer tunnel across the room.")
    print_pause("You can see a faint light coming from the other end.")
    print_pause("You start toward the tunnel, when you hear your "
                "son crying overhead.")
    print_pause("You look to your right and see a ladder leading up "
                "to an opening.")
    print_pause("What do you do?\n")

def replay():
    play_again = input("Would you like to play again?\n"
                       "Please type 'yes' or 'no'.").lower()
    if play_again == "yes":
        main()
    elif play_again == "no":
        print_pause("Thank you for playing.")
    else:
        print_pause("I'm not clear what you'd like to do.")
        replay()

def input_error():
    print_pause("That is not an option. Please enter 'A' or 'B'.")

def fight_or_flee():
    f_or_f = input("Do you:\nA. Try to fight the {creature}\nB. Flee back "
                    "down to the dungeon\n(Enter A or B)").lower()
    if f_or_f == "a":
        print_pause("You are no match for the giant ninja {creature}.")
        print_pause("It easily overpowers and defeats you.")
        print_pause("GAME OVER!")
        replay()
    elif f_or_f == "b":
        print_pause("You make it back to the hole in the groung and "
                    "down the ladder before the {creature} can get you")
        print_pause("Luckily the {creature} is too large to fit down "
                    "the hole.")
        print_pause("However, you need to rescue your son but need to "
                    "find a weapon to defeat the giant ninja {creature}")
        print_pause("What do you do next?")
        escape_dungeon()
    else:
        input_error()
        fight_or_flee()

def go_home():
    print_pause("You make it home, but your spouse is so "
                "upset that you abandoned your son, that "
                "they take you out with their bare hands.")
    print_pause("GAME OVER")
    replay()

def leave_or_search():
    l_or_s = input("Do you:\nA. Try to find your way home and hope "
                   "that your son will be okay?\nor\nB. Search "
                   "through the dumpster to see what's causing "
                   "the glow?\n(Enter 'A' or'B')\n").lower()
    if l_or_s == "a":
        go_home()
    elif l_or_s == "b":
        print_pause("You dig through the muck in the dumpster "
                    "until you fing a glowing green ninja star!")
        print_pause("What do you do next?")
        stay_or_go = input("Do you:\nA. Take you new toy and head "
                            "home?\nor\nB. Head toward the roll-up "
                            "door where you heard the screams of you son?\n").lower()
        if stay_or_go == 'a':
            go_home()
        elif stay_or_go == 'b':
            print_pause("As you approach the roll-up door, it flies "
                        "open and the giant ninja {creature} rushes "
                        "toward you.")
            print_pause("This time, you're prepared!")   
            print_pause("You throw the glowng green ninja star at the "
                        "{creature} and hit it right between the eyes.")
            print_pause("It lets out the loudest screech you've ever heard, "
                        "and vanishes in a burst of white light.")
            print_pause("You rush over to your son, untie him, and hug him tight.")
            print_pause("He thanks you and tells you that he admires your bravery.")
            print_pause("You assure him that you will always have is back.")
            print_pause("The two of you head home and tell your spouse of the "
                        "fantastic events of the day.")
            print_pause("Your spouse is impressed and showers you with affection!")
            print_pause("You are the hero of your family forevermore!")
            print_pause("YOU WIN!")
            replay()
        else:
            replay()
    else:
        input_error()
        leave_or_search()

def escape_dungeon():
    escape = input("Do you:\nA. Take the ladder up to find "
                   "your son?\nor\nB. Continue down the tunnel "
                   "to find a way out?\n(Enter A or B)\n").lower()
    if escape == "a":
        print_pause("You climb up the ladder and push aside the "
                    "heavy wooden plank that is covering "
                    "the opening.")
        print_pause("You're now standing in a big empty warehouse.")
        print_pause("You see your son tied to a chair near a "
                    "roll-up door on the opposite wall.")
        print_pause("You sprint over to save him, when a giant "
                    "ninja {creature} suddenly appears to stop you.")
        print_pause("You don't have any weapons or fighting skills")
        print_pause("What do you do next?")
        fight_or_flee()
    elif escape == "b":
        print_pause("You head down the damp tunnel until you "
                    "reach a ladder leading up to a sewage grate.")
        print_pause("You climb out of the sewer into a dark alley "
                    "in an abandoned industrial complex.")
        print_pause("It looks like you're free from danger, but "
                    "you know your son is inside one of these buildings.")
        print_pause("You suddenly hear him screaming for you from behind "
                    "the roll-up door to a building to your left.")
        print_pause("Next to the roll up door is a dumpster that's filled "
                    "with gross garbage, but there is also a bright green "
                    "glow coming from inside that dumpster.")
        print_pause("You know that your son is being held captive "
                    "behind that door, but you also know that you "
                    "don't have the fighting skills to defeat the giant "
                    "ninja {creature}.")
        print_pause("What do you do next?")
        leave_or_search()
    else:
        input_error()
        escape_dungeon()
