# Create a new file Game.py inside the same folder use the pre-made classes to create a simple Game where two players or
# one player vs a computer will be able to reduce their opponent’s hp to 0.

import time
from singlePlayer import start_battleSP
from playerVSplayer import choose_class, start_battlePVP

print("Welcome to PyBattle!")

# selecting two game modes
time.sleep(1)
gameMode = int(input("""
Select a Game Mode:
> Single Player (type 1)
> Player vs Player (type 2)

> """))

# Code for Player vs Player mode
if gameMode == 2:
    # Player 1
    print("\nPlayer vs Player chosen!")
    playerName1 = input("Please enter the name of Player 1: ")
    player1 = choose_class(playerName1)

    # Player 2
    playerName2 = input("Please enter the name of Player 2: ")
    player2 = choose_class(playerName2)

    print("\nGet yourselves ready for a fight!")
    time.sleep(1)
    print("\nThe watch will start in")
    time.sleep(1)
    for number in [3, 2, 1]:
        time.sleep(1)
        print(number)
    time.sleep(1)
    print(("-" * 20) + "<GAME START>" + ("-" * 20))

    start_battlePVP(player1, player2)

# Code for Single Player mode
elif gameMode == 1:
    print("\nSingle Player chosen!")
    playerName1 = input("Please enter your name: ")
    time.sleep(1)
    input(f"You, {playerName1}, will start as a Novice adventurer (press Enter to continue).")
    input("You will have to face against monsters and rank up (press Enter to continue).")
    input("Win 2 matches and you will be able to choose a class! (press Enter to continue).")

    start_battleSP(playerName1)
