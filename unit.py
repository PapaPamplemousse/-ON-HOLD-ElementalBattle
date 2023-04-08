import time

class Unit:
    def __init__(self, health, attack, defense, cost):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.cost = cost

    def is_alive(self):
        """Return True if the unit is alive, otherwise False."""
        return self.health > 0

    def get_damage_multiplier(self, attacker):
        """Return the damage multiplier based on the attacker's type."""
        return 1

    def take_damage(self, damage, attacker):
        """Reduce the unit's health by the amount of damage, considering defense and damage multiplier."""
        multiplier = self.get_damage_multiplier(attacker)
        self.health -= max(0, (damage - self.defense) * multiplier)

    def attack_enemy(self, enemy):
        """Attack the enemy unit and cause damage."""
        if self.is_alive() and enemy.is_alive():
            enemy.take_damage(self.attack, self)

class FireElemental(Unit):
    def __init__(self):
        super().__init__(health=60, attack=30, defense=10, cost=10)

    def get_damage_multiplier(self, attacker):
        if isinstance(attacker, AirElemental):
            return 0.5
        elif isinstance(attacker, WaterElemental):
            return 2
        return 1
    @classmethod
    def get_cost(cls):
        return cls().cost

class WaterElemental(Unit):
    def __init__(self):
        super().__init__(health=80, attack=20, defense=15, cost=10)

    def get_damage_multiplier(self, attacker):
        if isinstance(attacker, FireElemental):
            return 0.5
        elif isinstance(attacker, EarthElemental):
            return 2
        return 1
    @classmethod
    def get_cost(cls):
        return cls().cost

class AirElemental(Unit):
    def __init__(self):
        super().__init__(health=50, attack=25, defense=5, cost=10)

    def get_damage_multiplier(self, attacker):
        if isinstance(attacker, EarthElemental):
            return 0.5
        elif isinstance(attacker, FireElemental):
            return 2
        return 1
    @classmethod
    def get_cost(cls):
        return cls().cost

class EarthElemental(Unit):
    def __init__(self):
        super().__init__(health=100, attack=15, defense=20, cost=10)

    def get_damage_multiplier(self, attacker):
        if isinstance(attacker, WaterElemental):
            return 2
        elif isinstance(attacker, AirElemental):
            return 0.5
        return 1
    @classmethod
    def get_cost(cls):
        return cls().cost
