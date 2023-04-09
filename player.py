class Player:
    def __init__(self, name, inventory, gold):
        self.name = name
        self.inventory = inventory
        self.gold = gold
        self.units_lost = 0

    def has_units(self):
        """Return True if the player has any alive units, otherwise False."""
        return any(unit.is_alive() for unit in self.units)

    def earn_gold(self, amount):
        """Increase the player's gold by the specified amount."""
        self.gold += amount
        
    def recruit_unit(self, unit_class, player):
        unit_cost = unit_class.cost
        if self.gold >= unit_cost:
            self.gold -= unit_cost
            self.inventory.append(unit_class(player))  # Pass player as an argument
            return True
        return False
    
    def count_units(self, unit_class):
        return sum(1 for unit in self.inventory if isinstance(unit, unit_class))
    
    def place_unit(self, unit, x, y, board):
        """Place a unit from the inventory onto the board."""
        if unit in self.inventory and board.place_unit(unit, x, y):
            self.inventory.remove(unit)
            self.units.append(unit)
            print(f"{self.name} a placé un {unit.__class__.__name__} en ({x}, {y})")
        else:
            print(f"{self.name} ne peut pas placer l'unité en ({x}, {y})")
