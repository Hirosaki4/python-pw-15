class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def get_info(self):
        return f"{self.name}, {self.age} років, м. {self.city}"


# Приклад використання
person1 = Person("Олег", 25, "Київ")
print(person1.get_info())
