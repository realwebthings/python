# @property = Decorator used to define a method as property (it can be accessed like an attribute)
#             = It is used to create read-only attributes from methods
#             = It allows you to define a method that can be accessed like an attribute, but it can also be used to perform some calculations or transformations on the data before returning it.
#             = It is commonly used to provide a way to access data from a class without having to call a method explicitly.
#             = It is useful when you want to encapsulate the logic of getting and setting a value, and you want to provide a more convenient way to access that value.
#             = It is also useful when you want to add some additional logic or validation when getting or setting the value, without having to modify the underlying method.
#             = It is often used in conjunction with the @property decorator, which allows you to define a method as a property, and the @property.decorator allows you to define a method as a property with additional functionality.
#             = It is commonly used in scenarios where you want to provide a read-only attribute that is calculated based on other attributes or data, or where you want to provide a way to access data from a class without having to call a method explicitly.
#             = It is also commonly used in frameworks and libraries that use object-oriented programming, such as Django and SQLAlchemy, where properties are used to define the attributes of models and to provide additional functionality when accessing or modifying those attributes.
#             Benefits = Add additonal logic when read, write or delete attributes
#             Gives you better, setter and deleter method

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @property
    def age(self):
        return 2023 - self.year

car = Car("Toyota", "Corolla", 2015)

print(car.age) # Output: 8
print(car.make) # Output: Toyota
print(car.model) # Output: Corolla
print(car.year) # Output: 2015


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
    
    @age.deleter
    def age(self):
        print("Deleting age...")
        self._age = None

person = Person("John", 30)
print(f"Initial age: {person.age}")  # Output: 30
person.age = 35
print(f"Updated age: {person.age}")  # Output: 35

# Test deleter
del person.age
print(f"Age after deletion: {person.age}")  # Output: None



class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def diameter(self):
        return 2 * self.radius
    
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
        print("Diameter updated")
    
    @diameter.deleter
    def diameter(self):
        print("Resetting circle to unit circle (radius = 1)")
        self.radius = 1
    
    @property
    def area(self):
        return 3.14159 * self.radius ** 2
    
    @property
    def circumference(self):
        return 2 * 3.14159 * self.radius
    

print("\n=== Person Examples ===")
print("\n=== Circle Examples ===")
circle = Circle(5)
print(f"Initial radius: {circle.radius}")  # Output: 5
print(f"Initial diameter: {circle.diameter}")  # Output: 10
print(f"Initial area: {circle.area:.2f}")  # Output: 78.54
print(f"Initial circumference: {circle.circumference:.2f}")  # Output: 31.42

# Update diameter (this will change radius)
circle.diameter = 12
print(f"\nAfter setting diameter to 12:")
print(f"Radius: {circle.radius}")  # Output: 6.0
print(f"Diameter: {circle.diameter}")  # Output: 12.0
print(f"Area: {circle.area:.2f}")  # Output: 113.10
print(f"Circumference: {circle.circumference:.2f}")  # Output: 37.70

# Test deleter
print(f"\nBefore deletion - Radius: {circle.radius}")
del circle.diameter
print(f"After deletion - Radius: {circle.radius}")  # Output: 1
print(f"After deletion - Diameter: {circle.diameter}")  # Output: 2


# Comprehensive example with all three decorators
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Get temperature in Celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius with validation"""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        print(f"Setting temperature to {value}°C")
        self._celsius = value
    
    @celsius.deleter
    def celsius(self):
        """Reset temperature to absolute zero"""
        print("Resetting temperature to absolute zero")
        self._celsius = -273.15
    
    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature using Fahrenheit"""
        celsius_value = (value - 32) * 5/9
        self.celsius = celsius_value  # Use celsius setter for validation
    
    @property
    def kelvin(self):
        """Get temperature in Kelvin"""
        return self._celsius + 273.15

print("\n=== Temperature Examples ===")
temp = Temperature(25)  # 25°C
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit:.1f}°F")
print(f"Kelvin: {temp.kelvin:.1f}K")

# Set using Fahrenheit
temp.fahrenheit = 100  # 100°F
print(f"\nAfter setting to 100°F:")
print(f"Celsius: {temp.celsius:.1f}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")
print(f"Kelvin: {temp.kelvin:.1f}K")

# Delete (reset to absolute zero)
del temp.celsius
print(f"\nAfter deletion:")
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit:.1f}°F")
print(f"Kelvin: {temp.kelvin}K")

# Try invalid temperature
try:
    temp.celsius = -300  # Below absolute zero
except ValueError as e:
    print(f"\nError: {e}")


