def play_game(player1, player2):
    """Simulate a battle between two players until one of them has no units left."""
    while player1.has_units() and player2.has_units():
        for unit1, unit2 in zip(player1.units, player2.units):
            unit1.attack_enemy(unit2)
            unit2.attack_enemy(unit1)

    winner = player1 if player1.has_units() else player2
    print(f"{winner.name} a gagné la partie!")
