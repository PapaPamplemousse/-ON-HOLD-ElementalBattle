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
        if self.is_in_range(enemy):
            damage = self.attack - enemy.defense
            enemy.take_damage(damage)
            print(f"{self.__class__.__name__} a infligé {damage} points de dégâts à {enemy.__class__.__name__}")

    def is_in_range(self, enemy):
        """Check if the enemy unit is in attack range."""
        raise NotImplementedError("is_in_range() doit être implémentée dans les sous-classes.")

    def move_towards_enemy(self, enemies, board):
        closest_enemy = None
        min_distance = float("inf")

        for enemy in enemies:
            distance = abs(self.x - enemy.x) + abs(self.y - enemy.y)
            if distance < min_distance:
                min_distance = distance
                closest_enemy = enemy

        dx = closest_enemy.x - self.x
        dy = closest_enemy.y - self.y

        move_x, move_y = 0, 0
        if abs(dx) > abs(dy):
            move_x = 1 if dx > 0 else -1
        else:
            move_y = 1 if dy > 0 else -1

        new_x, new_y = self.x + move_x, self.y + move_y
        if 0 <= new_x < board.size and 0 <= new_y < board.size:
            board.move_unit(self, new_x, new_y)
            self.x, self.y = new_x, new_y
        

class FireElemental(Unit):
    def __init__(self):
        super().__init__(health=60, attack=30, defense=10, cost=10)

    def get_damage_multiplier(self, attacker):
        if isinstance(attacker, AirElemental):
            return 0.5
        elif isinstance(attacker, WaterElemental):
            return 2
        return 1
    
    def is_in_range(self, enemy):
        x_diff = abs(self.x - enemy.x)
        y_diff = abs(self.y - enemy.y)
        return x_diff == 2 and y_diff == 2
    
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
    
    def is_in_range(self, enemy):
        x_diff = abs(self.x - enemy.x)
        y_diff = abs(self.y - enemy.y)
        return x_diff == 2 and y_diff == 2
    
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
    
    def is_in_range(self, enemy):
        x_diff = abs(self.x - enemy.x)
        y_diff = abs(self.y - enemy.y)
        return (x_diff == 1 and y_diff == 0) or (x_diff == 0 and y_diff == 1)
    
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
    
    def is_in_range(self, enemy):
        x_diff = abs(self.x - enemy.x)
        y_diff = abs(self.y - enemy.y)
        return (x_diff == 1 and y_diff == 0) or (x_diff == 0 and y_diff == 1)
    
    @classmethod
    def get_cost(cls):
        return cls().cost
