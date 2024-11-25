import random
import time
import sys


def PrintSleep(msg, t):
    print(msg)
    time.sleep(t)


def combat(weapon):
    PrintSleep(f"The {enemy} attacks you!", 2)
    if weapon == "dagger":
        PrintSleep(f"You are under-prepared what only havig a{weapon}?", 2)
    while True:
        choice = input("Would you like to (1) fight or (2) run away?"
                       "(Please Enter the number (1) or (2))")
        if choice == '1':
            if weapon == 'dagger':
                PrintSleep(f"You do your best...", 1)
                PrintSleep(f"The {weapon} is no match for the{enemy}.", 2)
                PrintSleep(f"You have been defeated!""", 2)
            elif weapon == "Sword":
                PrintSleep(f"As the {enemy} moves to the attack,"
                           "you unsheath your new sword.", 2)
                PrintSleep(f"The sword of Ogoroth brightly in"
                           " your hand as you brace yourself", 2)
                PrintSleep(f"But the {enemy} takes one look at"
                           " your shiny new toy and runs away!", 3)
                PrintSleep(f"You have rid the town of the{enemy}.You"
                           "are victorious!", 3)
            break
        elif choice == '2':
            PrintSleep("You run back into the field."
                       "Luclily, you don't seem to have been followed.", 3)
            where_to()
            break
        else:
            PrintSleep("Invalid choice. Please enter"
                       "1 to fight or 2 to run away.", 2)


def PlayAgain():
    choice = ''
    while choice not in ['y', 'n']:
        choice = input("Would you like to play again? (y/n)")
        if choice == 'n':
            PrintSleep('Thanks for playing! See you next time.', 2)
            sys.exit(0)
        elif choice == 'y':
            PrintSleep("Excellent! Restarting the game...",  2)
            weapon = 'dagger'
            return 'running'


def intro():
    PrintSleep("You find yourself standing in an open filled,"
               "filled with grass and yellow wildflowers", 3)
    PrintSleep(f"Rumor has it that a {enemy} is somewhere around here,"
               "and has been terrifying the nearby village", 2)
    PrintSleep(f"In your hand you hold your trusty {weapon}.", 1)
    PrintSleep("Here the journey begins!!!", 1)


def where_to():
    PrintSleep("", 2)
    PrintSleep("And you walked until reached another place", 2)
    PrintSleep("In front of you is a house .", 1)
    PrintSleep("To your right is a dark cave.", 1)
    PrintSleep("Enter 1 to knock on the door of the house.", 2)
    PrintSleep("Enter 2 to peer into cave.", 2)
    PrintSleep("what would you like to do?", 0)
    choice = ''
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")

    if choice == '1':
        house()

    elif choice == '2':
        cave()


def house():
    PrintSleep("You approach the door of the house and knock it.", 2)
    PrintSleep(f"Eep! This is the {enemy}'s house!", 2)
    combat(weapon)


def cave():
    global cave_visited
    global weapon
    PrintSleep("You peer cautiously into the cave.", 3)
    if cave_visited:
        PrintSleep("You've been here brfor, and gotten all the "
                   "good stuff. It's just an empty cave.", 3)
    elif cave_visited is False:
        PrintSleep("It turns out to be only a very small cave.", 2)
        PrintSleep("Your eye catches a glint of metal dehind a rock.", 2)
        PrintSleep("You have found the magical Sword of Ogoroth!", 2)
        PrintSleep(f"You discard your silly old "
                   "{weapon} and take the sword with you.", 2)
        weapon = "Sword"
    cave_visited = True
    PrintSleep("You walk back out to the field.", 2)
    where_to()


def Inquiry():
    PrintSleep("A local resident approaches you in "
               "the field, seeking your assistance.", 2)
    PrintSleep("You are tasked with locating a missing"
               "family heirloom within the Castle.", 2)
    PrintSleep("Enter 1 to help the family.", 1)
    PrintSleep("Enter 2 to say sorry ", 2)
    PrintSleep("what would you like to do?", 0)
    choice = ''
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")

    if choice == '1':
        Castle()

    elif choice == '2':
        PrintSleep("I'm sorry I can't help . ", 2)


