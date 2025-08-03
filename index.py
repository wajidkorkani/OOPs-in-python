class Person:
    def __init__(self, name="John", age=49):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
person1 = Person("Alice", 30)
print(person1.greet())

person2 = Person()
print(person2.greet())
