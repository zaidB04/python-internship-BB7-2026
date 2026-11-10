class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"My car is {self.brand} {self.model}, manufactured in {self.year}.")


car1 = Car("Suzuki", "Fronx", 2026)
car2 = Car("hyundai", "exeter", 2025)
car3 = Car("Honda", " Amaze", 2023)

car1.display_info()
car2.display_info()
car3.display_info()