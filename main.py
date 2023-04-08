from unit import Unit
from player import Player
from game import play_game

class FireElemental(Unit):
    def __init__(self):
        super().__init__(health=60, attack=30, defense=10, cost=10)

class WaterElemental(Unit):
    def __init__(self):
        super().__init__(health=80, attack=20, defense=15, cost=10)

class AirElemental(Unit):
    def __init__(self):
        super().__init__(health=50, attack=25, defense=5, cost=10)

class EarthElemental(Unit):
    def __init__(self):
        super().__init__(health=100, attack=15, defense=20, cost=10)

if __name__ == "__main__":
    units_p1 = []
    units_p2 = []

    player1 = Player("Joueur 1", units_p1, 50)
    player2 = Player("Joueur 2", units_p2, 50)

    player1.recruit_unit(FireElemental())
    player2.recruit_unit(WaterElemental())
    player1.recruit_unit(AirElemental())
    player2.recruit_unit(EarthElemental())

    play_game(player1, player2)
