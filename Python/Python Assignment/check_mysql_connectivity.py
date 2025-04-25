import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
)

print("Connected:", conn.is_connected())
conn.close()



nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 2, nums))
print(result)

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def __str__(self):
        return f"The {self.color} car has {self.mileage:,} miles"


car1 = Car("blue", 20_000)
print(car1)
car2 = Car("red", 30_000)   
print(car2)


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class GoldenRetriever(Dog):
    def speak(self, sound = "Bark"):
        return super().speak(sound)


obj1 = GoldenRetriever("Lassie", 8)
print(obj1.speak())

