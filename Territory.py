class Territory():
    def __init__(self, name, neighbours):
        self.name = name
        self.owner = False
        self.troops = 0
        self.neighbours = neighbours

    def is_neighbours_with(self, other_region):
        for neighbour in self.neighbours:
            if neighbour == other_region:
                return True
        return False
    
    def add_troops(self, troop_count):
        self.troops += troop_count

    def remove_troops(self, troop_count):
        if self.troops > troop_count:
            self.troops -= troop_count
            return True
        return False

    def move_troops(self, destination, troop_count):
        if self.remove_troops(troop_count) and self.owner == destination.owner:
                destination.add_troops(troop_count)
                return

    def attack(self, other_region, blitz=True):
        if blitz:
            if self.troops > other_region.troops:
                self.troops -= other_region.troops
                other_region.owner = self.owner
                other_region.troops = self.troops - 1
                self.troops = 1
                return
            other_region.troops -= self.troops - 1
            self.troops = 1
            
        
        
