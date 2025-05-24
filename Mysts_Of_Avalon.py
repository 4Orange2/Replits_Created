from time import *


def atForestEdge():  #Procedure definition
    print()
    print("You're at the edge of a spooky forest. What would you like to do? ")
    choice = input(
        "(a) Go into the forest immediately, (b) Camp here and wait until morning,  (c) Go back to the door "
    )

    if choice == "a":
        insideForest()  #Procedure-call

    elif choice == "b":
        waitUntilMorning()  #Procedure-call

    elif choice == "c":
        atDoor()  #Procedure-call

    else:
        print("Typing a non-option is fatal.")
        print("You died")
        wantToRestart()  #Procedure-call


def jumpForJoy():
    print()
    print("Jumping in trees is a bad idea. You fell out of the tree.")
    print("And died.")
    wantToRestart()


def openDoor():
    print()
    print("The sign was right.")
    print("A dragon leaped out and ate you.  You died.")
    wantToRestart()


def atDoor():
    print()
    print(
        "You're at a door with a high wall. The door says Beware of Dragon.  What would you like to do?"
    )
    choice = input(
        "(a) Open the door and look for treasure.    (b) Go to the forest instead  "
    )

    if choice == "a":
        openDoor()

    elif choice == "b":
        atForestEdge()

    else:
        print("Picking a non-option is fatal.  You died")
        wantToRestart()


def waitUntilMorning():
    print()
    print("A pack of wolves finds you while you are sleeping.")
    sleep(1)
    print("They ransack your tent.  They take your wallet and your phone.")
    print(
        "Deprived of social media for 20 consecutive minutes, you die of loneliness."
    )
    wantToRestart()


def insideForest():
    print()
    print("You see an axe stuck in a tree. What would you like to do? ")
    choice = input(
        "(a) Pull the axe out of the tree, (b) Climb the tree, (c) Go back to the edge of the forest "
    )

    if choice == "a":
        pullAxe()

    elif choice == "b":
        climbTree()

    elif choice == "c":
        atForestEdge()

    else:
        print("Picking a non-option is fatal.  You died.")
        wantToRestart()


def pullAxe():
    print()
    print(
        "The axe was magic!  And it is angry at being disturbed!  It leaps from your hands and chops down the tree."
    )
    print("Which falls on you.")
    print("You died.")
    wantToRestart()


def climbTree():
    print()
    print(
        "You find a bag of gold in the branches!  It's enough to pay for university.  You are set for life!"
    )
    print("What would you like to do? ")
    choice = input("(a) Jump for joy!  (b) Climb back down:  ")

    if choice == "a":
        jumpForJoy()

    elif choice == "b":
        climbDown()

    else:
        print("Picking a non-option is fatal.  You died.")
        wantToRestart()


def climbDown():
    print()
    print(
        "You take your gold back home and pay for university, where you get a CS degree and save the world from climate change."
    )
    print("You live happily ever after...")
    sleep(2)
    print("...and then die of old age.")
    sleep(1)
    youWin()


def youWin():
    print("@~" * 30 + "\n")
    print("CONGRATULATIONS ON WINNING THE GAME!")
    print("@~" * 30 + "\n")


def wantToRestart():
    playAgain = input("\nDo you want to start over? (y/n): ")

    if playAgain in ["y", "Y", "yes", "YES", "Yes"]:
        startGame()

    else:
        print("Bye")


def startGame():  #Procedure.  A procedure is a new command that we teach Python.
    print()
    print("@~" * 18 + "\n")
    print("Welcome to THE MYSTS OF AVALON 2.0\n")
    print("@~" * 18 + "\n")
    atDoor()


startGame()  #The procedure-call that actually starts the game