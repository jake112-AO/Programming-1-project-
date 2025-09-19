class Pakuri:
    def __init__(self, species):
        self.species = species
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13
    def get_species(self):
        return self.species 
    
    def get_attack(self):
        return self.attack
    
    def get_defense(self):
        return self.defense
    
    def get_speed(self):
        return self.speed
    
    def __lt__(self, other):
        return self.species <= other.species
    
    def set_attack(self, new_attack):
        self.attack = new_attack
    def evolve(self):
        self.attack = self.attack * 2
        self.defense = self.defense * 4
        self.speed = self.speed * 3 
        