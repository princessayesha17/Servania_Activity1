class Car:
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer = 0          # total km na natakbo ng kotse

    def drive(self, km):
        if km <= 0:                # validation
            print("Invalid: ang km ay dapat higit sa 0.")
            return
        self.odometer += km
        print(f"Nag-drive ng {km} km. Total: {self.odometer} km")

    def age(self, current_year):
        return current_year - self.year

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} - {self.odometer} km"


car1 = Car("Toyota", "Vios", 2020)
car1.drive(50)
car1.drive(120)
car1.drive(-10)     # dapat mag-invalid
car1.drive(0)       # dapat mag-invalid
print("Age:", car1.age(2026), "taon")
print(car1)