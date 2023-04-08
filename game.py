import time

def play_game(player1, player2):
    """Simulate a battle between two players until one of them loses 30 units."""
    start_time = time.time()
    while player1.units_lost < 30 and player2.units_lost < 30:
        for unit1, unit2 in zip(player1.units, player2.units):
            initial_health_unit2 = unit2.health
            unit1.attack_enemy(unit2)
            if not unit2.is_alive() and initial_health_unit2 > 0:
                player1.earn_gold(5)
                player2.units_lost += 1

            initial_health_unit1 = unit1.health
            unit2.attack_enemy(unit1)
            if not unit1.is_alive() and initial_health_unit1 > 0:
                player2.earn_gold(5)
                player1.units_lost += 1

        elapsed_time = time.time() - start_time
        if elapsed_time // 5 > 0:
            player1.earn_gold(5 * int(elapsed_time // 5))
            player2.earn_gold(5 * int(elapsed_time // 5))
            start_time = time.time()

    winner = player1 if player1.units_lost < 30 else player2
    print(f"{winner.name} a gagné la partie!")