def Castle():
    PrintSleep("You draw near to a majestic, timeworn"
               "castle encircled by a vast moat.", 2)
    PrintSleep("The drawbridge is down, and the massive"
               "wooden doors are slightly ajar.", 2)
    PrintSleep("You enter with caution and discover yourself in"
               "an expansive hall, softly illuminated by dim lighting.", 2)
    choice = ''

    while choice not in ['1', '2']:
        PrintSleep("Inside the castle, you see two paths ahead:", 2)
        PrintSleep("1. A staircase leading up to a mysterious tower.", 2)
        PrintSleep("2. A doorway leading to what"
                   "looks like a treasure room.", 2)
        choice = input("Which path do you choose? (1 or 2)\n")
    if choice == '1':
        tower()
    else:
        riddle_with_random()


def riddle_with_random():
    PrintSleep("A voice echoes: 'Solve the riddle of"
               "numbers to proceed And to have a friend!'", 2)
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operation = random.choice(["+", "-", "*"])
    if operation == "+":
        correct_answer = num1 + num2
    elif operation == "-":
        correct_answer = num1 - num2
    elif operation == "*":
        correct_answer = num1 * num2
    PrintSleep(f"The voice asks: What is {num1} {operation} {num2}?", 2)
    attempts = 3
    while attempts > 0:
        player_answer = int(input("Your answer: "))
        if player_answer == correct_answer:
            PrintSleep("It's better, you've passed it, and here's"
                       "a little fairy who's your friend", 3)
            attempts = 0
            mysterious_room()
            break
        else:
            attempts -= 1
            if attempts > 0:
                PrintSleep(f"Incorrect!You have {attempts} attempts"
                           "remaining.", 2)
            else:
                PrintSleep("Fire comes out from everywhere and kills you.", 3)


def tower():
    PrintSleep("You walk up the winding stairs, feeling the"
               "air getting colder with every step and the"
               "sounds of owls and spider webs everywhere..", 3)
    PrintSleep("At the top, an ancient guardian protects"
               "an ancient pin-deh cube, emitting a golden"
               "glow and a beautiful sound.", 3)
    PrintSleep("The guardian stares at you and challenges you"
               "to a riddle and He will become his friend and help him.", 3)
    answer = input("The guardian asks: 'What has keys"
                   "but can't open locks?' \nYour answer: ").lower()
    if answer == 'piano':
        PrintSleep("The guardian nods in approval"
                   "and hands you the magical cube.", 3)
        PrintSleep("You now have the magical cube in your inventory!", 3)
        PrintSleep("He opened the box and moved it to the place of the"
                   "family heirloom, With a new"
                   "friend, a little fairy, to help him", 3)
        mysterious_room()
    else:
        PrintSleep("The guardian shakes its head"
                   "and banishes you from the tower.", 3)
        PrintSleep("You stumble back into the field,"
                   "feeling defeated, and go back", 3)


def mysterious_room():
    PrintSleep("You step into the treasure room, and your"
               "eyes widen at the sight of glittering gold and jewels.", 3)
    PrintSleep("As you reach for the treasure, a trap is triggered!", 3)
    choice = ''
    while choice not in ['1', '2']:
        PrintSleep("You see two options to escape:", 2)
        PrintSleep("1.Ask the little fairy to lift"
                   "the handle to get out of the trap.", 2)
        PrintSleep(f"2. Use your {weapon} to break"
                   "through the trap mechanism.", 2)
        choice = input("What will you do? (1 or 2)\n")
    if choice == '1':
        PrintSleep("The fairy turns the handle and her friends"
                   "leave And here you have found the treasure"
                   "and solved the puzzle!!!", 3)
        Back_to_family()
    elif choice == '2':
        if weapon == "Sword":
            PrintSleep("You use your powerful sword to disable"
                       "the trap and escape safely with some treasure!", 3)
            Back_to_family()
        else:
            PrintSleep("Your dagger isn't strong enough, and"
                       "you barely escape with your life.", 3)


def Back_to_family():
    PrintSleep("Tells the family the location"
               "of the treasure and how to reach it", 2)
    PrintSleep("Directs them to the fund protector to help them", 2)
    game_state = PlayAgain()


game_state = 'running'


while game_state == 'running':
    enemies = ['troll', 'wicked fairie', 'pirate', 'gorgon', 'dragon']
    enemy = random.choice(enemies)
    weapon = 'dagger'
    cave_visited = False

    intro()
    random_number = random.choice([1, 2])
    if random_number == 1:
        random_weapon = random.choice(['dagger', 'Sword'])
        Inquiry()
    else:
        where_to()
    game_state = PlayAgain()
