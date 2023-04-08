class Player:
    def __init__(self, name, units, gold):
        self.name = name
        self.units = units
        self.gold = gold

    def has_units(self):
        """Return True if the player has any alive units, otherwise False."""
        return any(unit.is_alive() for unit in self.units)

    def recruit_unit(self, unit_class):
        """Recruit a new unit if the player has enough gold."""
        if self.gold >= unit_class.cost:
            self.gold -= unit_class.cost
            self.units.append(unit_class)
            print(f"{self.name} a recruté un {unit_class.__class__.__name__}")
        else:
            print(f"{self.name} n'a pas assez d'or pour recruter un {unit_class.__class__.__name__}")
