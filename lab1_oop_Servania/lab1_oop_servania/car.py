class Car:
    wheels = 4  # class attribute: pareho para sa lahat ng Car

    def __init__(self, brand, model, year):
        self.brand = brand      # instance attributes: iba-iba bawat Car
        self.model = model
        self.year = year

# tatlong objects
car1 = Car("Toyota", "Vios", 2020)
car2 = Car("Honda", "Civic", 2018)
car3 = Car("Mitsubishi", "Mirage", 2022)

print(car1.brand, car1.model, car1.year, car1.wheels)
print(car2.brand, car2.model, car2.year, car2.wheels)
print(car3.brand, car3.model, car3.year, car3.wheels)
print("Wheels (galing sa class):", Car.wheels)