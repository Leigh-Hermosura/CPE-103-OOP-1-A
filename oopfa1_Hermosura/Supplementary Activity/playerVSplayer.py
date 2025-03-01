import time
import random
from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician


def choose_class(player_name):
    while True:
        try:
            player_class = int(input(f"""{player_name}, please choose a class:
- Swordsman (type 1)
- Archer (type 2)
- Magician (type 3)

> """))
            if player_class == 1:
                return Swordsman(player_name)
            elif player_class == 2:
                return Archer(player_name)
            elif player_class == 3:
                return Magician(player_name)
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")


def start_battlePVP(player1, player2):
    while player1.getHp() > 0 and player2.getHp() > 0:
        print(f"\n{player1.getUsername()} HP: {player1.getHp()} -----|VERSUS|----- "
              f"{player2.getUsername()} HP: {player2.getHp()}")

        # Randomized chance of which of the two players will attack first
        goFirst, goSecond = (player1, player2) if random.choice([True, False]) else (player2, player1)
        print(f"{goFirst.getUsername()} goes first")
        action = choose_action(goFirst, goSecond)
        execute_action(goFirst, action, goSecond)

        if goSecond.getHp() > 0:
            action = choose_action(goSecond, goFirst)
            execute_action(goSecond, action, goFirst)

        # Check if the game is over
        if player1.getHp() <= 0 or player2.getHp() <= 0:
            break

    # Announce the winner and ask if the players want to continue
    if player1.getHp() <= 0:
        print(f"{player1.getUsername()} has been defeated! {player2.getUsername()} wins!")
    else:
        print(f"{player2.getUsername()} has been defeated! {player1.getUsername()} wins!")

    time.sleep(1)
    contBattle = input("Continue (type Y), start a new game (type N), or quit (type Q)? ")
    if contBattle.lower() == "q":
        print("Game Over!")
        return
    elif contBattle.lower() == "n":
        print("Starting a new game...")
        new_match()
        return

    player1.resetHp()
    player2.resetHp()

    # Starting a new match
    print("Starting a new match...")
    time.sleep(1)
    for num in [3, 2, 1]:
        time.sleep(1)
        print(num)
    time.sleep(1)
    print(("-" * 20) + "<GAME START>" + ("-" * 20))

    start_battlePVP(player1, player2)


def choose_action(player, opponent):
    while True:
        try:
            if isinstance(player, Swordsman):
                action = int(input(f"""- Use Slash Attack on {opponent.getUsername()} (type 1) 
> """))
            elif isinstance(player, Archer):
                action = int(input(f"""- Use Ranged Attack on {opponent.getUsername()} (type 1) 
> """))
            elif isinstance(player, Magician):
                action = int(input(f"""- Use Magic Attack on {opponent.getUsername()} (type 1) 
- Use Heal on yourself (type 2)
> """))
            else:
                action = 0
            if action in [1, 2] or (action == 1 and not isinstance(player, Magician)):
                return action
            else:
                print("Invalid action.")
        except ValueError:
            print("Invalid input.")


def execute_action(player, action, opponent):
    if action == 1:
        if isinstance(player, Swordsman):
            player.slashAttack(opponent)
        elif isinstance(player, Archer):
            player.rangedAttack(opponent)
        elif isinstance(player, Magician):
            player.magicAttack(opponent)
    elif action == 2 and isinstance(player, Magician):
        player.heal()
    else:
        print("Please enter a valid number.")


def new_match():
    playerName1 = input("Please enter the name of Player 1: ")
    player1 = choose_class(playerName1)

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
