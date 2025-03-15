import time
import random
from Novice import Novice
from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
from Boss import Boss


def start_battleSP(playerName1):
    playerSP = Novice(playerName1)
    winCount = 0
    playerClassSP = None

    def battle_restart():
        nonlocal playerSP
        if playerClassSP is None:
            playerSP = Novice(playerName1)
        else:
            playerSP = playerClassSP(playerName1)

        enemy = Boss("Monster")
        print("\nStarting a new match...")
        time.sleep(1)
        for number in [3, 2, 1]:
            time.sleep(1)
            print(number)
        time.sleep(1)
        print("-" * 20 + "<GAME START>" + "-" * 20)

        return enemy

    while True:
        enemy = battle_restart()

        while playerSP.getHp() > 0 and enemy.getHp() > 0:
            print(f"\n{playerSP.getUsername()} HP: {playerSP.getHp()} -----|VERSUS|----- "
                  f"{enemy.getUsername()} HP: {enemy.getHp()}")

            if isinstance(playerSP, Swordsman):
                action = int(input("""- Use Slash Attack (type 1) 
> """))
            elif isinstance(playerSP, Archer):
                action = int(input("""- Use Ranged Attack (type 1) 
> """))
            elif isinstance(playerSP, Magician):
                action = int(input("""- Use Magic Attack (type 1) 
- Use Heal (type 2)
> """))
            else:
                action = int(input("""- Use Basic Attack (type 1)
> """))

            # Player action
            if action == 1:
                if isinstance(playerSP, Swordsman):
                    playerSP.slashAttack(enemy)
                elif isinstance(playerSP, Archer):
                    playerSP.rangedAttack(enemy)
                elif isinstance(playerSP, Magician):
                    playerSP.magicAttack(enemy)
                else:
                    playerSP.basicAttack(enemy)
            elif action == 2 and isinstance(playerSP, Magician):
                playerSP.heal()
            else:
                print("Invalid input.")

            # Check if enemy is defeated
            if enemy.getHp() <= 0:
                print(f"{enemy.getUsername()} has been defeated!")
                winCount += 1
                time.sleep(1)
                contBattle = input("Continue? Y/N: ").lower()
                if contBattle == "n":
                    print("Game Over!")
                    return
                break  # Exit inner loop to restart battle

            # Monster action randomizer
            enemyAction = random.choice(["basic", "slash", "ranged", "magic", "heal"])
            if enemyAction == "basic":
                enemy.bossBasicAttack(playerSP)
            elif enemyAction == "slash":
                enemy.slashAttack(playerSP)
            elif enemyAction == "ranged":
                enemy.rangedAttack(playerSP)
            elif enemyAction == "magic":
                enemy.magicAttack(playerSP)
            elif enemyAction == "heal":
                enemy.heal()

            # Check if player is defeated
            if playerSP.getHp() <= 0:
                print(f"{playerSP.getUsername()} has been defeated!")
                time.sleep(1)
                contBattle = input("Continue? Y/N: ").lower()
                if contBattle == "n":
                    print("Game Over!")
                    return
                break

        # New role selection after getting 2 wins
        if winCount == 2:
            input("\nCongratulations on winning 2 matches! (press Enter to continue).")
            print("Please choose a class:")
            classChoice = int(input("""1 - Swordsman
2 - Archer
3 - Magician

> """))

            if classChoice == 1:
                playerClassSP = Swordsman
                input("\nYou are now a Swordsman! (press Enter to continue).")
            elif classChoice == 2:
                playerClassSP = Archer
                input("\nYou are now an Archer! (press Enter to continue).")
            elif classChoice == 3:
                playerClassSP = Magician
                input("\nYou are now a Magician! (press Enter to continue).")
            else:
                print("Invalid choice. Restarting as Novice.")

            # Reset win count
            winCount = 0