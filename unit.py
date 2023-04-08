class Unit:
    def __init__(self, health, attack, defense, cost):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.cost = cost

    def is_alive(self):
        """Return True if the unit is alive, otherwise False."""
        return self.health > 0

    def take_damage(self, damage):
        """Reduce the unit's health by the amount of damage, considering defense."""
        self.health -= max(0, damage - self.defense)

    def attack_enemy(self, enemy):
        """Attack the enemy unit and cause damage."""
        if self.is_alive() and enemy.is_alive():
            enemy.take_damage(self.attack)
