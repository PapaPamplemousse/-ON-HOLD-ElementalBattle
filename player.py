class Player:
    def __init__(self, name, units, gold):
        self.name = name
        self.units = units
        self.inventory = []
        self.gold = gold
        self.units_lost = 0

    def has_units(self):
        """Return True if the player has any alive units, otherwise False."""
        return any(unit.is_alive() for unit in self.units)

    def recruit_unit(self, unit_class):
        """Recruit a new unit if the player has enough gold."""
        if self.gold >= unit_class.get_cost():
            self.gold -= unit_class.get_cost()
            self.units.append(unit_class())
            print(f"{self.name} a recruté un {unit_class.__name__}")
        else:
            print(f"{self.name} n'a pas assez d'or pour recruter un {unit_class.__name__}")

    def earn_gold(self, amount):
        """Increase the player's gold by the specified amount."""
        self.gold += amount
        
    def recruit_unit(self, unit_class):
        """Recruit a new unit if the player has enough gold."""
        if self.gold >= unit_class.get_cost():
            self.gold -= unit_class.get_cost()
            self.inventory.append(unit_class())
            print(f"{self.name} a recruté un {unit_class.__name__}")
        else:
            print(f"{self.name} n'a pas assez d'or pour recruter un {unit_class.__name__}")

    def place_unit(self, unit, x, y, board):
        """Place a unit from the inventory onto the board."""
        if unit in self.inventory and board.place_unit(unit, x, y):
            self.inventory.remove(unit)
            self.units.append(unit)
            print(f"{self.name} a placé un {unit.__class__.__name__} en ({x}, {y})")
        else:
            print(f"{self.name} ne peut pas placer l'unité en ({x}, {y})")
