# Пиши свій код тут
class Animal:
    def __init__(self, name: str, current_fead: int, max_fead: int, speed: int, loss_fead_per_km: int, position: int = 0):
        self.name = name
        self.current_fead = current_fead
        self.max_fead = max_fead
        self.speed = speed
        self.loss_fead_per_km = loss_fead_per_km
        self.position = position
        
    def __str__(self) -> str:
        return f"{self.name} Feed: {self.current_fead}/{self.max_fead} Speed: {self.speed} Loss: {self.loss_fead_per_km} | Position: {self.position}"
        
    def can_move_to (self, distance: int, animal):
        if self.current_fead >= animal.current_fead:
            return False
        else:
            self.current_fead += distance - self.loss_fead_per_km * distance / 100
            self.position += distance
            return True
        

    

cat = Animal("Cat", 70, 200, 20, 2)

print( cat)
print(cat.can_move_to(10, cat)) # Має повернути: True
print(cat.can_move_to(100, cat)) # Має повернути: False
