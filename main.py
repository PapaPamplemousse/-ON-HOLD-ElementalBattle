from unit import FireElemental, WaterElemental, AirElemental, EarthElemental
from player import Player
from game import play_game

def recruit_units(player):
    player.recruit_unit(FireElemental)
    player.recruit_unit(WaterElemental)
    player.recruit_unit(AirElemental)
    player.recruit_unit(EarthElemental)

if __name__ == "__main__":
    units_p1 = []
    units_p2 = []

    player1 = Player("Joueur 1", units_p1, 50)
    player2 = Player("Joueur 2", units_p2, 50)

    recruit_units(player1)
    recruit_units(player2)

    play_game(player1, player2)
