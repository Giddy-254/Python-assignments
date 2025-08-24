
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f"This is a {self.brand} {self.model}.")
        

class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model) 
        self.__storage = storage        
        self.battery = battery

    def get_storage(self):
        return self.__storage
    
    def install_app(self, app_name):
        print(f"{app_name} installed on {self.brand} {self.model}!")

    def charge(self):
        print(f"{self.brand} {self.model} is charging 🔋")


phone1 = Smartphone("Samsung", "Galaxy S23", "256GB", "5000mAh")
phone2 = Smartphone("Apple", "iPhone 15", "128GB", "4200mAh")

phone1.info()
phone1.install_app("WhatsApp")
print("Storage:", phone1.get_storage())
phone2.charge()

#  polymorphism challenge
class Animal:
    def move(self):
        pass  

class Dog(Animal):
    def move(self):
        print("Running 🐕")

class Bird(Animal):
    def move(self):
        print("Flying 🐦")

class Fish(Animal):
    def move(self):
        print("Swimming 🐟")


animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()   
