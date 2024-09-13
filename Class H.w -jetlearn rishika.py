class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        return f"The engine of the {self.year} {self.make} {self.model} is now running."

    def stop_engine(self):
        return f"The engine of the {self.year} {self.make} {self.model} is now off."

car1=Car("toyota","yaris",2012)
print(car1.start_engine())
print(car1.stop_engine())

car2=Car("Tesla"," model S",2000)
print(car2.start_engine())
print(car2.stop_engine())