class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def get_full_info(self):
        return f"{self.brand} {self.model}, {self.year} року, колір: {self.color}"

    def change_color(self, new_color):
        self.color = new_color


# Приклад використання
car1 = Car("Toyota", "Camry", 2020, "чорний")
print(car1.get_full_info())
car1.change_color("білий")
print("Після зміни кольору:", car1.get_full_info())
