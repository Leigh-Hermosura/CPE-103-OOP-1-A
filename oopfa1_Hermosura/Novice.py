import random
from Character import Character


class Novice(Character):
    def basicAttack(self, character):
        if random.random() < 0.35:
            character.reduceHp(self.getCritDmg())
            print(f"{self.getUsername()} performed Basic Attack! CRITICAL🔥 -{self.getCritDmg()}")
        else:
            character.reduceHp(self.getDamage())
            print(f"{self.getUsername()} performed Basic Attack! -{self.getDamage()}")
    pass

# character1 = Novice("Your Username")
# print(character1.getUsername())
# print(character1.getHp())
