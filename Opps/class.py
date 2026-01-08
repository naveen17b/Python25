
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"Car Brand: {self.brand}, Model: {self.model}"
    

class Sports_car(Car):
    def __init__(self, brand, model, top_speed):
        super().__init__(brand, model)
        self.top_speed = top_speed

my_super_car = Sports_car("ferrari", "488 spider", "330 km/h")
print(my_super_car.display_info())
 
my_car = Car("tata", "nexon")
print(my_car.brand)
print(my_car.model)
print(my_car.display_info())


