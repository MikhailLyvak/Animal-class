# Пиши свій код тут
from turtle import position


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
        
   def can_move_to (self, distance: int, animal: "Animal") -> bool:
        required_feed = distance * self.loss_fead_per_km
        return animal.current_fead >= required_feed
    
    def move_to(self, distance: int) -> None:
        if self.can_move_to(distance, self):
             self.position += distance
             self.current_fead -= distance * self.loss_fead_per_km
             print(f"Тваринка перемістилась на відстань {distance}.")
        else:
            print("Not enough feed")

    def feed (self, calories: int) -> None:
        if self.current_fead + calories <= self.max_fead:
            self.current_fead += calories
        else:
            print("Too much feed")
        



cat = Animal("Cat", 70, 200, 20, 2)
print(cat)
cat.move_to(30)
print(cat)
