class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
    
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness += 1
        if self.happiness > 10:
            self.happiness = 10
        print(f"{self.name} ate some food and is now less hungry!")
    
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} had a good nap and is now refreshed!")
    
    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} had fun playing!")
    
    def get_status(self):
        print(f"\n----- {self.name}'s Status -----")
        print(f"Hunger: {'🍗' * self.hunger + '◻️' * (10 - self.hunger)} ({self.hunger}/10)")
        print(f"Energy: {'⚡' * self.energy + '◻️' * (10 - self.energy)} ({self.energy}/10)")
        print(f"Happiness: {'😀' * self.happiness + '◻️' * (10 - self.happiness)} ({self.happiness}/10)")
    
    def train(self, trick):
        if self.energy >= 3 and self.hunger <= 7:
            self.tricks.append(trick)
            self.energy -= 3
            self.hunger += 2
            self.happiness += 1
            print(f"{self.name} learned how to {trick}!")
        else:
            print(f"{self.name} is too tired or hungry to learn a new trick right now.")
    
    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} doesn't know any tricks yet.")
        else:
            print(f"\n----- {self.name}'s Tricks -----")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")