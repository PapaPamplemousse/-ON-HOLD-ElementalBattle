import pygame
from player import Player
from unit import FireElemental, WaterElemental, AirElemental, EarthElemental
from time import time

def recruit_units(player):
    print("Choose the unit you want to recruit:")
    print("1. Fire Elemental - Cost: 10 gold")
    print("2. Water Elemental - Cost: 10 gold")
    print("3. Air Elemental - Cost: 10 gold")
    print("4. Earth Elemental - Cost: 10 gold")
    choice = int(input("Enter the number corresponding to the unit: "))

    unit_classes = {
        1: FireElemental,
        2: WaterElemental,
        3: AirElemental,
        4: EarthElemental
    }

    unit_class = unit_classes.get(choice, None)
    if unit_class:
        player.recruit_unit(unit_class)
    else:
        print("Invalid choice. Please try again.")

def main():
    pygame.init()
    player1 = Player("Player 1", [], 50)
    player2 = Player("Player 2", [], 50)

    # Recruitment phase
    phase_end_time = time() + 60  # Recruitment phase lasts 60 seconds
    phase_end_time = time() + 60  # Recruitment phase lasts 60 seconds

    while time() < phase_end_time:
        print("\nRecruitment phase time remaining: {:.0f}s".format(phase_end_time - time()))

        print("\n{}:".format(player1.name))
        recruit_units(player1)

        print("\n{}:".format(player2.name))
        recruit_units(player2)

    # Rest of the game logic

if __name__ == "__main__":
    main()
