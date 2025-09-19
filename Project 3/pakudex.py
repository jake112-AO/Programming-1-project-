from pakuri import Pakuri

class Pakudex:
    
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.size = 0
        self.my_pakudex = []

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        if not self.my_pakudex:
            return None 
    
        return [each_pakuri.get_species() for each_pakuri in self.my_pakudex]


    def get_stats(self, species):
        for each_pakuri in self.my_pakudex:
            if each_pakuri.get_species() == species:
                return [each_pakuri.get_attack(), each_pakuri.get_defense(), each_pakuri.get_speed()]

        return None  

    def sort_pakuri(self):
        self.my_pakudex.sort(key=lambda pakuri: pakuri.get_species())
    
    def add_pakuri(self, species):
        if self.size >= self.capacity:
            return False  
        for each_pakuri in self.my_pakudex:
            if each_pakuri.get_species() == species:
                return False

        self.my_pakudex.append(Pakuri(species))
        self.size += 1
        return True 

    def evolve_species(self, species):
        for each_pakuri in self.my_pakudex:
            if each_pakuri.get_species() == species:
                each_pakuri.evolve()
                return True  
        return False 

    
