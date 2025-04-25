def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Adding sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("Adding fudge")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream")


get_ice_cream("chocolate")

# Static method
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

# Using the static method
res = MathOperations.add(5, 3)
print(res)  

# Class method
class Employee:
    raise_amount = 1.05

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

# Using the class method
Employee.set_raise_amount(1.10)
print(Employee.raise_amount)  

# @property
print("@property decorator")
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative")

    @property
    def area(self):
        return 3.14159 * (self._radius ** 2)

# Using the property
c = Circle(5)
print(c.radius) 
print(c.area)    
c.radius = 10
print(c.area)    


# Chaining Decorators
print("Chaining Decorators")
# code for testing decorator chaining 
def decor1(func): 
    def inner(): 
        x = func() 
        return x * x 
    return inner 

def decor(func): 
    def inner(): 
        x = func() 
        return 2 * x 
    return inner 

@decor1
@decor
def num(): 
    return 10

@decor
@decor1
def num2():
    return 10
  
print(num()) 
print(num2())
