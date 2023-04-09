import time
from player import Player

class Unit:
    def __init__(self, player, health, attack, cost):
        self.player = player
        self.health = health
        self.attack = attack
        self.cost = cost

    def is_alive(self):
        """Return True if the unit is alive, otherwise False."""
        return self.health > 0

    def get_damage_multiplier(self, attacker):
        """Return the damage multiplier based on the attacker's type."""
        return 1

    def take_damage(self, damage, attacker):
        """Reduce the unit's health by the amount of damage, considering damage multiplier."""
        multiplier = self.get_damage_multiplier(attacker)
        self.health -= max(0, damage * multiplier)

class Elemental(Unit):
    @classmethod
    def get_cost(cls):
        return cls.cost

class FireElemental(Elemental):
    cost = 10

    def __init__(self, player):
        super().__init__(player, 50, 10, 2)

    def get_damage_multiplier(self, attacker):
        if isinstance(attacker, AirElemental):
            return 0.5
        elif isinstance(attacker, WaterElemental):
            return 2
        return 1

class WaterElemental(Elemental):
    cost = 10

    def __init__(self, player):
        super().__init__(player, 40, 8, 3)

    def get_damage_multiplier(self, attacker):
        if isinstance(attacker, FireElemental):
            return 0.5
        elif isinstance(attacker, EarthElemental):
            return 2
        return 1

class AirElemental(Elemental):
    cost = 10

    def __init__(self, player):
        super().__init__(player, 30, 12, 4)

    def get_damage_multiplier(self, attacker):
        if isinstance(attacker, EarthElemental):
            return 0.5
        elif isinstance(attacker, FireElemental):
            return 2
        return 1

class EarthElemental(Elemental):
    cost = 10

    def __init__(self, player):
        super().__init__(player, 60, 6, 1)

    def get_damage_multiplier(self, attacker):
        if isinstance(attacker, WaterElemental):
            return 2
        elif isinstance(attacker, AirElemental):
            return 0.5
        return 1
